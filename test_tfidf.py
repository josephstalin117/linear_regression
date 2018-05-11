# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 10:50:44 2018

@author: joseph
"""

from sklearn.feature_extraction.text import TfidfTransformer
transformer = TfidfTransformer(smooth_idf=False)

counts=[[3,0,1],[2,0,0],[3,0,0],[4,0,0],[3,2,0],[3,0,2]]
tfidf=transformer.fit_transform(counts)