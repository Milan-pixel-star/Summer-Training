#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(1,5):
    for j in range(1,5):
        print("* ",end="")
    print("")


# In[21]:


for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print("")


# In[60]:


c = 1
for i in range(1,5):
    for j in range(1,i+1):
        print(c,end="")
        c=c+1
    print('')


# In[61]:


c = 10
for i in range(1,5):
    for j in range(1,i+1):
        print(c,end="")
        c=c-1
    print('')


# In[64]:


for i in range(1,5):
    for j in range(0,i):
        print(chr(j+65),end="")
    print("")


# In[22]:


for i in range(0,4):
    for j in range(0,i+1):
        print(chr(i+65),end="")
        i=i+1
    print('')


# In[ ]:





# In[38]:


c = 25
for i in range(1,5):
    for j in range(1,i+1):
        print(chr(c+65),end="")
        c=c-1
    print('')


# In[18]:


n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i == j) or (j == 1) or (i==n):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")


# In[34]:


c = 1
for i in range(0,4):
    for j in range(0,i+1):
        print(c,end="")
        print(chr(c+96),end="")
        c=c+1
    print('')


# In[7]:


c = 1
for i in range(0,4):
    for j in range(0,i+1):
        print(chr(c+96),end="")
        c=c+1
    print('')


# In[14]:


c = 1
for i in range(1,5):
    for j in range(1,i+1):
        print(c,end="")
        c=c+1
    print('')


# In[80]:


c = 26
for i in range(1,4):
    for j in range(1,i+1):
        print(chr(64+c),end="")
        c=c-2
    print('')


# In[92]:


c = 1
for i in range(1,5):
    for j in range(1,i+1):
        print(chr(64+c),end="")
        c=c+1
    print('')


# In[ ]:





# In[ ]:




