# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 12:03:08 2024

@author: User
"""

import pandas as pd
file=pd.read_csv('META.csv')
print('This comand will indentify all missing values of the data:')
print(file.isnull().to_string())
print('To find the number of missing values you can use:')
print(file.isnull().sum())
print('There is a lot of versions to encode missing data values')
print('code to delate all missing data')
delating=file.dropna()
print(delating)

print(file.head(6))
print(file.tail(4))
print(file.duplicated())
print(file.drop_duplicates())
print(file.fillna(98899))

x = file["Close"].mean()
replace=file["Close"].fillna(x)
print(replace)

y = file["Low"].mode()[0]
mode=file["Low"].fillna(x)
print(mode)

z = file["Volume"].median()
median=file["Volume"].fillna(x)
print(median)


    