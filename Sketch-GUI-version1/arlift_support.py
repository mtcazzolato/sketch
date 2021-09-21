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
import os
import pandas as pd
import numpy as np
import subprocess # to run bash commands
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from pandastable import Table, TableModel
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk, Image
from tkinterhtml import HtmlFrame
from colorutils import Color
from ast import literal_eval
from sketch_modules.arlProcess import runARL, getSankeyParameters, readInputData

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
    global entryInputTransactionsVar
    entryInputTransactionsVar = tk.StringVar()

    global entryInputRulesVar
    entryInputRulesVar = tk.StringVar()

    global spinboxMinSupport
    spinboxMinSupport = tk.StringVar()
    spinboxMinSupport.set('0.35')

    global spinboxMinConfidence
    spinboxMinConfidence = tk.StringVar()
    spinboxMinConfidence.set('0.35')
    
    global listSelectedAttributesVar
    listSelectedAttributesVar = tk.StringVar()

    global selectedAttribute
    selectedAttribute = tk.StringVar()
    
    global spinboxKValue
    spinboxKValue = tk.StringVar()

    global TLabelResult
    TLabelResult = tk.StringVar()

    global selectedAttList
    selectedAttList = []

    global imgARL_figure, imgARL_file
    imgARL_file = '~temp.png'
    global availableAttributes

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    global dfData, dfCTypes, usefulColumns, usefulCTypes
    global availableAttributes

    w = gui
    top_level = top
    root = top

    sns.set()

    dfData = args[0]
    dfCTypes = args[1]
    usefulColumns = args[2]
    usefulCTypes = args[3]

    # Set attribute list and add it to the corresponding combobox
    availableAttributes = usefulColumns.to_list()
    w.TComboboxSelectedAttribute.configure(values=availableAttributes)

def btnAddAttToList():
    global listSelectedAttributesVar, selectedAttList, availableAttributes

    # Get selected item
    selectedAtt = w.TComboboxSelectedAttribute.get()

    # If one item was selected
    if (selectedAtt != ''):
        # Remove attribute from the ones available
        availableAttributes.remove(selectedAtt)
        w.TComboboxSelectedAttribute.configure(values=availableAttributes)
        
        # Append attribute to the list of selected ones
        selectedAttList.append(selectedAtt)
        listSelectedAttributesVar.set(selectedAttList)

        # Set the item of the combobox to the first attribute available
        if (len(availableAttributes) > 0):
            w.TComboboxSelectedAttribute.set(availableAttributes[0])
        else:
            w.TComboboxSelectedAttribute.set('')
    
    sys.stdout.flush()

def btnRemoveAttFromList():
    global listSelectedAttributesVar, selectedAttList, availableAttributes
    
    # Get item currently seleted in the listbox of attributes
    currentSelection = w.ScrolledlistboxSelectedAttributes.curselection()

    # If list is not empty and an item is selected
    if (len(currentSelection) != 0): 
        # Get current selection and remove it from the list
        selectedAtt = w.ScrolledlistboxSelectedAttributes.get(currentSelection)
        selectedAttList.remove(selectedAtt)
        listSelectedAttributesVar.set(selectedAttList)

        # Add attribute to the combobox of avaliable ones
        availableAttributes.append(selectedAtt)
        w.TComboboxSelectedAttribute.configure(values=availableAttributes)

        # Set focus to the first item of the combobox
        w.TComboboxSelectedAttribute.set(availableAttributes[0])

    sys.stdout.flush()

def btnDiscoverARL():
    global dfData, usefulColumns, selectedAttList
    global transactions, dfARules
    global spinboxMinSupport, spinboxMinConfidence
    global imgARL_figure, imgARL_file

    if (len(selectedAttList) == 0):
        tk.messagebox.showinfo(title='No attribute selected', message='Please, select the attributes\nto generate the AR.', parent = top_level)
    else:
        minSup = float(spinboxMinSupport.get())
        minConf = float(spinboxMinConfidence.get())
        print(minSup, minConf)
        transactions, dfARules = runARL(dfData, selectedAttList, minSup, minConf)

        table = Table(w.TFrameData, dataframe=dfARules,
                        showtoolbar=True, showstatusbar=True)
        table.show()
        table.redraw()

        # Get Sankey diagram parameters from association rules
        label, colorvalues, source, target, value, linkColors = getSankeyParameters(dfARules)

        # To use colors in the diagram
        opacity = 0.4

        # Construct Sankey plot
        imgARL_figure = go.Figure(data=[go.Sankey(
                    node = dict(
                        pad = 50, thickness = 15,
                        line = dict(color = 'black', width = 0.5),
                        label = label,
                        color = colorvalues
                    ),
                    textfont  = dict(size =20),
                    link = dict(
                        source = source,
                        target = target,
                        value = value,
                        color = linkColors
                    )
        )])

        # imgARL_figure.show()
        imgARL_figure.write_image(imgARL_file)
        visualizeSankeyDiagram()

    sys.stdout.flush()

def btnLoadTransactions():
    global entryInputTransactionsVar
    inputFolder = '~/Documents/'

    fname = tk.filedialog.askopenfile(mode="r",
            initialdir = inputFolder,
            title = "Select transactions data file",
            filetypes = (("csv files","*.csv"),("text files","*.txt"),("all files","*.*")),
            parent = top_level
    )

    if (fname is not None):
            print('File:', fname.name)
            entryInputTransactionsVar.set(fname.name)
    
    sys.stdout.flush()

def btnLoadARules():
    global entryInputRulesVar

    inputFolder = '~/Documents/'

    fname = tk.filedialog.askopenfile(mode="r",
            initialdir = inputFolder,
            title = "Select assocation rules data file",
            filetypes = (("csv files","*.csv"),("text files","*.txt"),("all files","*.*")),
            parent = top_level
    )

    if (fname is not None):
            print('File:', fname.name)
            entryInputRulesVar.set(fname.name)

    sys.stdout.flush()

def btnLoadFilesAR():
    global entryInputTransactionsVar, entryInputRulesVar
    global imgARL_figure, imgARL_file
    global transactions, dfARules

    print(entryInputTransactionsVar.get(), entryInputRulesVar.get())

    transactions = pd.read_csv(entryInputTransactionsVar.get(), sep = ';')
    dfARules = pd.read_csv(entryInputRulesVar.get(), sep = ';')

    try:
        # Cast attributes containing lists
        dfARules[['antecedents', 'consequents']] = dfARules[['antecedents', 'consequents']].applymap(literal_eval)

        if (len(dfARules) > 0):
                table = Table(w.TFrameData, dataframe=dfARules,
                            showtoolbar=True, showstatusbar=True)
                table.show()
                table.redraw()

                # Get Sankey diagram parameters from association rules
                label, colorvalues, source, target, value, linkColors = getSankeyParameters(dfARules)

                # To use colors in the diagram
                opacity = 0.4

                # Construct Sankey plot
                imgARL_figure = go.Figure(data=[go.Sankey(
                            node = dict(
                                pad = 50, thickness = 15,
                                line = dict(color = 'black', width = 0.5),
                                label = label,
                                color = colorvalues
                            ),
                            textfont  = dict(size =20),
                            link = dict(
                                source = source,
                                target = target,
                                value = value,
                                color = linkColors
                            )
                )])

                imgARL_figure.write_image(imgARL_file)
    
        visualizeSankeyDiagram()
    except:
        print('Warning: exception on arlift_support.btnLoadFilesAR')
        
    sys.stdout.flush()

def btnVisualizeSankeyDiagram():
    visualizeSankeyDiagram()

def visualizeSankeyDiagram():
    global transactions, dfARules
    global imgARL_file

    try:
        if (len(dfARules) == 0):
                tk.messagebox.showinfo(title='No rules to show', message='Please, generate or load AR to visualize.', parent = top_level)
        else:
                image = ImageTk.PhotoImage(Image.open(imgARL_file))  
                w.CanvasPlotAR.create_image(0, 0, anchor='nw', image=image) 
                w.CanvasPlotAR.image = image
    except:
        print('Warning: exception on visualizeSankeyDiagram')
    
    sys.stdout.flush()

def btnVisualizeSankeyDiagramHTML():
    global imgARL_figure, dfARules

    try:
        if (len(dfARules) == 0):
                tk.messagebox.showinfo(title='No rules to show', message='Please, generate or load AR to visualize.', parent = top_level)
        else:
                frame = HtmlFrame(w.CanvasPlotAR, horizontal_scrollbar="auto")
                # frame.grid(sticky=tk.NSEW)
                frame.set_content(imgARL_figure.show())
    except:
        print('Warning: exception on btnVisualizeSankeyDiagramHTML')

    sys.stdout.flush()

def btnSaveSankeyImage():
    global imgARL_figure, dfData
    
    try:
        if (len(dfARules) == 0):
            tk.messagebox.showinfo(title='No image to save', message='Please, generate or load AR\nto visualize and save.', parent = top_level)
        else:
            inputFolder = '~/Documents/'
            fname = tk.filedialog.asksaveasfile(
                initialdir = inputFolder,
                title = "Inform the image name to save",
                filetypes = (("png files","*.png"),("all files","*.*")),
                parent = top_level
            )

            if (fname is not None):
                imgARL_figure.write_image(fname.name)
    except:
        print('Warning: exception on btnSaveSankeyImage')

    sys.stdout.flush()

def btnSaveRulesTransactions():
    global dfARules, transactions
    
    try:
        if (len(dfARules) == 0):
            tk.messagebox.showinfo(title='No rules to save', message='Please, generate or load AR to save.', parent = top_level)
        else:
            inputFolder = '~/Documents/'
            fname = tk.filedialog.asksaveasfile(
                    initialdir = inputFolder,
                    title = "Inform the prefix of files to save",
                    filetypes = (("csv files","*.csv"),("all files","*.*")),
                    parent = top_level
            )
    
            if (fname is not None):
                # Save output files
                dfARules.to_csv(str(fname.name), sep=';', index=False)
                transactions.to_csv(str(fname.name)[:-4] + '-transactions.csv', sep=';', index=False)
    except:
        print('Warning: exception on btnSaveRulesTransactions')
        
    sys.stdout.flush()

def destroy_window():
    # Function which closes the window.
    global top_level, imgARL_file

    # Remove temporary plot file
    if os.path.exists(imgARL_file):
        os.remove(imgARL_file)

    top_level.destroy()
    top_level = None

def btnCloseARL():
    destroy_window()
    
if __name__ == '__main__':
    import arlift
    arlift.vp_start_gui()
    
