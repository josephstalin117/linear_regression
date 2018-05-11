# -*- coding:utf8 -*-

import json
import pandas as pd

sourcefile="waterdata_5_5.txt"
csvfilename="waterdata_5_5.csv"
df = pd.DataFrame(columns=['dateTime','CODMn', 'DO', 'NH4', 'TOC', 'attribute','level','pH','siteName','status'])

with open(sourcefile, encoding='utf-8') as f:      
    for r in f.readlines():
        s=r.split('}')[:-1]
        for i in s:
            i=i+'}'
            i=i.replace("'", '"')
            data_dict=json.loads(i)
            df=df.append(data_dict,ignore_index=True)