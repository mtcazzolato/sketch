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
# SKETCH - Query complete tuples
###################################################################

import sys
import numpy as np
import pandas as pd
import editdistance

from scipy.spatial import distance
from sklearn import preprocessing
from sklearn.metrics import jaccard_score

###################################################################
# Distances and handy functions
###################################################################

def p_root(value, root): # nth root of a value
    root_value = 1 / float(root)
    return round (float(value) **
                  float(root_value), 3)

def getNormalizedValues(values): # Normalize values
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(values)
    return x_scaled

# Sum distance of Equality comparisons of terms
def getWeightedEqualDistance(queryObj, db, w):

    distances = []
    for i in range(len(db)):
        partial_dist = 0
        
        for j, att in enumerate(db.columns):
            if (str(queryObj[att]) != str(db[att].iloc[i])):
                partial_dist += 1 * w[j]
#             else
#                 partial_dist += 0
        
        partial_dist *= 1/sum(w) if sum(w) > 0 else 0;
        distances.append(partial_dist)
    
    return pd.DataFrame(data=distances, columns=['WeightedEqualDist'])

# Minkowiski global distance of weighted difference comparisons of terms
def getWeightedMinkowiski(queryObj, db, p, w):

    distances_wmink = []
    
    for i in range(len(db)):
        partial_dist = 0
        
        for j, att in enumerate(db.columns):
            partial_dist += pow(abs(queryObj[att] - db[att].iloc[i]), p) * w[j]
        
        partial_dist *= 1/sum(w) if sum(w) > 0 else 0;
        distances_wmink.append(p_root(partial_dist, p))
    
    return pd.DataFrame(data=distances_wmink, columns=['WeightedDifferenceMink'])

# Minkowiski global distance of weighted LEdit comparisons of terms
def getWeightedLEdit(queryObj, db, p, w):

    distances_wledit = []
        
    for i in range(len(db)):
        partial_dist = 0
        
        for j, att in enumerate(db.columns):
            partial_dist += pow(abs(editdistance.distance(str(queryObj[att]), str(db[att].iloc[i]))), p) * w[j]
        
        partial_dist *= 1/sum(w) if sum(w) > 0 else 0;
        distances_wledit.append(p_root(partial_dist, p))
        
    return pd.DataFrame(data=distances_wledit, columns=['WeightedLEditMink'])

###################################################################
# Query complete tuples
###################################################################

def getTupleDistance(queryObject, db, ctypes, w, p=2, normalized=True):
    # type = 0 is ID, ignore the corresponding columns
    columns = db.columns

    # Compare by LEdit (textual attributes)
    distances = getWeightedLEdit(queryObject[columns[ctypes['type'] == 2]].loc[:],
                                 db[columns[ctypes['type'] == 2]].loc[:],
                                 2,
                                 w[ctypes['type'] == 2].values)
    
    # Compare by equality (categorical attributes)
    distances['WeightedEqualDist'] = getWeightedEqualDistance(queryObject[columns[ctypes['type'] == 3]],
                                                      db[columns[ctypes['type'] == 3]],
                                                      w[ctypes['type'] == 3].values)
    
    # Compare by difference (numerical attributes)
    distances['WeightedDifferenceMink'] = getWeightedMinkowiski(queryObject[columns[ctypes['type'] == 4]],
                                                                db[columns[ctypes['type'] == 4]],
                                                                2, w[ctypes['type'] == 4].values)
    
    if (normalized):
        distances['Norm-WeightedLEditMink'] = getNormalizedValues(distances[['WeightedLEditMink']].values)
        distances['Norm-WeightedEqualDist'] = getNormalizedValues(distances[['WeightedEqualDist']].values)
        distances['Norm-WeightedDifferenceMink'] = getNormalizedValues(distances[['WeightedDifferenceMink']].values)
        
        distances['TupleDist'] = distances[['WeightedLEditMink', 'WeightedEqualDist', 'WeightedDifferenceMink']].sum(axis=1)
        distances['NormTupleDist'] = distances[['Norm-WeightedLEditMink', 'Norm-WeightedEqualDist', 'Norm-WeightedDifferenceMink']].sum(axis = 1)
        distances['NormTupleDist'] = getNormalizedValues(distances[['NormTupleDist']].values)

    else:
        distances['TupleDist'] = distances[['WeightedLEditMink', 'WeightedEqualDist', 'WeightedDifferenceMink']].sum(axis=1)
    
    return distances




def runCompleteQueries(dfQueryObjects, dfData, ctypes, k, r, w, p=2, normalized=True):
    # -------------------------------
    # Input data and initial parameters
    # -------------------------------

    performKnnQuery = True if k > 0 else False
    performRangeQuery = True if r > 0 else False

    # columns = dfData.columns

    if (len(w) == 0):
        # Weight matrix (default)
        w = pd.Series([1] * len(dfData.columns))
    
    # -------------------------------
    # Perform query with complete tuples
    # -------------------------------

    listQ1 = []
    dfQueries = pd.DataFrame()
    ctypes.astype(int)
    
    if (performKnnQuery and performRangeQuery):
        for i in range(0, len(dfQueryObjects)):
            print(str(i) + ' / ' + str(len(dfQueryObjects)), end = '\r')

            distances = getTupleDistance(pd.Series(dfQueryObjects.loc[[i]]), dfData.loc[:], ctypes, w, p, True)

            # KNN and Range queries
            listQ1.append([distances.sort_values(by = ['NormTupleDist'], ascending = True).iloc[:k].index.values,
                           distances[distances['NormTupleDist'] <= r].sort_values(by = ['NormTupleDist'], ascending = True).index.values])

        # Concatenate result sets
        dfQueries = pd.DataFrame(data = listQ1, columns=['KNNCompleteQuery','RqCompleteQuery'])

    elif (performKnnQuery):
        for i in range(0, len(dfQueryObjects)):
            distances = getTupleDistance(dfQueryObjects.iloc[i], dfData.iloc[:], ctypes,w, p, True)
            
            # KNN
            listQ1.append([distances.sort_values(by = ['NormTupleDist'], ascending = True).iloc[:k].index.values])
        
        # Concatenate result sets
        dfQueries = pd.DataFrame(data = listQ1, columns=['KNNCompleteQuery'])

    else:
        for i in range(0, len(dfQueryObjects)):
            distances = getTupleDistance(dfQueryObjects.iloc[i], dfData.iloc[:], ctypes, w, p, True)
            
            # Range queries
            listQ1.append([distances[distances['NormTupleDist'] <= r].sort_values(by = ['NormTupleDist'], ascending = True).index.values])

        # Concatenate result sets
        dfQueries = pd.DataFrame(data = listQ1, columns=['RqCompleteQuery'])
    

    # Return dataframe with computed distances
    return dfQueries
