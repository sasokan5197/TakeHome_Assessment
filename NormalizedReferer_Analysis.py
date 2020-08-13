#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 10:24:07 2020

@author: sahanaasokan
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt 
import seaborn as sns 
import datetime

#Creating a new table to do a deeper dive into relationships.
#Did Data Manipulation using Excel/SQL to group by specific metrics.

df_ver3 = pd.read_excel('data_ver3.xlsx', encoding='utf-8')
sns.set(rc={'figure.figsize':(11,7)})
sns.set(style="whitegrid", color_codes=True)
pal = sns.color_palette("GnBu_d", len(df_ver3))
plt.title('Acquired Retailers vs Type of Referer')
sns.barplot(x='normalized_referer',y= 'Count_retailer_placed_first_confirmed_order_at', data=df_ver3,palette=pal)

Percentage_BlankReferer_ConfirmedRetailer= (12899/14004)*100


#Outgoing Email Id.
#72.9% of the retailers clicked on the link outside of our email (72.9% of Outgoing Email ID is null)
#(~59,005 retailers clicked on the link through our email)
#(14,004 Confrmed Retailers)
#(23.7% conversion within our link)

