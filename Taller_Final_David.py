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

#Ejercicio 5

data['Recuperado'].replace('fallecido','Fallecido', inplace=True)
data[data['Recuperado'] == 'Recuperado'].shape[0]

#Ejercicio 6

data[data.Estado == 'Fallecido' ].shape[0]

#Ejercicio 7

data.groupby('Tipo de contagio').size().sort_values(ascending=False)

#Ejercicio 8

data['Nombre departamento'].replace('Tolima','TOLIMA', inplace=True)
data['Nombre departamento'].replace('Caldas','CALDAS', inplace=True)
num_dpto = len(data.groupby('Nombre departamento').size())
print (num_dpto)

#Ejercicio 9

data.groupby('Nombre departamento').size().sort_values

#Ejercicio 10

data['Ubicación del caso'].replace('CASA','Casa', inplace=True)
data['Ubicación del caso'].replace('casa','Casa', inplace=True)
data.groupby('Ubicación del caso').size().sort_values(ascending=False)

#Ejercicio 11

data.groupby('Nombre departamento').size().sort_values(ascending=False).head(10)

#Ejercicio 12

data[(data.Estado == 'Fallecido')].groupby('Nombre departamento').size().sort_values(ascending=False).head(10)

#Ejercicio 13

data[(data.Recuperado == 'Recuperado')].groupby('Nombre departamento').size().sort_values(ascending=False).head(10)

#Ejercicio 14

data.groupby('Nombre municipio').size().sort_values(ascending=False).head(10)

#Ejercicio 15

data[(data.Estado == 'Fallecido')].groupby('Nombre municipio').size().sort_values(ascending=False).head(10)

#Ejercicio 16

data[(data.Recuperado == 'Recuperado')].groupby('Nombre municipio').size().sort_values(ascending=False).head(10)

#Ejercicio 17

data.groupby(['Nombre departamento','Nombre municipio']).size().sort_values(ascending=False)

#Ejercicio 18

data.groupby(['Sexo','Nombre municipio','Nombre departamento']).size()

#Ejercicio 19

data.groupby(['Sexo','Nombre municipio','Nombre departamento']).Edad.mean()

#Ejercicio 20

data.groupby('Nombre del país').size().sort_values(ascending=False)

#Ejercicio 21

data.groupby('Fecha de diagnóstico').size().sort_values(ascending=False)

#Ejercicio 22

tasa_mortalidad = (len(data[data.Estado == 'Fallecido'])/len(data))*100
tasa_recup = (len(data[data.Recuperado == 'Recuperado']) / len(data))*100

print("la tasa de mortalidad es de un", + tasa_mortalidad,"%")
print("la tasa de recuperación es de un", + tasa_recup,"%")

#Ejercicio 23

tasa_mortalidad = (len(data[data.Estado == 'Fallecido'])/len(data))*100
tasa_recup = (len(data[data.Recuperado == 'Recuperado']) / len(data))*100
data.groupby([int(tasa_mortalidad), int(tasa_recup),'Nombre departamento']).size()

#Ejercicio 24

tasa_mortalidad = (len(data[data.Estado == 'Fallecido'])/len(data))*100
tasa_recup = (len(data[data.Recuperado == 'Recuperado']) / len(data))*100
data.groupby([int(tasa_mortalidad), int(tasa_recup),'Nombre municipio']).size()

#Ejercicio 25

data.groupby(['Nombre municipio','Ubicación del caso']).size()

#Ejercicio 26

data.groupby(['Sexo','Nombre municipio']).Edad.mean()

#Ejercicio 27

data.groupby(['Recuperado']).size().cumsum().plot()

#Ejercicio 32

data['Ubicación del caso'].value_counts().plot.bar()

#Ejercicio 33

data.Sexo.value_counts().plot.bar()

#Ejercicio 34

data['Tipo de contagio'].value_counts().plot.bar()

#Ejercicio 35

data['fecha reporte web'] = pd.to_datetime(data['fecha reporte web'])
data.groupby[('Recuperado','Fecha reporte web')].size().plot.bar()
