# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 13:16:39 2017

@author: Noureddin Sadawi
"""

import pandas as pd
import sys

assert (len(sys.argv) == 3),'Please pass two parameters!'+'\n'+'Example usage: python npc2batman.py /path/to/input.csv /another/path/to/out.txt'


#input and out put files as command line parameters
#example run: python npc2batman /path/to/input.csv /another/path/to/out.txt 
input_file = sys.argv[1]
outut_file = sys.argv[2]

#read the input csv
data = pd.read_csv(input_file)
#get number of columns
ncol = len(data.columns)
#get index of column '0'
i = data.columns.get_loc('0')
#get a slice of the DF .. from column '0' to last column
data = data.ix[:,i:ncol]

#reverse column order
data = data.ix[::,::-1]
# transpose dtaframe
data = data.transpose()
#rename column 0 to 'ppm'
data.rename(columns={0: 'ppm'}, inplace=True)
#save to output file (notice extension is txt)
data.to_csv(outut_file, sep='\t',index=False)