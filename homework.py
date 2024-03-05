# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:33:40 2024

@author: User
"""
import pandas as pd 

file = pd.read_csv('data (2).csv',)
'''
1. Handling Missing Data Questions:

How do you identify and handle missing values in a Pandas DataFrame?
What is imputation, and why might it be useful in dealing with missing data?
'''
print('This comand will indentify all missing values of the data:')
print(file.isnull().to_string())
print('To find the number of missing values you can use:')
print(file.isnull().sum())
print('There is a lot of versions to encode missing data values')
print('code to delate all missing data')
delating=file.dropna()
print(delating)

print(file.head())

file.loc[5, 'Date'] = '02/03/23' #this will be replaced by location, also used in wrong data

changing=file.fillna(130)
print('to change the number to other spesific number', changing)

x = file["Calories"].mean()
replace=file["Calories"].fillna(x)
print('This file will replace missing data to avarege number', replace)

y = file["Duration"].mode()[0]
mode=file["Duration"].fillna(x)
print('This code will replace missing data to most usen number', mode)

z = file["Maxpulse"].median()
median=file["Maxpulse"].fillna(x)
print('This code will replace missing data to most used number', median)
print('Why is it useful?  You can just correct your code without doing it again, also in big data you may not notice missing values and the code will help you')
'''
2. Data Transformation Questions:

How can you encode categorical variables in a Pandas DataFrame?
What is one-hot encoding, and when would you use it in data preprocessing?
'''
print('To change certain data information you can usee location function ')
file.loc[6, 'Pulse']=100 
print(file.head(6))
print('Also you can use it to correct certain wrong data')
for x in file.index:
  if file.loc[x, "Maxpulse"] > 136:
    file.loc[x, "Maxpulse"] = 120
    print(file)
print('Also you can just delete all that rows with wrong data')
for x in file.index:
  if file.loc[x, "Duration"] > 120:
    file.drop(x, inplace=True)
print(file)


print('One-hot encoding is like bool the data. If you giving id to students you may use is by checking uniqueness ')
file_encoded = pd.get_dummies(file, columns=['Date', ])
print(file_encoded)
'''
3. Removing Duplicates Questions:

How do you identify and remove duplicate rows from a DataFrame?
Can you explain the difference between the duplicated() and drop_duplicates() methods in Pandas?
'''
print('This code finds out all duplicated rows')
print(file.duplicated())

print('You can delete all duplicated files', file.drop_duplicates()) 
print('duplicated() will give information about data, shows is it duplicated or not. drop_duplicates() will delete all duplicated files')
'''
4. Data Scaling and Normalization Questions:

Discuss the importance of feature scaling in machine learning.
Explain the difference between min-max scaling and z-score normalization.
'''
print('Feature scaling is making things balanced. Sometimes the data units may be uncomparable, so future scaling make them simular.')
print('In machine learning you may use sth related to distance and to do not machine with different units like kilometer or miles')
print('Their formula is different: min-mix scaling use (original-minimum)/(maximum-minimum) and will give number between 0 and 1')
print('Z-scaling use (original-main value)/standard deviation ')
data = {
    'Height (cm)': [160, 170, 180, 190],
    'Weight (kg)': [55, 60, 65, 70]
}
df = pd.DataFrame(data)
print(df)
def min_max_scaling(x):
    return (x - x.min()) / (x.max() - x.min())
min_max_scaled_df = df.apply(min_max_scaling)
print("Min-Max Scaled Data:")
print(min_max_scaled_df)
def z_score_normalization(x):
    return (x - x.mean()) / x.std()
z_score_scaled_df = df.apply(z_score_normalization)
print("\nZ-Score Scaled Data:")
print(z_score_scaled_df)
'''
5. Handling Outliers Questions:

What are outliers, and why might they impact machine learning models?
Describe different methods for detecting outliers in a dataset in Python
How can you handle outliers in a continuous numerical variable in Python?
'''
print('Outlier is the number which is changing all data information. For example, let us say MATMIE wrote an exam for 25 students who got points from 90-100, and the other 5 got 0. And average number will be 75-83, but no one got these points. Here we can not say students exam results between 75-83.')
print('with comand describe you can know general information and compare them')
print(file.describe()['Calories'])
print('other method')
import numpy as np
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
print(data)
print("Lower bound:", abs(lower_bound))
print("Upper bound:", upper_bound)
print('1. You can just remove outlier to get result')
print('2. Change ir with mode or mean value')
print('3. Make it less impact to your result by using mathematical operations')
print('4.You can output two results one with outlier and the second without outlier.')
print('5. ')
print(file.ndim)