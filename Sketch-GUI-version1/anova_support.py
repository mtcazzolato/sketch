### 
# Copyright (C) 2021  Mirela Teixeira Cazzolato <mirelac@usp.br>
# Copyright (C) 2021  Lucas Santiago Rodrigues <lucas_rodrigues@usp.br>
# 
# This program is free software: you can redistribute it and/or modify
# # it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
###

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from tkinter import filedialog
from pandastable import Table, TableModel
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sketch_modules.anovaQuery import getANOVAResults

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global VarRunOutput
    VarRunOutput = tk.StringVar()
    VarRunOutput.set('')

    global checkChartHorizontalVar
    checkChartHorizontalVar = tk.IntVar()
    checkChartHorizontalVar.set(1)

    global checkLabelChartVar
    checkLabelChartVar = tk.IntVar()
    checkLabelChartVar.set(1)

    global comboAttReference1
    comboAttReference1 = tk.StringVar()

    global comboAttReference2
    comboAttReference2 = tk.StringVar()
    
    global VarInputFile
    VarInputFile = tk.StringVar()
    VarInputFile.set('')

    global VarInputFileDataType
    VarInputFileDataType = tk.StringVar()
    VarInputFileDataType.set('')

    global spinboxQueryIndex
    spinboxQueryIndex = tk.StringVar()
    spinboxQueryIndex.set('1')

    global spinboxQueryKNN
    spinboxQueryKNN = tk.StringVar()
    spinboxQueryKNN.set('-1')

    global spinboxQueryRadius
    spinboxQueryRadius = tk.StringVar()
    spinboxQueryRadius.set('-1')

    global comboboxAttRefQ
    comboboxAttRefQ = tk.StringVar()

    global dfData
    dfData = pd.DataFrame()

    global dfCTypes
    dfCTypes = pd.DataFrame()

    global dfAnovaResults
    dfAnovaResults = pd.DataFrame()

    global figure_boxplot, CanvasPlotBoxplot

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    global dfData, dfCTypes, usefulColumns, usefulCTypes
    w = gui
    top_level = top
    root = top

    sns.set()

    dfData = args[0]
    dfCTypes = args[1]
    usefulColumns = args[2]
    usefulCTypes = args[3]

    loadData()

def loadData():
    global dfData, dfCTypes, usefulColumns, usefulCTypes

    table = Table(w.TFrameDataMainPage,
                    dataframe=dfData,
                    showtoolbar=True,
                    showstatusbar=True)
        
    table.show()
    table.redraw()

    # REFERENCE:
    # columnTypes = {0 : 'id',
    #                1 : 'date',
    #                2 : 'text',
    #                3 : 'categorical',
    #                4 : 'numerical'}

    categoricalColumns = dfData[dfData.columns[dfCTypes['type'] == 3]].columns
    w.TComboboxAttReference1.configure(values=categoricalColumns.to_list())

    numericalColumns = dfData[dfData.columns[dfCTypes['type'] == 4]].columns
    w.TComboboxAttReference2.configure(values=numericalColumns.to_list())

    sys.stdout.flush()

def btnRunQueryANOVA():
    global dfAnovaResults, figure_boxplot, CanvasPlotBoxplot

    attCategorical  = comboAttReference1.get()
    attNumerical    = comboAttReference2.get()
    
    if (str(attCategorical) == ''):
        tk.messagebox.showinfo(title='Attribute selection',
                                message='Please, a categorical variable.', parent = top_level)
    elif (str(attNumerical) == ''):
        tk.messagebox.showinfo(title='Attribute selection',
                                message='Please, a numerical variable.', parent = top_level)
    
    # To allow reploting charts
    try:
        CanvasPlotBoxplot.get_tk_widget().destroy()
    except:
        pass

    print('Running ANOVA')
    
    VarRunOutput.set('Running...')
    sys.stdout.flush()
    
    try:
        dfAnovaResults = getANOVAResults(attCategorical,
                            attNumerical,
                            dfData)
        
        table = Table(w.TFrameDataMainPageCorrQ,
                    dataframe=dfAnovaResults,
                    showtoolbar=True,
                    showstatusbar=True)

        table.show()
        table.redraw()

        # Generate Boxplot
        figure_boxplot = plt.figure()
        ax = figure_boxplot.subplots()
        
        if (checkChartHorizontalVar.get() == 1):
            sns.boxplot(x = attNumerical, y = attCategorical, data = dfData, color = 'tomato')
            plt.xlabel(attNumerical)
            plt.ylabel(attCategorical)
        else:
            sns.boxplot(x = attCategorical, y = attNumerical, data = dfData, color = 'tomato')
            plt.xlabel(attCategorical)
            plt.ylabel(attNumerical)
            plt.xticks(rotation=45)

        print('values checks')
        print(checkChartHorizontalVar.get(), checkLabelChartVar.get())

        if (checkLabelChartVar.get() != 1):
            plt.xticks([])
            plt.yticks([])

        plt.tight_layout()

        CanvasPlotBoxplot = FigureCanvasTkAgg(figure_boxplot, master=w.TFrameDataMainPageCompQ)
        CanvasPlotBoxplot.draw()
        CanvasPlotBoxplot.get_tk_widget().pack(side=tk.TOP, fill=tk.X)

        VarRunOutput.set('Done.')
    except:
        VarRunOutput.set('Please, change chosen variable.')
        
    print('Finished running.')
    
    sys.stdout.flush()

def btnCloseAnovaWindow():
    destroy_window()

def btnSaveAnovaResults():
    global dfAnovaResults
    
    if (len(dfAnovaResults) == 0):
        tk.messagebox.showinfo(title='No data to save',
                                message='Please, generate ANOVA information to save.', parent = top_level)
    else:
        inputFolder = '~/Documents/'
        fname = tk.filedialog.asksaveasfile(
                initialdir = inputFolder,
                title = "Save the ANOVA results",
                filetypes = (("csv files","*.csv"),("all files","*.*")),
                parent = top_level
        )

        # Save output files
        dfAnovaResults.to_csv(str(fname.name), sep=';', index=False)

    sys.stdout.flush()

def btnSaveBoxplotImage():
    global figure_boxplot
    
    try:
        inputFolder = '~/Documents/'
        fname = tk.filedialog.asksaveasfile(
                initialdir = inputFolder,
                title = "Inform the image name to save",
                filetypes = (("png files","*.png"),("all files","*.*")),
                parent = top_level
        )

        if (fname is not None):
            figure_boxplot.savefig(fname.name, dpi=500, bbox_inches='tight')
    except:
        tk.messagebox.showinfo(title='No plot to save',
                                message='Please, generate boxplot to save.', parent = top_level)
        
    sys.stdout.flush()

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import anova
    anova.vp_start_gui()
