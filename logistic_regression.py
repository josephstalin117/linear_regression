import pandas as pd
import numpy as np
from numpy import nan as Nan
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
    #drop nan
    df=df.dropna(axis=1,how='any')
    #convert percent string to float
    for x in ['quality_3','quality_4','quality_5']:
        df[x]=df[x].str.rstrip('%').astype('float') / 100.0   
    return df

for province in provinces:
    df_dict[province]=data_cleaning(df_dict[province])

## Regional division

east={}
central={}
west={}
northeast={}

for x in provinces:
    if x in ["beijing","tianjin","hebei","shanghai","jiangsu","zhejiang","fujian","shandong","guangdong","hainan"]:
        east[x]=df_dict[x]
    elif x in ["shanxi","anhui","jiangxi","henan","hubei","hunan"]:
        central[x]=df_dict[x]
    elif x in ["neimenggu","guangxi","chongqing","sichuan","guizhou","yunnan","xizang","shaanxi","gansu","qinghai","ningxia","xinjiang"]:
        west[x]=df_dict[x]
    elif x in ["liaoning","jilin","heilongjiang"]:
        northeast[x]=df_dict[x]
    else:
        print("error")
        print(x)

#check lack col of some province
def check_lack_col(normal_df,lack_df):
    normal_list=[x for x in normal_df]
    lack_list=[x for x in lack_df]
    if len(normal_list)<len(lack_list):
        print('fuck you!')
    elif len(normal_list)<len(lack_list):
        print('equal length')
    else:
        i,j=0,0
        while(i<len(normal_list) and j<len(lack_list)):
            if normal_list[i]==lack_list[j]:
                i+=1
                j+=1
            else:
                print(normal_list[i])
                i+=1
        while(i<len(normal_list)):
            print(normal_list[i])


#check_lack_col(east['shandong'],east['shanghai'])

#drop xizhang data
west.pop('xizang',0)


def area_merge(area_dict,area_name='uname'):
    pd_size=-1
    pd_size_province=""
    for x in area_dict:
        if pd_size==-1 or len(area_dict[x].columns)<pd_size:
            pd_size=len(area_dict[x].columns)
            pd_size_province=x

    area_df=pd.DataFrame(columns=[x for x in area_dict[pd_size_province]])
    ## get sum
    i=0
    for year in years:
        for col in area_df.columns:
            if col=='province':
                area_df.loc[i]=pd.Series([np.nan if col=='province' or col=='year' else 0 for col in area_df.columns],index=[x for x in area_df.columns])
            elif col=='year':
                area_df.loc[i]['year']=year
            else:
                for province in area_dict:
                    area_df[col][i]+=area_dict[province][col][year-2006]
            if col==area_df.columns[-1]:
                i+=1
    area_df['province']=area_name
    return area_df

east_df=pd.DataFrame()
west_df=pd.DataFrame()
central_df=pd.DataFrame()
northeast_df=pd.DataFrame()

east_df=area_merge(east,'east')
west_df=area_merge(west,'west')
central_df=area_merge(central,'central')
northeast_df=area_merge(northeast,'northeast')






