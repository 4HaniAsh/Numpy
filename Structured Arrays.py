#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# * Ref .
# * Data type opject
# https://docs.scipy.org/doc/numpy-1.10.4/reference/arrays.dtypes.html

# In[2]:


employee_info=[('name','S10') , ('salary','f8') , ('age','i8')]


# In[3]:


employee_info


# In[4]:


employees_staff=np.zeros((3),dtype= employee_info)


# In[5]:


employees_staff


# In[6]:


employees_staff[2] = ("Hani", 3000,25)


# In[7]:


employees_staff[1] = ("Ahmed", 5000,32)


# In[8]:


employees_staff


# In[9]:


employees_staff[1:]


# In[10]:


salary=employees_staff['salary']


# In[11]:


salary


# In[12]:


age= employees_staff['age']


# In[13]:


age


# In[14]:


employees_staff['name']


# In[15]:


add_salary= salary+2000


# In[16]:


add_salary


# In[17]:


add_age= age+3


# In[18]:


add_age


# 

# In[19]:


employees_staff


# In[20]:


all_employees=np.zeros((4,3,2),dtype= employee_info)


# In[21]:


all_employees


# In[22]:


all_employees['name']


# In[23]:


all_employees['age']


# In[24]:


all_employees['salary']


# In[25]:


all_employees


# In[27]:


all_employees[0,0,1]=("hani",3000,24)


# In[28]:


all_employees


# In[29]:


all_employees[1,1,0]=("Ali",5000,30)


# In[30]:


all_employees


# In[31]:


all_employees[2,2,1]=("mahmoud",2000,28)


# In[32]:


all_employees


# In[33]:


all_employees[3,2,0]=("yousef",8000,42)


# In[34]:


all_employees


# In[35]:


all_employees["name"]


# In[36]:


all_employees["salary"]


# In[37]:


all_employees["age"]


# In[39]:


all_employees[ ["name","age"] ]


# In[40]:


all_employees[ ["name","salary"] ]


# In[ ]:




