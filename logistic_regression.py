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
   
def data_cleaning(df):
    #unified units
    for col in df:
        if df[col].dtype!='object' and str(df[col].min())!='nan' and len(str(int(df[col].max())))-len(str(int(df[col].min())))>=3:
            for item in df[col]:
                if str(item)!='nan' and len(str(int(df[col].max())))-len(str(int(item)))>=3:
                    df.loc[df[col]==item,col]=item*10000
    #remove or fitting data
    for col in df:
        if df[col].isnull().sum()<=2 and df[col].dtype!='object':
            df[col]=df[col].fillna(df[col].mean())
    df=df.dropna(axis=1,how='any')
    return df


for province in provinces:
    df_dict[province]=data_cleaning(df_dict[province])