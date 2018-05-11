# -*- coding:utf8 -*-
import csv
import codecs
import json

with open('waterdata_5_5.txt', encoding='utf-8') as f:      
    for r in f.readlines():
        data=json.loads(json.dumps(r))
        s=r.split('}')[:-1]
        for i in s:
            i=i+'}'
            i=i.replace("'", '"')
            #json_i=json.dumps(i,ensure_ascii=False)
            data_dict=json.loads(i)