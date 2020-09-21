#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# Function 
# * add ==> sum

# In[5]:


a = np.char.add(["Hani ","Ali "],["Ash","Mohmmed"])


# In[6]:


print(a)


# Function 
# * multiply ==> cross

# In[11]:


b= np.char.multiply("Hani ", 4)


# In[12]:


print (b)


# Function
# 
# * capitalize ==> 1st Letter capital

# In[18]:


c= np.char.capitalize("hani ash ")


# In[19]:


print (c)


# In[22]:


d= np.char.title("hani yousef ashour")


# In[23]:


print (d)


# In[25]:


e= np.char.lower("HANI YOUSEF ASHOUR")


# In[26]:


print (e)


# In[27]:


f= np.char.upper("hani yousef ashour")


# In[28]:


print (f)


# In[34]:


g= np.char.split("hani yousef ashour" , sep=" ")


# In[35]:


print(g)


# In[36]:


print (type(g))


# In[37]:


h= np.char.join("-","Hani Ash")


# In[38]:


print (h)


# * ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ

# In[39]:


mystr="Hani Ash"


# In[40]:


print(mystr)


# In[41]:


i = np.char.replace(mystr,"Ash","yousef")


# In[42]:


print(i)


# In[ ]:




