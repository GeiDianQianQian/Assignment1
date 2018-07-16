
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd


# In[2]:

totals = pd.read_csv('totals.csv').set_index(keys=['name'])


# In[3]:

counts = pd.read_csv('counts.csv').set_index(keys=['name'])


# In[4]:

#print(totals)


# In[5]:

#print(counts)


# In[6]:

print("City with lowest total precipitation:")


# In[7]:

total_row = totals.sum(axis=1)


# In[8]:

print(total_row.idxmin())


# In[9]:

print("Average precipitation in each month:")


# In[10]:

total_column = totals.sum(axis=0)


# In[11]:

#print(total_column)


# In[12]:

count_column = counts.sum(axis=0)


# In[13]:

print(total_column / count_column)


# In[14]:

print('Average precipitation in each city:')


# In[15]:

count_row = counts.sum(axis=1)


# In[16]:

print(total_row/count_row)
