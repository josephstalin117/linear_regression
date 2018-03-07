import pandas as pd
import numpy as np
from pandas import Series,DataFrame

years=[2006,2007,2008,2009,2010,2011,2012,2013,2014,2015]

df_list=[pd.read_csv('csv/'+str(x)+'.csv', header=0) for x in years]

provinces=df_list[1]['province']
df_dict={}

for province in provinces:
    df_dict[province]=[x[x['province']==province] for x in df_list]

for province in provinces:
    df_dict[province]=pd.concat(df_dict[province])
    df_dict[province].reset_index(inplace=True,drop=True)