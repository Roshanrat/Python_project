#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd
import numpy as np


# In[16]:


car = pd.read_csv(r"C:\Users\HP\Desktop\2. Cars Data1.csv")


# In[17]:


car.head()


# In[18]:


car.shape


# instruction (for data cleaning)

# In[46]:


car.isnull().sum()


# In[35]:


car['Cylinders'].fillna(car['Cylinders'].mean(), inplace=True)


# row selection
# 

# In[49]:


car.head(7)


# column selection and values counts

# In[53]:


car['Make'].value_counts()


# filtering ( Origin o capital)

# In[56]:


car[car['Origin'].isin(['Asia','Europe'])]


# removing unwanted records

# In[58]:


car[~(car['Weight']>4000)]


# increase / adding values

# In[60]:


car.head()


# In[63]:


car['MPG_City'] = car['MPG_City'].apply(lambda x:x+3)


# In[64]:


car.head(2)


# In[ ]:




