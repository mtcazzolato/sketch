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
# Sketch
###################################################################

import sys
import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, fpmax, fpgrowth
from mlxtend.frequent_patterns import association_rules
from ast import literal_eval
from colorutils import Color

###################################################################
# Parameters and Data Structure
###################################################################


###################################################################
# Define Apriori class
###################################################################

class Apriori:
    """Apriori Class. Its has Apriori steps."""
    threshold = 0.5
    df = None
    
    def __init__(self, df, threshold=None, transform_bol=False):
        """Apriori Constructor. 

        :param pandas.DataFrame df: transactions dataset (True or False).
        :param float threshold: set threshold for min_support.
        :return: Apriori instance.
        :rtype: Apriori
        """

        self._validate_df(df)

        self.df = df
        if threshold is not None:
            self.threshold = threshold

        if transform_bol:
            self._transform_bol()
    
    def _validate_df(self, df=None):
        """Validade if df exists. 

        :param pandas.DataFrame df: transactions dataset (1 or 0).
        :return: 
        :rtype: void
        """

        if df is None:
            raise Exception("df must be a valid pandas.DataDrame.")
    
    def _transform_bol(self):
        """Transform (1 or 0) dataset to (True or False). 

        :return: 
        :rtype: void
        """

        for column in self.df.columns:
            self.df[column] = self.df[column].apply(lambda x: True if x == 1 else False)
    
    def _apriori(self, use_colnames=False, max_len=None, count=True):
        """Call apriori mlxtend.frequent_patterns function. 

        :param bool use_colnames: Flag to use columns name in final DataFrame.
        :param int max_len: Maximum length of itemsets generated.
        :param bool count: Flag to count length of the itemsets.
        :return: apriori DataFrame.
        :rtype: pandas.DataFrame
        """
    
        apriori_df = apriori(
                    self.df, 
                    min_support=self.threshold,
                    use_colnames=use_colnames, 
                    max_len=max_len
                )
        if count:
            apriori_df['length'] = apriori_df['itemsets'].apply(lambda x: len(x))

        return apriori_df
    
    def run(self, use_colnames=False, max_len=None, count=True):
        """Apriori Runner Function.

        :param bool use_colnames: Flag to use columns name in final DataFrame.
        :param int max_len: Maximum length of itemsets generated.
        :param bool count: Flag to count length of the itemsets.
        :return: apriori DataFrame.
        :rtype: pandas.DataFrame
        """

        return self._apriori(
                        use_colnames=use_colnames,
                        max_len=max_len,
                        count=count
                    )

    def filter(self, apriori_df, length, threshold):
        """Filter Apriori DataFrame by length and  threshold.

        :param pandas.DataFrame apriori_df: Apriori DataFrame.
        :param int length: Length of itemsets required.
        :param float threshold: Minimum threshold nrequired.
        :return: apriori filtered DataFrame.
        :rtype:pandas.DataFrame
        """
        
        if 'length' not in apriori_df.columns:
            raise Exception("apriori_df has no length. Please run the Apriori with count=True.")

        return apriori_df[ (apriori_df['length'] == length) & (apriori_df['support'] >= threshold) ]

###################################################################
# Column to transactions
###################################################################

def getTransactionData(df, column):
    # Get unique values
    uvalues = df[column].unique()
    # Get column names by concatenating column name with value
    uvalues_colName = [str(column) + '.' + str(val) for val in uvalues]
    print('Unique values:', uvalues)
    # Transaction dataframe, with every value as a column/attribute
    dfTransaction = pd.DataFrame(columns = uvalues)

    # For every row of the dataframe
    for i in range(len(df)):
        # Initialize transaction with all values as False
        init = [False] * len(uvalues)
        
        # For every possible value
        for j, v in enumerate(uvalues):
            # Set as True the column corresponding to the item present in the tuple
            if (df[column].iloc[i] == v):
                init[j] = True
        
        # Add transaction to the resulting dataframe
        dfTransaction.loc[len(dfTransaction)] = init
    
    dfTransaction.columns = uvalues_colName
    return dfTransaction

def generateTransactions(data, usefulColumns):
    transactions = pd.DataFrame()

    for c in usefulColumns:
        df = getTransactionData(data, c)
        transactions = pd.concat([transactions, df], axis=1)

    return transactions

###################################################################
# Genertate the Association Rules
# generate / select
###################################################################

def frozensetToList(df): # For both 'antecedents' and 'consequents' columns
    antecedents = []
    consequents = []

    for ant in (df['antecedents']):
        antecedents.append(list(ant))

    for ant in (df['consequents']):
        consequents.append(list(ant))

    return antecedents, consequents

def runApriori(transactions, minSup, minConf):
    # Instantiate Apriori
    apriori_runner = Apriori(transactions, threshold=minSup, transform_bol=True)
    # Generate frequent itemsets
    frequent_itemsets = apriori_runner.run(use_colnames=True)
    # Generate association rules
    ar = association_rules(frequent_itemsets, metric="confidence", min_threshold=minConf)
   
    # Split antecedent and consequent to save it separately (because of error with att type (frozenset))
    antecedents, consequents = frozensetToList(ar)
    dfFinal = pd.DataFrame()
    dfFinal['antecedents'] = antecedents
    dfFinal['consequents'] = consequents

    dfFinal[['antecedent support', 'consequent support', 'support', 'confidence', 'lift', 'leverage', 'conviction']] = ar[['antecedent support', 'consequent support', 'support', 'confidence', 'lift', 'leverage', 'conviction']]

    # Return association rules
    return dfFinal

###################################################################
# Input Data
###################################################################

def readInputData(filepath):
    dfData = pd.read_csv(filepath, encoding ='utf-8')
    return dfData

##############################################################################################################
# Main
##############################################################################################################

def runARL(dfData, usefulColumns, minSup, minConf):
    # usefulColumns = ['ic_sexo', 'cd_uf', 'cd_municipio', 'de_origem',
                #'de_exame', 'de_analito', 'cd_unidade', 'de_valor_referencia',
                #'de_tipo_atendimento', 'de_clinica', 'de_desfecho']
    # dfData = readInputData(filepath)

    transactions = generateTransactions(dfData, usefulColumns)
    dfARules = runApriori(transactions, minSup, minConf)

    # Save Output Files
    # transactions.to_csv(outtransactionpath, sep = ';', index = False)
    # dfARules.to_csv(outarpath, sep=';', index = False)

    return transactions, dfARules


def getSankeyParameters(selectedRules):
    # ================================================================
    # Collect diagram data
    # ================================================================

    #selectedRules = arules.copy()
    print('Number of rules:', len(selectedRules))

    # # Filter if the diagram is too big to visualize
    # if (len(selectedRules) > 100):
    #     selectedRules = selectedRules.loc[:100]

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
    linkc = []

    for i, rule in enumerate(selectedRules['antecedents']):
        for item in rule:
            consequents = selectedRules['consequents'].iloc[i]
            
            for c in consequents:
                if (selectedRules['lift'].iloc[i] != 1):
                    source.append(itemdict[item])
                    target.append(itemdict[c])
                    value.append(selectedRules['confidence'].iloc[i])
                    linkc.append(itemdict[item])


    # Generate colors
    colorvalues = ['#808B96', '#00CC66', '#EC7063', '#F7DC6F', '#48C9B0', '#2685E3', '#D60A33', '#75B09C',
                '#808B96', '#00CC66', '#EC7063', '#F7DC6F', '#48C9B0', '#2685E3', '#D60A33', '#75B09C',
                '#808B96', '#00CC66', '#EC7063', '#F7DC6F', '#48C9B0', '#2685E3', '#D60A33', '#75B09C',
                '#808B96', '#00CC66', '#EC7063', '#F7DC6F', '#48C9B0', '#2685E3', '#D60A33', '#75B09C']

    linkcolorvalues = []
    for c in colorvalues:
        # Generate link colors
        originalColor = Color(hex=c)
        h, s, v = originalColor.hsv
        s = s * 100 - 60
        if (s < 10):
            s = 20
        v = v * 100
        hsvValue = 'hsv(' + str(int(h)) + ',' + str(int(s)) + '%,' + str(int(v)) + '%)'

        linkcolorvalues.append(hsvValue)

    linkColors = []

    for i in range(len(linkc)):
        linkColors.append(linkcolorvalues[source[i]])
    
    return label, colorvalues, source, target, value, linkColors
