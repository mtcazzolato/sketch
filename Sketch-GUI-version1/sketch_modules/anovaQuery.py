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
# R-SKETCH - ANOVA correlation value
###################################################################

import sys
import numpy as np
import pandas as pd
from scipy import stats


def safe_float_convert(x):
    try:
        float(x)
        return True # numeric, success!
    except ValueError:
        return False # not numeric
    except TypeError:
        return False # null typedfSample


def treatNumericVariable(dfData, numericAttribute):
    try:
        dfWork = dfData.copy()
        dfWork[str(numericAttribute)].replace({',': '.'}, inplace=True, regex=True)
        dfWork[str(numericAttribute)].replace({':': '.'}, inplace=True, regex=True)
        mask = dfWork[str(numericAttribute)].map(safe_float_convert)
        
        dfWork = dfWork.loc[mask]

        dfWork[str(numericAttribute)] = pd.to_numeric(dfWork[str(numericAttribute)], downcast='float')
        dfWork[str(numericAttribute)].fillna(dfWork[str(numericAttribute)].mean(), inplace = True)
        
        return dfWork
    
    except:
        print('Error treating numerical variable')
        dfData[str(numericAttribute)].fillna(dfData[str(numericAttribute)].mean(), inplace = True)
        return dfData
    
def treatCategorivalVariable(dfData, categoricalAttribute):
    try:
        dfWork = dfData.copy()
        dfWork[str(categoricalAttribute)].fillna('Not Informed', inplace = True)
        
        return dfWork
    except:
        print('Error treating categorical variable')
        return dfData

###################################################################
# Run ANOVA pairwise (pairs of categorical values) in relation with
# the numerical attribute
###################################################################

def getANOVAResults(attCategorical, attNumerical, dfData):
    
    dfData = treatNumericVariable(dfData, attNumerical)
    dfData = treatCategorivalVariable(dfData, attCategorical)
    
    grouping = dfData[[str(attCategorical), str(attNumerical)]].groupby(str(attCategorical))

    dfAnovaCorrelation = pd.DataFrame(columns = ['Category 1', 'Category 2', 'F-value', 'p-value'])
    categoricalValues = dfData[str(attCategorical)].unique()

    # Get the F-value and p-value for each combination of categorical values in relation with the numerical attribute
    for v1 in categoricalValues:
        for v2 in categoricalValues:
            # print('Testing <' + str(v1) + ', ' + str(v2) + '>')
            fval, pval = stats.f_oneway(grouping.get_group(v1)[attNumerical], grouping.get_group(v2)[attNumerical])
            dfAnovaCorrelation.loc[len(dfAnovaCorrelation)] = [v1, v2, fval, pval]

    # Get the F-value and p-value for all categories in relation with the numerical attribute
    # print('Testing <All, All>')
    fval, pval = stats.f_oneway(*[list(grouping.get_group(v)[attNumerical]) for v in set(categoricalValues)])
    dfAnovaCorrelation.loc[len(dfAnovaCorrelation)] = ['All', 'All', fval, pval]

    dfAnovaCorrelation.sort_values(['F-value'], ascending = False, inplace = True)
    dfAnovaCorrelation.reset_index(inplace=True, drop=True)

    return (dfAnovaCorrelation)
