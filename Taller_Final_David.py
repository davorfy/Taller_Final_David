# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 09:49:42 2021

@author: Lenovo
"""

import pandas as pd

url = 'covid_22_noviembre.csv'
data = pd.read_csv(url)

#Ejercicio 1

num_casos = len(data)
print (num_casos)

#Ejercicio 2 

data['Nombre municipio'].replace('puerto colombia','PUERTO COLOMBIA', inplace=True)
data['Nombre municipio'].replace('puerto COLOMBIA','PUERTO COLOMBIA', inplace=True)
data['Nombre municipio'].replace('MEDELLiN','MEDELLIN', inplace=True)
data['Nombre municipio'].replace('Galapa','GALAPA', inplace=True)
data['Nombre municipio'].replace('momil','MOMIL', inplace=True)
data['Nombre municipio'].replace('Guepsa','GUEPSA', inplace=True)
data['Nombre municipio'].replace('barrancabermeja','BARRANCABERMEJA', inplace=True)
data['Nombre municipio'].replace('Pensilvania','PENSILVANIA', inplace=True)
data['Nombre municipio'].replace('Anserma','ANSERMA', inplace=True)

num_municipios = len(data.groupby('Nombre municipio').size())
print (num_municipios)

#Ejercicio 3

data.groupby('Nombre municipio').size().sort_values

#Ejercicio 4

data['Ubicación del caso'].replace('casa','Casa', inplace=True)
data['Ubicación del caso'].replace('CASA','Casa', inplace=True)

num_casa = len(data[data['Ubicación del caso'] == 'Casa'])
print(num_casa)
