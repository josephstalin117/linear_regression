# -*- coding: utf-8 -*-
"""
Created on Fri May 11 08:53:25 2018

@author: Icy
"""

import json
import csv
import pandas as pd
#with open('waterdata.txt', 'r') as f:
#    listj=[]
#    json_data = json.load(f.replace("'", "\""))
#    for line in json_data:
#        print(line)
#        listj.append(line)
#result=[]  
#fd = file( "waterdata.txt", "r" )  
  
#with open('ccc.csv','a') as fl:
#        wr = csv.DictWriter(fl,fieldnames=['dateTime', 'siteName','pH', 'CODMn', 'DO', 'NH4', 'TOC', 'status','attribute',  'level'])
#        for l in datalist:
#            # newlist=[]
#            # for key,value in l.items():
#            #     print(value)
#            #     newlist.append(value)
#            wr.writerow(l)

#import pickle
#import json
#f = open('waterdata.txt', 'rb')
#for line in f.readlines():
#    json_data = json.loads(line)
#d = pickle.load(f)
#f.close()
#print(d)
#print(json_data)

with open('waterdata.txt', encoding='utf-8') as f: 
    datalist=[]       
    for r in f.readlines():
        data=json.loads(json.dumps(r))
        s=r.split('}')[:-1]
        for i in s:
            i=i+'}'
            json_i=json.dumps(i,ensure_ascii=False)
            data_dict=json.loads(json_i)
            
            
#with open('ccc.csv','a') as fl:
#        wr = csv.DictWriter(fl,fieldnames=['dateTime', 'siteName','pH', 'CODMn', 'DO', 'NH4', 'TOC', 'status','attribute',  'level'])
#        for l in datalist:
#            wr.writerow(l)
