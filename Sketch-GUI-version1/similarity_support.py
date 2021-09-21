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

from tkinter import Canvas, filedialog
from pandastable import Table, TableModel
from sketch_modules.corrCompleteTuples import runCorrelation
from sketch_modules.completeQuery import runCompleteQueries
from sketch_modules.mdsCompleteTuple import runMDS
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
    global radioQueryVar
    radioQueryVar = tk.IntVar()
    radioQueryVar.set(1)

    global varCheckHeatBar
    varCheckHeatBar = tk.IntVar()
    varCheckHeatBar.set(0)

    global varCheckHeatLegend
    varCheckHeatLegend = tk.IntVar()
    varCheckHeatLegend.set(1)

    global selectedButton
    selectedButton = tk.IntVar()

    global comboboxAttRefQ
    comboboxAttRefQ = tk.StringVar()

    global VarInputFileDataType
    VarInputFileDataType = tk.StringVar()
    VarInputFileDataType.set('')

    global spinboxQueryKNN
    spinboxQueryKNN = tk.StringVar()
    spinboxQueryKNN.set('1')

    global spinboxQueryRadius
    spinboxQueryRadius = tk.StringVar()
    spinboxQueryRadius.set('0.01')

    global spinboxQueryIndex
    spinboxQueryIndex = tk.StringVar()
    spinboxQueryIndex.set('1')

    global RunningTextVar
    RunningTextVar = tk.StringVar()
    RunningTextVar.set('')

    global SpinboxPercentSampleData
    SpinboxPercentSampleData = tk.StringVar()
    SpinboxPercentSampleData.set('5')

    global VarInputFile
    VarInputFile = tk.StringVar()
    VarInputFile.set('')

    global dfData
    dfData = pd.DataFrame()

    global dfCTypes
    dfCTypes = pd.DataFrame()

    global dfCorrelations
    dfCorrelations = pd.DataFrame()

    global usefulColumns
    usefulColumns = []

    global usefulCTypes
    usefulCTypes = []

    global CanvasPlotHeatmap, CanvasPlotScatterMDSCorr, CanvasPlotScatterMDSTrad

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    global varCheckHeatBar, varCheckHeatLegend
    global dfData, dfCTypes, usefulColumns, usefulCTypes
    global spinboxQueryRadius, spinboxQueryKNN
    sns.set()

    w = gui
    top_level = top
    root = top
    
    dfData = args[0]
    dfCTypes = args[1]
    usefulColumns = args[2]
    usefulCTypes = args[3]

    w.TComboboxAttReferenceQ.configure(values=usefulColumns.to_list())
    spinboxQueryKNN.set(1)
    spinboxQueryRadius.set(0)

def btnComputeCorrelation():
    global dfData, dfCTypes, dfCorrelations, CanvasPlotHeatmap
    
    RunningTextVar.set('Status: Computing the correlation...')
    sampleFraction = float(float(SpinboxPercentSampleData.get())/100)

    # Get data sample
    dfSample = dfData.sample(frac = sampleFraction)
    dfSample.reset_index(inplace=True, drop=True)
    dfCorrelations = runCorrelation(dfSample, dfCTypes, 'Pearson')
    RunningTextVar.set('Status: Done.')

    # sns.set(font_scale=.5)
    # figure = plt.figure(figsize=(4, 4))
    # ax = figure.subplots()
    #sns.heatmap(matrix, square=True, cbar=False)

    heatmap_figure = plt.figure()
    ax = sns.heatmap(dfCorrelations, square=False, cmap='vlag', vmin=-1., vmax=1., cbar=varCheckHeatBar.get()==1)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')

    plt.xlabel(None)
    plt.ylabel(None)
    plt.xticks(size=6, rotation=90)

    if (varCheckHeatLegend.get() == 1):
        plt.yticks(size=6)
    else:
        plt.yticks([], size=6)
    
    plt.tight_layout()
    
    # To allow reploting charts
    try:
        CanvasPlotHeatmap.get_tk_widget().destroy()
    except:
        pass

    #w.TFrameHeatmapFig=ttk.Frame(relief = 'groove',borderwidth = '2')
    #w.TFrameHeatmapFig.pack(side = tk.TOP, fill = tk.BOTH, expand = 1,)
    CanvasPlotHeatmap = FigureCanvasTkAgg(heatmap_figure, master=w.TFrameHeatmapFig)
    CanvasPlotHeatmap.draw()
    CanvasPlotHeatmap.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    sys.stdout.flush()

def btnRetrieveTuples():
    global dfData, dfCTypes
    
    qObjIndex = spinboxQueryIndex.get()
    k = int(spinboxQueryKNN.get())
    rangeq = float(spinboxQueryRadius.get())
    
    if (radioQueryVar.get()==1): # KNN selected
        rangeq = float(-1.0)
    else: # Range selected
        k = int(-1)

    dfResultComplete = runCompleteQueries(dfData.iloc[[qObjIndex]], dfData, dfCTypes, k, rangeq, [], 2, True)

    dfShow = dfData.iloc[dfResultComplete.iloc[0].values[0]]
    dfShow.reset_index(inplace=True)

    table = Table(w.TFrameDataMainPageCompQ, dataframe=dfShow, showtoolbar=True, showstatusbar=True)
    table.show()
    table.redraw()

    sys.stdout.flush()

def btnRetrieveTuplesCorr():
    global dfData, dfCTypes, dfCorrelations, comboboxAttRefQ

    print('Selected value:', comboboxAttRefQ.get())

    if (comboboxAttRefQ.get() == ''):
        tk.messagebox.showinfo(title='Sketch', message='Select a reference attribute to use as query weight.', parent = top_level)

    elif (comboboxAttRefQ.get() not in dfData.columns):
        tk.messagebox.showinfo(title='Sketch', message='Invalid reference attribute.\nSelect a reference attribute to use as query weight.', parent = top_level)

    elif (len(dfCorrelations) == 0):
        tk.messagebox.showinfo(title='Sketch', message='Compute correlation matrix first.', parent = top_level)

    else:
        referenceAttribute = comboboxAttRefQ.get()
        qObjIndex = spinboxQueryIndex.get()
        k = int(spinboxQueryKNN.get())
        rangeq = float(spinboxQueryRadius.get())
        
        if (radioQueryVar.get()==1): # KNN selected
            rangeq = float(-1.0)
        else: # Range selected
            k = int(-1)

        # Initialize weights
        weights = [0.] * len(dfData.columns)

        # Get (absolute) correlation valus form the reference attribute
        wSelectedColumns = dfCorrelations[referenceAttribute].abs().values

        # Replace NaN with zero
        s = np.isnan(wSelectedColumns)
        wSelectedColumns[s] = 0.0

        windex = 0
        for i in range(len(dfData.columns)):
            if (dfCTypes['type'].loc[i] > 1):
                weights[i] = wSelectedColumns[windex]
                windex+=1

        dfResultComplete = runCompleteQueries(dfData.iloc[[qObjIndex]],
            dfData.iloc[0:100], dfCTypes, k, rangeq, pd.Series(weights), 2, True)

        dfShow = dfData.iloc[dfResultComplete.iloc[0].values[0]]
        dfShow.reset_index(inplace=True)

        table = Table(w.TFrameDataMainPageCorrQ,
                dataframe=dfShow,
                showtoolbar=True,
                showstatusbar=True)
        
        #w.TFrameData.table = pt = Table()
        table.show()
        table.redraw()
        sys.stdout.flush()

def btnScatterPlot():
    global dfData, dfCTypes, CanvasPlotScatterMDSTrad
    mds_coords = runMDS(dfData.loc[0:200], dfCTypes, [], p=2, normalized=False)

    figure = plt.figure()
    ax = figure.subplots()
    plt.scatter(mds_coords[:,0], mds_coords[:,1], facecolors = 'blue', s=8)
    plt.xticks([],size=6)
    plt.yticks([],size=6)
    plt.tight_layout(pad=0.05)
    ax.grid(True)

    # To allow reploting charts
    try:
        CanvasPlotScatterMDSTrad.get_tk_widget().destroy()
    except:
        pass

    # Show scatter plot with the traditional query
    CanvasPlotScatterMDSTrad = FigureCanvasTkAgg(figure, master=w.TFrameScatterMDSTraditional)
    CanvasPlotScatterMDSTrad.draw()
    CanvasPlotScatterMDSTrad.get_tk_widget().pack(side=tk.TOP, fill=tk.X)

    sys.stdout.flush()

def btnScatterPlotCorr():
    global dfData, dfCTypes, dfCorrelations, comboboxAttRefQ, CanvasPlotScatterMDSCorr

    referenceAttribute = comboboxAttRefQ.get()
    # Initialize weights
    weights = [0.] * len(dfData.columns)

    # Get (absolute) correlation valus form the reference attribute
    wSelectedColumns = dfCorrelations[referenceAttribute].abs().values

    # Replace NaN with zero
    s = np.isnan(wSelectedColumns)
    wSelectedColumns[s] = 0.0

    windex = 0
    for i in range(len(dfData.columns)):
        if (dfCTypes['type'].loc[i] > 1):
            weights[i] = wSelectedColumns[windex]
            windex+=1

    mds_coords = runMDS(dfData.loc[0:200], dfCTypes, pd.Series(weights), p=2, normalized=False)

    figure = plt.figure()
    ax = figure.subplots()
    plt.scatter(mds_coords[:,0], mds_coords[:,1], facecolors = 'blue', s=8)
    plt.xticks([],size=6)
    plt.yticks([],size=6)
    plt.tight_layout(pad=0.05)
    ax.grid(True)

    # To allow reploting charts
    try:
        CanvasPlotScatterMDSCorr.get_tk_widget().destroy()
    except:
        pass

    # Show scatter plot with the correlated query
    CanvasPlotScatterMDSCorr = FigureCanvasTkAgg(figure, master=w.TFrameScatterMDSCorrelation)
    CanvasPlotScatterMDSCorr.draw()
    CanvasPlotScatterMDSCorr.get_tk_widget().pack(side=tk.TOP, fill=tk.X)

    sys.stdout.flush()

def cmbKnnSelected():
    global radioQueryVar
    print(radioQueryVar.get())
    sys.stdout.flush()

def cmbRangeSelected():
    global radioQueryVar
    print(radioQueryVar.get())
    sys.stdout.flush()

def btnSaveHeatmap():
    global heatmap_figure

    inputFolder = '~/Documents/'
    fname = tk.filedialog.asksaveasfile(
            initialdir = inputFolder,
            title = "Inform the image name to save",
            filetypes = (("png files","*.png"),("all files","*.*")),
            parent = top_level
    )

    heatmap_figure.savefig(fname.name, dpi=500)
    sys.stdout.flush()

def TButtonCloseSimilarity():
    destroy_window()

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import similarity
    similarity.vp_start_gui()
