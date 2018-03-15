import pandas as pd
import numpy as np
from pandas import Series,DataFrame

## data polymerization

years=[2006,2007,2008,2009,2010,2011,2012,2013,2014,2015]

# read csv
df_list=[pd.read_csv('csv/'+str(x)+'.csv', header=0) for x in years]

provinces=df_list[1]['province']
df_dict={}

#get province names from 2006.csv
for province in provinces:
    df_dict[province]=[x[x['province']==province] for x in df_list]

#merge same province data
for province in provinces:
    df_dict[province]=pd.concat(df_dict[province])
    df_dict[province].reset_index(inplace=True,drop=True)

##data cleaning

#test_df just use to test
    
#test_df=df_dict['beijing'].dropna(axis=1,how='any')
test_df=df_dict['beijing']

#print(test_df['province'].dtype)
#print(test_df['province'].dtype=='object')

#unified unit
for column in test_df:
    if test_df[column].dtype!='object' and len(str(int(test_df[column].max())))-len(str(int(test_df[column].min())))>=3:
        for item in test_df[column]:
            if str(item)!='nan' and len(str(int(test_df[column].max())))-len(str(int(item)))>=3:
                #print(test_df[column][item])
                #print(item)
                test_df.loc[test_df[column] == item, column] = item*10000

#remove or fitting data
for column in test_df:
    #print(test_df[column].isnull().sum())
    if test_df[column].isnull().sum()<2 and test_df[column].dtype!='object':
        test_df[column]=test_df[column].fillna(test_df[column].mean())

test_df=test_df.dropna(axis=1,how='any')
   
#jianchi!
for province in provinces:
    for column in dict[province]:
        if dict[province][column].dtype!='object' and len(str(int(dict[province][column].max())))-len(str(int(dict[province][column].min())))>=3:
            for item in

            
#df_dict[province]=df_dict[province].dropna(axis=1,thresh=3)
    
    
