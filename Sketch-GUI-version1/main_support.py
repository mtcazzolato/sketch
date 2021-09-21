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

import os
import sys
import numpy as np
import pandas as pd
import psycopg2
from tkinter import filedialog
from pandastable import Table, TableModel
from pathlib import Path

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

import similarity
import arlift
import anova

def set_Tk_var():
    global listDBTablesVar
    listDBTablesVar = tk.StringVar()
    global VarInputDBFile
    VarInputDBFile = tk.StringVar()
    VarInputDBFile.set('')

    global VarQueryText
    VarQueryText = tk.StringVar()

    global VarInputFileDataType
    VarInputFileDataType = tk.StringVar()
    VarInputFileDataType.set('')

    global VarTextQuery
    VarTextQuery = tk.StringVar()
    VarTextQuery.set('')
    
    global VarInputFile
    VarInputFile = tk.StringVar()
    VarInputFile.set('')

    global dfData
    dfData = pd.DataFrame()

    global dfCTypes
    dfCTypes = pd.DataFrame()

    global usefulColumns
    usefulColumns = []

    global usefulCTypes
    usefulCTypes = []
    
    global connDB
    connDB = None
    
    global tablesList
    tablesList = []
    
    global currentTable
    currentTable = ''
    
def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    
    loadDatabaseInit()

def btnSelectFile():
    inputFolder = '~/'

    fname = tk.filedialog.askopenfile(mode="r",
            initialdir = inputFolder,
            title = "Select data file",
            filetypes = (("csv files","*.csv"),("text files","*.txt"),("all files","*.*"))
    )

    if (fname is not None):
        print('File:', fname.name)
        VarInputFile.set(fname.name)
        w.TLabelInputFileDisplay.configure(text=fname.name)
    
    sys.stdout.flush()

def btnSelectFileDataType():
    inputFolder = '~/'

    fname = tk.filedialog.askopenfile(mode="r",
            initialdir = inputFolder,
            title = "Select data types file",
            filetypes = (("csv files","*.csv"),("text files","*.txt"),("all files","*.*"))
    )

    if (fname is not None):
        print('File:', fname.name)
        VarInputFileDataType.set(fname.name)
        w.TLabelInputFileDisplay.configure(text=fname.name)
    
    sys.stdout.flush()

def btnLoadFile():
    global dfData, dfCTypes, usefulColumns, usefulCTypes

    #print('FILENAMES:', VarInputFile.get(), VarInputFileDataType.get())

    if (VarInputFile.get() == ''):
        tk.messagebox.showinfo(title='Sketch', message='Input file not informed.', parent = top_level)
    elif (VarInputFileDataType.get() == ''):
        tk.messagebox.showinfo(title='Sketch', message='Input file with data types not informed.', parent = top_level)
    else:
        dfData = pd.read_csv(VarInputFile.get())
        dfCTypes = pd.read_csv(VarInputFileDataType.get())

        table = Table(w.TFrameDataMainPage,
                dataframe=dfData,
                showtoolbar=True,
                showstatusbar=True)

        table.show()
        table.redraw()
        usefulColumns = dfData[dfData.columns[dfCTypes['type'] > 1]].columns

        usefulCTypes = dfCTypes[dfCTypes['type'] > 1]
        usefulCTypes.reset_index(inplace = True, drop = True)

    sys.stdout.flush()

def loadDatabaseInit():
    global connDB, dfData, tablesList
        
    if(os.path.exists('dbFile.txt')):
        
        # Using readlines()
        file1 = open('dbFile.txt', 'r')
        Lines = file1.readlines()
        nameDB = Lines[0].split('=')[1]
        username = Lines[1].split('=')[1]
        pwd = Lines[2].split('=')[1]
        
        w.TEntryDBName.insert(0,nameDB)
        w.TEntryUsername.insert(0,username)
        w.TEntryPassword.insert(0,pwd)
        sys.stdout.flush()

    elif(w.TEntryDBName.get() != '' and w.TEntryDBName.get() != '' and w.TEntryDBName.get() != ''): 
        nameDB = w.TEntryDBName.get()
        username = w.TEntryUsername.get()
        pwd = w.TEntryPassword.get()
    
    if(connDB is None):
        
        try:
            # connect to the PostgreSQL server
            conn = psycopg2.connect("dbname={} user={} password={}".format(nameDB, username, pwd))
            # create a cursor
            cur = conn.cursor()
            # execute a statement
            
            cur.execute('SELECT version()')
            db_version = cur.fetchone()

            # save connection into global variable
            connDB = conn
            
            cur.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND  schemaname != 'information_schema'")
            rows = cur.fetchall()
            for row in rows:
                tablesList +=[row[0]]
                
            cur.execute("SELECT matviewname FROM pg_matviews;")
            rows = cur.fetchall()
            for row in rows:
                tablesList +=[row[0]]
                
            cur.execute("SELECT table_name FROM INFORMATION_SCHEMA.views WHERE table_schema = ANY (current_schemas(false));")      
            rows = cur.fetchall()
            for row in rows:
                tablesList +=[row[0]]
                        
            for i in range(len(tablesList)):
                w.ScrolledlistboxDBTables.insert(i,tablesList[i])        
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
    print('main_support.loadDatabaseInit')
    sys.stdout.flush()
    
def btnLoadDatabase():
    global connDB, dfData, tablesList
        
    if(w.TEntryDBName.get() != '' or w.TEntryDBName.get() != '' or w.TEntryDBName.get() != ''): 
        nameDB = w.TEntryDBName.get()
        username = w.TEntryUsername.get()
        pwd = w.TEntryPassword.get()
                      
        try:
            # connect to the PostgreSQL server
            conn = psycopg2.connect("dbname={} user={} password={}".format(nameDB, username, pwd))
            # create a cursor
            cur = conn.cursor()
            # execute a statement
            
            cur.execute('SELECT version()')
            db_version = cur.fetchone()

            # save connection into global variable
            connDB = conn
            
            cur.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND  schemaname != 'information_schema'")
            rows = cur.fetchall()
            for row in rows:
                tablesList +=[row[0]]
                
            cur.execute("SELECT matviewname FROM pg_matviews;")
            rows = cur.fetchall()
            for row in rows:
                tablesList +=[row[0]]
                
            cur.execute("SELECT table_name FROM INFORMATION_SCHEMA.views WHERE table_schema = ANY (current_schemas(false));")      
            rows = cur.fetchall()
            for row in rows:
                tablesList +=[row[0]]
                        
            for i in range(len(tablesList)):
                w.ScrolledlistboxDBTables.insert(i,tablesList[i])        
            
        except (Exception, psycopg2.DatabaseError) as error:
            tk.messagebox.showinfo(title='Sketch',
                            message='Verify the connection information, please!', parent = top_level) 
    
    else:
         tk.messagebox.showinfo(title='Sketch',
                        message='Insert the connection information, please', parent = top_level) 
            
    print('main_support.btnLoadDatabase')
    sys.stdout.flush()

def btnClearQueryField():
    VarQueryText.set('')    
    sys.stdout.flush()

def btnRunQuery():
    
    global connDB, dfData, dfCTypes, usefulColumns, usefulCTypes
    
    if(connDB is not None):
            
        try:
            cur = connDB.cursor()

            query =  w.EntryQuery.get()
            
            cur.execute("DROP MATERIALIZED VIEW IF EXISTS queryruntime;")
            cur.execute("CREATE MATERIALIZED VIEW queryruntime AS {}".format(query))
            connDB.commit()

            dfData = pd.read_sql_query('SELECT * FROM queryRuntime;',con=connDB)
            
            typesAttributes = pd.read_sql_query("SELECT a.attname, pg_catalog.format_type(a.atttypid, a.atttypmod) FROM pg_attribute a JOIN pg_class t on a.attrelid = t.oid JOIN pg_namespace s on t.relnamespace = s.oid WHERE a.attnum > 0 AND NOT a.attisdropped AND t.relname = 'queryruntime' AND s.nspname = 'public' ORDER BY a.attnum;",con=connDB)
                        
            dfCTypes = pd.DataFrame(columns=['type'])
                        
            for i in range(len(typesAttributes)):
                if(typesAttributes.iloc[i,1] == 'ARRAY'):                                             dfCTypes.loc[len(dfCTypes)] = [5] ### get array type
                elif(typesAttributes.iloc[i,1] == 'integer' or typesAttributes.iloc[i,1] == 'numeric'): dfCTypes.loc[len(dfCTypes)] = [4] ### get numeric type
                elif('character' in typesAttributes.iloc[i,1]):                                       dfCTypes.loc[len(dfCTypes)] = [3] ### get categorical type    
                elif(typesAttributes.iloc[i,1] == 'text' and 'id' not in typesAttributes.iloc[i,0]):  dfCTypes.loc[len(dfCTypes)] = [2] ### get texts type
                elif(typesAttributes.iloc[i,1] == 'date' or typesAttributes.iloc[i,1] == 'datetime'): dfCTypes.loc[len(dfCTypes)] = [1] ### get date type
                elif(typesAttributes.iloc[i,1] == 'text' and 'id' in typesAttributes.iloc[i,0]):      dfCTypes.loc[len(dfCTypes)] = [0] ### get ID type
                else: dfCTypes.loc[len(dfCTypes)] = [-1]
            
            usefulColumns = dfData[dfData.columns[dfCTypes['type'] > 1]].columns

            usefulCTypes = dfCTypes[dfCTypes['type'] > 1]
            usefulCTypes.reset_index(inplace = True, drop = True)
                        

            table = Table(w.TFrameDataMainPage,
                dataframe=dfData,
                showtoolbar=True,
                showstatusbar=True)

            table.show()
            table.redraw()
            for i in range(len(tablesList)):
                w.ScrolledlistboxDBTables.insert(i,tablesList[i])        

        except (Exception, psycopg2.DatabaseError) as error:
             tk.messagebox.showinfo(title='Sketch',
                            message='Unavalible Data, check your query, please!')
    else:
        tk.messagebox.showinfo(title='Sketch',
                            message='Open the connection with the database!') 
    
    print('main_support.btnRunQuery')
    sys.stdout.flush()

def btnOpenSimWindow():
    if ((len(dfData) == 0) or (len(dfCTypes) == 0)):
        tk.messagebox.showinfo(title='Sketch', message='Please, load file with the working data.', parent = top_level)
    else:
        similarity.create_ToplevelSimilarity(root, dfData, dfCTypes, usefulColumns, usefulCTypes)
    sys.stdout.flush()

def btnOpenARLiftWindow():
    if ((len(dfData) == 0) or (len(dfCTypes) == 0)):
        tk.messagebox.showinfo(title='Sketch', message='Please, load file with the working data.', parent = top_level)
    else:
        arlift.create_ToplevelARL(root, dfData, dfCTypes, usefulColumns, usefulCTypes)
    sys.stdout.flush()

def btnOpenAnovaWindow():
    if ((len(dfData) == 0) or (len(dfCTypes) == 0)):
        tk.messagebox.showinfo(title='Sketch', message='Please, load file with the working data.', parent = top_level)
    else:
        anova.create_ToplevelAnova(root, dfData, dfCTypes, usefulColumns, usefulCTypes)
    sys.stdout.flush()

def btnExit():
    sys.stdout.flush()
    sys.exit()

def btnAbout():
    tk.messagebox.showinfo(title='Sketch',
                            message='Citation details, sample files\nand howto use manual are available at\n\'http://github.com/mtcazzolato/sketch\'.', parent = top_level)
    sys.stdout.flush()

def btnLoadSelectedTable():
    global connDB, dfData, dfCTypes, usefulColumns, usefulCTypes, currentTable
            
    try:

        currentTable =  w.ScrolledlistboxDBTables.get(w.ScrolledlistboxDBTables.curselection())
    
        try:
            cur = connDB.cursor()
         
            dfData = pd.read_sql_query('SELECT * FROM {};'.format(currentTable),con=connDB)
            
            typesAttributes = pd.read_sql_query("SELECT a.attname, pg_catalog.format_type(a.atttypid, a.atttypmod)FROM pg_attribute a JOIN pg_class t on a.attrelid = t.oid JOIN pg_namespace s on t.relnamespace = s.oid WHERE a.attnum > 0 AND NOT a.attisdropped AND t.relname = '{}' AND s.nspname = 'public' ORDER BY a.attnum;".format(currentTable),con=connDB)
            
            dfCTypes = pd.DataFrame(columns=['type'])
            
            for i in range(len(typesAttributes)):
                if(typesAttributes.iloc[i,1] == 'ARRAY'):                                             dfCTypes.loc[len(dfCTypes)] = [5] ### get array type
                if(typesAttributes.iloc[i,1] == 'integer' or typesAttributes.iloc[i,1] == 'numeric'): dfCTypes.loc[len(dfCTypes)] = [4] ### get numeric type
                elif('character' in typesAttributes.iloc[i,1]):                                       dfCTypes.loc[len(dfCTypes)] = [3] ### get categorical type    
                elif(typesAttributes.iloc[i,1] == 'text' and 'id' not in typesAttributes.iloc[i,0]):  dfCTypes.loc[len(dfCTypes)] = [2] ### get texts type
                elif(typesAttributes.iloc[i,1] == 'date' or typesAttributes.iloc[i,1] == 'datetime'): dfCTypes.loc[len(dfCTypes)] = [1] ### get date type
                elif(typesAttributes.iloc[i,1] == 'text' and 'id' in typesAttributes.iloc[i,0]):      dfCTypes.loc[len(dfCTypes)] = [0] ### get ID type
                else: dfCTypes.loc[len(dfCTypes)] = [-1]
            
            usefulColumns = dfData[dfData.columns[dfCTypes['type'] > 1]].columns

            usefulCTypes = dfCTypes[dfCTypes['type'] > 1]
            usefulCTypes.reset_index(inplace = True, drop = True)
                        
            table = Table(w.TFrameDataMainPage,
                dataframe=dfData,
                showtoolbar=True,
                showstatusbar=True)

            table.show()
            table.redraw()
            for i in range(len(tablesList)):
                w.ScrolledlistboxDBTables.insert(i,tablesList[i])    

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
                    
    except:
         tk.messagebox.showinfo(title='Sketch',
                        message='Choose a table to load, please!')
  
    print('main_support.btnLoadSelectedTable')
    sys.stdout.flush()

def btnSaveDatabaseConfigFile():
    
    if(w.TEntryDBName.get() != '' and w.TEntryDBName.get() != '' and w.TEntryDBName.get() != ''): 

        nameDB = w.TEntryDBName.get()
        username = w.TEntryUsername.get()
        pwd = w.TEntryPassword.get()
        try:
            with open('dbFile.txt', 'w') as f:
                f.write('nameDB='+nameDB+'\n'+'usernameDB='+username+'\n'+'pwdDB='+pwd+'\n')
                f.close()
                tk.messagebox.showinfo(title='Sketch',
                            message='File with database information saved!', parent=top_level)
        except:
            tk.messagebox.showinfo(title='Sketch',
                            message='Problem on create file, check your info!', parent=top_level)

    else:
        tk.messagebox.showinfo(title='Sketch',
                            message='Verify the connection information, please!', parent=top_level)
   

    sys.stdout.flush()

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import main
    main.vp_start_gui()
