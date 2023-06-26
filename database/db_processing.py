#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   db_processing.py
@Time    :   2023/06/26 19:46:33
@Author  :   Bart Ortiz 
@Version :   1.0
@Contact :   bortiz@ugr.es
@License :   CC-BY-SA or GPL3
@Desc    :   None
'''



# read animales.csv and create a new csv file with the data that match classes of Clase ARACHNIDA  INSECTA MALACOSTRACA

import pandas as pd


df = pd.read_excel('animales.xlsx')

# get only the rows that match the classes of Clase ARACHNIDA  INSECTA MALACOSTRACA
df = df[df['Clase'].isin(['Arachnida', 'Insecta', 'Malacostraca'])]
# get the one with Descripción not null
df = df[df['Descripción'].notnull()]
# save the new csv file
df.to_excel('animales_filtered.xlsx', index=False)