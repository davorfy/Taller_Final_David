# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 09:49:42 2021

@author: Lenovo
"""

import pandas as pd

url = 'covid_22_noviembre.csv'
data = pd.read_csv(url )

#Ejercicio 1

num_casos = len(data)
print (num_casos)