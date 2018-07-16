
# coding: utf-8

# In[1]:
import pdb
import numpy as np


# In[2]:

data = np.load('monthdata.npz')
totals = data['totals']
counts = data['counts']


# In[3]:

print("Row with lowest total precipitation:")


# In[4]:

total_row = totals.sum(axis=1)


# In[5]:

print(np.argmin(total_row))


# In[6]:

print("Average precipitation in each month:")


# In[7]:

total_column = totals.sum(axis=0)


# In[8]:

#print(totals)


# In[9]:

#print(counts)


# In[10]:

#print(total_precipitation)


# In[11]:

count_column = counts.sum(axis=0)


# In[12]:

#print(total_count)


# In[13]:

print(total_column / count_column)


# In[14]:

print("Average precipitation in each city:")


# In[15]:

count_row = counts.sum(axis=1)


# In[16]:

print(total_row/count_row)


# In[17]:

print("Quarterly precipitation totals:")


# In[18]:

quarterly_precipitation = totals.reshape(36,3)


# In[19]:

#print(quarterly_precipitation)


# In[20]:

total_quarterly_precipitation = quarterly_precipitation.sum(axis=1)


# In[21]:

#print(total_quarterly_precipitation)


# In[22]:

result = total_quarterly_precipitation.reshape(9,4)


# In[23]:

print(result)

