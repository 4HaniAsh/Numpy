#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


mylist = [22,33,44,55,66,77,88,99] 


# In[3]:


print(mylist)


# In[4]:


myarray=np.asarray(mylist)


# In[5]:


print(type(myarray))


# In[6]:


print(type(mylist))


# In[7]:


mytuple=(22,33,44,55,66,77,88,99)


# In[8]:


print (type(mytuple))


# In[9]:


print(mytuple)


# In[10]:


myarray_from_tuple=np.asarray(mytuple)


# In[11]:


print (type(myarray_from_tuple))


# In[12]:


mylist2=[[22,33,44,55,66,77,88,99],[1,2,3,4,5]]


# In[13]:


print(mylist2)


# In[14]:


print(type(mylist2))


# In[15]:


myarray_from_list=np.asarray(mylist2)


# In[16]:


print(myarray_from_list)


# In[17]:


print(type(myarray_from_list))


# In[18]:


mystring=b"Hani Ash"


# In[19]:


print(type(mystring))


# In[20]:


mystring_array=np.frombuffer(mystring , dtype ="S1"  )


# In[21]:


print(type(mystring_array))


# In[22]:


print (mystring_array)


# In[ ]:




