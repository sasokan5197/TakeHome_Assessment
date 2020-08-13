#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 12:27:23 2020

@author: sahanaasokan
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt 
import seaborn as sns 
import datetime

#Does the business type have an influence on the amount of online conversions?

df_ver5 = pd.read_excel('data_ver5.xlsx', encoding='utf-8')
df= df_ver5.nlargest(20, columns=['Count_Retailer_business_type'])


sns.set(rc={'figure.figsize':(11,7)})
sns.set(style="whitegrid", color_codes=True)
pal = sns.color_palette("Blues_r", len(df))
plt.xticks(rotation='vertical')
plt.title('Counts of Business Type')             
sns.barplot(x='Business_Type',y= 'Count_Retailer_business_type', data=df,palette=pal)
