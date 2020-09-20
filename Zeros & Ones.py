#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# ## Zeros
# The zeros() function is used to get a new array of given shape and type, filled with zeros.
# 
# 
# Determined:
# * the shape
# * Type
# * style

# In[2]:


np.zeros((3,2),dtype=float)


# In[4]:


myarray = np.zeros((3,2),dtype=int)


# In[5]:


print (myarray)


# ## Ones
# 

# In[8]:


myarray2 = np.ones((4,3),dtype=int)


# In[9]:


print (myarray2)


# ## empty 
# random

# In[10]:


myarray3 = np.empty((2,3),dtype=int)


# In[11]:


print (myarray3)


# In[ ]:




