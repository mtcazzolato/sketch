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

###################################################################
# R-SKETCH
###################################################################

import sys
import pandas as pd
import numpy as np
from ast import literal_eval
from mlxtend.frequent_patterns import apriori, fpmax, fpgrowth
from mlxtend.frequent_patterns import association_rules
import plotly.graph_objects as go
from colorutils import Color

###################################################################
# Parameters and Data Structure
###################################################################



###################################################################
# Input Data
###################################################################

def readInputData(dataFilePath, transactionFilePath, aruleFilePath):
    dfQView = pd.read_csv(dataFilePath, encoding ='utf-8')
    transactions = pd.read_csv(transactionFilePath, sep = ';')
    arules = pd.read_csv(aruleFilePath, sep = ';')

    # Consider columns as lists
    arules[['antecedents', 'consequents']] = arules[['antecedents', 'consequents']].applymap(literal_eval)

    return dfQView, transactions, arules

###################################################################
# Query over the input data, using the generated rules
###################################################################

def query(data, transactions, arules, qstring):
    # Filter transactions containing query string
    filteredTuples = transactions[transactions[qstring] == True]

    # Initialize scores as zero
    tscores = [0]  * len(transactions)

    occ = []
    for rule in arules['antecedents']:
        occ.append(qstring in rule)
    
    # Filter rules with the query string in the antecedent
    filteredAr = arules[occ]

    # For every rule containing the query string in the antecedent, add the score (lift) to the consequent
    for idx in filteredAr.index:
        # Sum score
        lift = filteredAr['lift'].loc[idx] - 1
        
        for item in filteredAr['consequents'].loc[idx]:
            f = filteredTuples[filteredTuples[item] == True]
            
            for line in f.index:
                tscores[line] += lift

    return tscores, filteredAr

###################################################################
# Plot Sankey Diagram
###################################################################
def getVisualization(selectedRules, outputImagePath):
    # Get items in the antecedents
    item = []
    for r in selectedRules['antecedents']:
        for i in r:
            item.append(i)

    # Get items in the consequents
    for r in selectedRules['consequents']:
        for i in r:
            item.append(i)

    # Construct dict with unique values and corresponding idexes
    itemdict = {}

    for index, uitem in enumerate(np.unique(item)):
        itemdict[uitem] = index

    label = list(itemdict.keys())
    source = []
    target = []
    value = []

    for i, rule in enumerate(selectedRules['antecedents']):
        for item in rule:
            consequents = selectedRules['consequents'].iloc[i]
            
            for c in consequents:
                source.append(itemdict[item])
                target.append(itemdict[c])
                value.append(selectedRules['lift'].iloc[i])

    # data to dict, dict to sankey
    link = dict(source = source, target = target, value = value)
    node = dict(label = label, pad=50, thickness=15)
    data = go.Sankey(link = link, node=node)
    # plot
    fig = go.Figure(data)
    #fig.savefig(outputImagePath, dpi=300)
    fig.write_image(outputImagePath)


###################################################################
# Main
###################################################################

def main(argv):
    datapath            = str(argv[1])
    transactionspath    = str(argv[2])
    arulespath          = str(argv[3])
    qcolumn             = str(argv[4])
    qvalue              = str(argv[5])
    outputpath          = str(argv[6])

    dfData, transactions, arules = readInputData(datapath, transactionspath, arulespath)
    qstring = qcolumn + '.' + qvalue

    # Rank tuples according to their scores:
    dfData['Score'], filteredAR = query(dfData, transactions, arules, qstring)
    dfData.sort_values('Score', ascending = False).to_csv(outputpath, sep = ';', index = False)
    
    if (len(filteredAR) > 100):
        filteredAR = filteredAR.loc[:100]
    
    getVisualization(filteredAR, outputpath[:-3] + 'png')
    
if __name__ == "__main__":
    if (len(sys.argv) != 7):
        print("Wrong number of input parameters.")
        print('Usage: <datapath> <transactionspath> <arulespath> <qcolumn> <qvalue> <outputpath>')

    else:
        print('Running the AR-Lift ranking algorithm...')
        main(sys.argv)
        print('Done.')

