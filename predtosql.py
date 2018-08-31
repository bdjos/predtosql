# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 09:28:26 2018

@author: BJoseph
"""

import pandasdb
import accuweathertest
import predict
import os
from sqlalchemy import Column, Integer, String, Float, Datetime

db_name = 'bjos'
table_name = 'forecast'

df = predict.predict()
print(df.columns)
df_dtypes = [Column(Datetime, primary_key=True), 
             Column(Integer),
             Column(Integer), 
             Column(Integer), 
             Column(Integer), 
             Column(Integer), 
             Column(Integer), 
             Column(Integer), 
             Column(Float)]

db = pandasdb.pandasdb(db_name, table_name)
db.pd_to_db(df_dtypes, df, if_exists='replace')

