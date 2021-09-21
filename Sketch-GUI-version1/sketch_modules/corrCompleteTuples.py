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
# SKETCH
###################################################################

import numpy as np
import pandas as pd
import editdistance
import matplotlib.pyplot as plt
import seaborn as sns

from ast import literal_eval
from scipy.spatial import distance
from sklearn.metrics import jaccard_score
from sklearn import preprocessing

###################################################################
# Compute distances of tuples (per attribute)
###################################################################

def p_root(value, root): # nth root of a value
    root_value = 1 / float(root)
    return round (float(value) **
                  float(root_value), 3)

def getDistTimeSeries(dfData, distFunctionId):
    distances = []
    p = 2 # Mink.Euclidean
    n = len(dfData)
    
    if (distFunctionId == 2):
        # Text with LEdit
        for i in range(len(dfData)):
            meanDist = 0
            for j in range(len(dfData)):
                meanDist += float(editdistance.distance(str(dfData.iloc[i]), str(dfData.iloc[j])))
                
            distances.append(float(meanDist / n))
            
    elif (distFunctionId == 3):
        # Text by equality
        for i in range(len(dfData)):
            meanDist = 0
            for j in range(len(dfData)):
                if (str(dfData.iloc[i]) != str(dfData.iloc[j])):
                    meanDist += 1
            
            distances.append(float(meanDist / n))
    
    elif (distFunctionId == 4):
        # Difference is the distance (numeric)
        for i in range(len(dfData)):
            meanDist = 0
            for j in range(len(dfData)):
                meanDist += p_root(pow(abs(float(dfData.iloc[i]) - float(dfData.iloc[j])), p), p)
            
            distances.append(float(meanDist / n))

    elif (distFunctionId == 5):
        # Difference is the distance (numeric)
        for i in range(len(dfData)):
            meanDist = 0
            for j in range(len(dfData)):
                if (str(dfData.iloc[i]) != 'nan' and str(dfData.iloc[j]) != 'nan'):
                    # meanDist += p_root(pow(abs(float(dfData.iloc[i]) - float(dfData.iloc[j])), p), p)
                    meanDist += distance.minkowski(literal_eval(dfData.iloc[i]), literal_eval(dfData.iloc[j]), p)
                else:
                    meanDist += 100
            
            distances.append(float(meanDist / n))

    return distances


###################################################################
# Main
###################################################################

def runCorrelation(dfData, dfTypes, corrMethod='Pearson'):

    print('Running correlation among attributes...')

    distances = pd.DataFrame(columns=[])
    print(dfData.columns)

    print(len(dfData.columns), len(dfTypes))
    
    for i, att in enumerate(dfData.columns):
        print(att, dfTypes['type'].iloc[i])

        if (dfTypes['type'].iloc[i] > 1 and dfTypes['type'].iloc[i] < 6): # Ignore IDs
            distances[att] = getDistTimeSeries(dfData[att], dfTypes['type'].iloc[i])

    # Return correlations
    return distances.corr()
