#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# ## 404 

# In[2]:


myarray1= np.array([11,22,33,44,55,66,77,88,99,100])


# In[3]:


myarray2= np.array([[11,22,33,44,55],[66,77,88,99,100]])


# In[4]:


myarray3=np.array([1,2,3,4,5])


# In[5]:


myarray_total=myarray1+myarray2


# In[6]:


myarray_total=myarray1+myarray3


# # Broadcasting 

# In[7]:


myarray_1= np.array( [[11,22,33,44,55],[66,77,88,99,100]] )


# In[8]:


myarray_3=np.array([11,22,33,44,55])


# In[9]:


myarray_total_13=myarray_1+myarray_3


# In[11]:


print(myarray_total_13)


# In[ ]:




