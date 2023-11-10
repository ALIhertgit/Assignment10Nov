# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 01:48:42 2023

@author: ali10
"""

import pandas as pd
import matplotlib.pyplot as plt  

""" load the data set"""
df = pd.read_csv('C:/Users/ali10/Downloads/goal11.wastegdp.csv')

"""Check the first few rows of the DataFrame"""
print(df.head())

top_10_countries = df.nlargest(10, 'pop')

print(top_10_countries[['iso3c', 'pop', 'gdp', 'waste', 'sharepopurban', 'wastepercap']])

"""Pie Chart for Waste Distribution"""

plt.figure(figsize=(8, 8))
plt.pie(top_10_countries['waste'], labels=top_10_countries['iso3c'], autopct='%1.1f%%', startangle=360)
plt.title('Waste Distribution for Top 10 Populated Countries')
plt.axis('equal')
plt.show()
 
top_10_populated = df.nlargest(10, 'pop')

"""Scatter plot GDP vs. Waste Per Capita"""

def create_scatter_plot_top_10(df, x_column, y_column, title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x_column], df[y_column], alpha=0.5)
    for i, row in df.iterrows():
        plt.text(row[x_column], row[y_column], row['iso3c'], fontsize=9)
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

create_scatter_plot_top_10(top_10_populated, 'gdp', 'wastepercap', 'GDP vs Waste Per Capita for Top 10 Populated Countries', 'GDP (in USD)', 'Waste Per Capita (in kg)')

"""Bar Chart representing Waste Per Capita for Top 10 Populated Countries"""

top_10_populated = df.nlargest(10, 'pop')

def create_bar_chart(df, x_column, y_column, title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    plt.bar(df[x_column], df[y_column], color='blue', edgecolor='black')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)  
    plt.grid(axis='y', alpha=0.75)
    plt.show()

create_bar_chart(top_10_populated, 'iso3c', 'wastepercap', 'Waste Per Capita for Top 10 Populated Countries', 'Country', 'Waste Per Capita (in kg)')




