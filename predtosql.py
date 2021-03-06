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
table_name = 'forecast2'

df = predict.predict()
df.columns = ['Rel Hum' if x == 'Rel Hum (%)' else x for x in df.columns]

print(f'the dataframe is: {df}')
print(f'column names are: {df.columns}')
df_dtypes = [DateTime(), 
             Float(),
             Float(), 
             Integer(), 
             Integer(), 
             Integer(), 
             Integer(), 
             Integer(),
             Integer(),
             Float()]

db = pandasdb.pandasdb(db_name, table_name)
db.pd_to_db(df_dtypes, df, if_exists='replace')

