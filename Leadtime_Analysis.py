#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 21:09:13 2020

@author: sahanaasokan
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plot 
import seaborn as sns 
#Lead time = 

#Load the CSV and take care of random spaces.
leadtime = pd.read_excel('Leadtime_Confirmed.xlsx')
leadtime.columns = [col.strip() for col in leadtime.columns]



#Dealiing with time-series data.
leadtime['retailer_placed_first_confirmed_order_at']= pd.to_datetime(leadtime['retailer_placed_first_confirmed_order_at'])
leadtime.set_index('retailer_placed_first_confirmed_order_at', inplace=True, drop=True)
leadtime.index = pd.to_datetime(leadtime.index)

#Lets visualize the Confiirmed Leadtime.
leadtime.plot(color='teal')
plot.ylim((0,500))
plot.ylabel('Confirmed Lead Time')
plot.xlabel('Date')
plot.title('Confirmed Lead Time vs Date')
plot.legend(loc=2)
plot.grid(True)
plot.show()


#Lets Find the Simple Day Moving Average of the Confirmed Leadtime
leadtime['MA_30'] = leadtime.Leadtime.rolling(30).mean()
leadtime['MA_30'].plot(label='MA 30 day')
plot.title('Simple MA(30) Confirmed Lead Time vs Date')
plot.ylabel('Confirmed Lead Time')
plot.xlabel('Date')
plot.ylim((0,500))
plot.legend(loc=2)
plot.grid(True)
plot.show()

mean=leadtime['Leadtime'].mean()
std=leadtime['Leadtime'].std()
median=leadtime['Leadtime'].median()
max=leadtime['Leadtime'].max()
min=leadtime['Leadtime'].min()

#Lead time Distribution
#Drop the Outlier
leadtime.reset_index(inplace=True)
id=leadtime[['Leadtime']].idxmax() 
#Create the table without the outlier.
Updated_leadtime=leadtime['Leadtime'].drop(id)
#Graph the Distribution
plot.title('Distribution of the Lead Time')
sns.distplot(Updated_leadtime)
plot.show()

