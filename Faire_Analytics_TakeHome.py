#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 12:15:03 2020
@author: sahanaasokan
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt 
import seaborn as sns 
import datetime


#Load the CSV
df= pd.read_csv('elevate_analytics_case_data.csv')
num_cols = df._get_numeric_data().columns


#Overall statistics of the dataframe. Data Types and Null Counts.
df.info()

#Lets find the missing counts.
missing_count= ((df.isna().sum()/(218538))*100).sort_values(ascending=False)
missing_data= pd.concat([missing_count],axis=1,keys=['Missing Count'])
missing_data.reset_index(inplace=True)

#Deaing with time-series
df['retailer_placed_first_confirmed_order_at']= pd.to_datetime(df['retailer_placed_first_confirmed_order_at'])

#Get Dummy Variables 'normalized_referer','confirmation_reason' 
encoded_df=pd.get_dummies(df, columns=['normalized_referer','confirmation_reason'])


#Correlation Graph to see any relationships.
Encoded_correlations = encoded_df.corr()
fig = plt.subplots(figsize=(5,5))
figure_2=sns.heatmap(Encoded_correlations,vmax= 0.9,cmap='Blues',square=True)
plt.show()

#Graph visualizing Missing Counts.


sns.set(style="whitegrid", color_codes=True)
pal = sns.color_palette("BuGn_r", len(missing_data))
sns.barplot(x='index', y= 'Missing Count',data= missing_data, palette=pal)
sns.set(rc={'figure.figsize':(9,8)})
plt.ylabel('Missing Percentage')
plt.xlabel('Column')
plt.title('Null Percentage of Columns')
plt.xticks(rotation='vertical')
plt.legend(loc=2)
plt.show()


# We are trying to understand the decline of Retailers and their Confirmed Orders
decline_df = (pd.to_datetime(df['retailer_placed_first_confirmed_order_at'])
       .dt.floor('d')
       .value_counts()
       .rename_axis('Date')
       .reset_index(name='count')
       .sort_values('Date'))

decline_df.set_index('Date', inplace=True, drop=True)
decline_df.index = pd.to_datetime(decline_df.index)

#Plot the decline of acquired retailers.
decline_df.plot(color= 'green')
plt.ylabel('Confirmed Retailer Count')
plt.xlabel('Date')
plt.title('Confirmed Acquired Retailers vs Date')
plt.legend(loc=2)
plt.show()



'''#Exploratory Analysis for normalized referer for Overall Dataset.
Refered_counts = df['normalized_referer'].value_counts()
Refered_counts= Refered_counts.to_frame()
Refered_counts.reset_index(inplace=True)

sns.set(style="whitegrid", color_codes=True)
pal = sns.color_palette("BuGn_r", len(Refered_counts))
figure_1 = sns.barplot(x='index',y='normalized_referer',data=Refered_counts,palette=pal)
plt.ylabel('Confirmed Retailer Count')
plt.xlabel('Types of Normalized Referer')
plt.title('Confirmed Retailers vs Types of Normalized Referer')

plt.show()
'''




              




