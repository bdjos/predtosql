# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 09:28:26 2018

@author: BJoseph
"""

import pandasdb
import accuweathertest
import predict
import os
from sqlalchemy import Column, Integer, String, Float, DateTime

db_name = 'bjos'
table_name = 'forecast'

df = predict.predict()
print(f'the dataframe is: {df}')
df_dtypes = [DateTime(), 
             Integer(),
             Integer(), 
             Integer(), 
             Integer(), 
             Integer(), 
             Integer(), 
             Integer(),
             Integer(),
             Float()]

db = pandasdb.pandasdb(db_name, table_name)
db.pd_to_db(df_dtypes, df, if_exists='replace')

