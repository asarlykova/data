# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 11:32:54 2024

@author: User
"""
# =============================================================================
# Basic Plot: Line, Bar, Scattered, Pie Chart, 3D
#Advanced Plot: Box, 2D Heatmap, Stacked Bar, Gantt Chart, Polar
# =============================================================================
import numpy as np
import seaborn as sns
import plotly as py
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
data= pd.read_csv('data.csv')
data.info()


# Basic Plot: Line
plt.figure(figsize=(8, 6))
plt.plot(data['Pulse'], data['Duration'])
plt.title('Line Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

# Basic Plot: Bar
plt.figure(figsize=(8, 6))
plt.bar(data['Duration'], data['Calories'])
plt.title('Bar Plot')
plt.xlabel('Duration')
plt.ylabel('Calories')
plt.show()

# Basic Plot: Scatter
plt.figure(figsize=(8, 6))
plt.scatter(data['Pulse'], data['Calories'])
plt.title('Scatter Plot')
plt.xlabel('Pulse')
plt.ylabel('Calories')
plt.show()

# Basic Plot: Pie Chart
plt.figure(figsize=(8, 6))
plt.pie(data['Calories'], labels=data['Duration'], autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()

# Basic Plot: 3D
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data['Duration'], data['Calories'], data['Duration'])
ax.set_title('3D Scatter Plot')
ax.set_xlabel('Duratoin')
ax.set_ylabel('Calories')
ax.set_zlabel('Pulse')
plt.show()



data.plot(x ='Duration', y='Calories', kind='scatter')
plt.show()

data.plot(kind='hist')
plt.show()

data.plot()
plt.show()

numeric_columns = ['Calories', 'Duration', 'Pulse','Maxpulse']
data = pd.read_csv('data.csv', usecols=numeric_columns)
data.plot()
plt.show()

correlation_matrix = data.corr()
axis_corr = sns.heatmap(correlation_matrix,vmin=-1, vmax=1, center=0,cmap=sns.diverging_palette(50, 500, n=500),square=True)
plt.show()