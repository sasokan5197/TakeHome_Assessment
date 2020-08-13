#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 12:24:28 2020

@author: sahanaasokan
"""


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt 
import seaborn as sns 
import datetime

#Analyze Confirmation Reasons (Fair Direct vs Fair Direct link) 'Confirmation_reason'?

df_ver6 = pd.read_excel('data_ver6.xlsx', encoding='utf-8')
df_ver4 = pd.read_excel('data_ver4.xlsx', encoding='utf-8')

sns.set(rc={'figure.figsize':(11,7)})
sns.set(style="whitegrid", color_codes=True)
pal = sns.color_palette("Blues_r", len(df_ver4))
plt.title('Acquired Retailers vs Confirmation_Reason')             
sns.barplot(x='Confirmaton_Reason',y= 'Count_retailer_placed_first_confirmed_order_at', data=df_ver4,palette=pal)

Percentage_SignedUP_ConfirmedRetailer= (13574/14004)*100
Percentage_FirstOrder_ConfirmedRetailer= (394/14004)*100
Percentage_Support_ConfirmedRetailer= (35/14004)*100