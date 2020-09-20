#!/usr/bin/env python
# coding: utf-8

# In[69]:


#package
import numpy as np


# In[70]:


a= np.array([11,22,33,44,55])


# In[71]:


print (a)


# In[72]:


print (type(a))


# #### multidimension

# In[73]:


b= np.array([[11,22,33,44,55],[1,2,3,4,5]])


# In[74]:


print (b)


# In[75]:


print (type(b))


# ### Complex type

# In[76]:


c= np.array([77,44,12,32],complex)


# In[77]:


print (c)


# In[78]:


type (c)


# ### Function ' ndim'
# How many dimension؟
# 

# In[79]:


print (a.ndim)


# In[80]:


print (b.ndim)


# ### Function ' itemsize'
# How many size?
# 
# 1 item = 4 byte
# 

# In[81]:


print (a.itemsize)


# In[82]:


print (b.itemsize)


# In[83]:


print (c.itemsize)


# ### Function ' dtype' , ' size' , 'shape'
# 

# In[84]:


print (a.dtype)


# In[85]:


print (a.size)


# In[86]:


print (a.shape)


# In[87]:


print (b.dtype)


# In[88]:


print (b.size)


# In[89]:


print (b.shape)


# In[90]:


print (c.dtype)


# In[91]:


print (c.size)


# In[92]:


print (c.shape)


# ## Reshaping the array

# In[93]:


myarray = np.array([[11,22,33,44] ,[11,22,33,55], [1,2,3,4]])


# In[94]:


print (myarray)


# print (myarray.shape)

# In[95]:


myarray2 = myarray.reshape(4,3)


# In[96]:


print (myarray2)


# #### Hash

# In[97]:


print (myarray)


# In[98]:


print (myarray[0,1])


# In[99]:


print (myarray[2,1])


# In[100]:


print (myarray[0,0])


# ## arithmetic operators for array

# In[101]:


myarray3 = np.array([[11,22,33,44] ,[11,22,33,55], [1,3,4,5]])


# In[102]:


myarray4 = np.array([[13,14,15,16] ,[11,22,33,55], [1,3,4,5]])


# In[103]:


print (myarray3 * myarray4)


# In[104]:


print (myarray3 + myarray4)


# In[105]:


print (myarray3 + myarray4)


# ### connect 
# * horizontal
# * Vertical 

# In[106]:


#horizontal
print(np.hstack((myarray3 ,myarray4)))


# In[107]:


#Vertical
print(np.vstack((myarray3 ,myarray4)))

