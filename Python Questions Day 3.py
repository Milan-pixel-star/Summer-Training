#!/usr/bin/env python
# coding: utf-8

# In[2]:


c=10
for i in range(1,5):
    for j in range(1,6-i):
        print(c,end=" ")
        c-=1
    for k in range(1,i+1):
        print("*",end=" ")
    print('')


# In[12]:


for i in range(1,5):
    for j in range(0,5-i):
        print(chr(j+65),end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    print('')


# In[25]:


c=0
for i in range(1,5):
    for j in range(0,5-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(chr(c+65),end=" ")
        c+=1
    print('')


# In[39]:


c=1
a=1
for i in range(1,5):
    for j in range(1,6-i):
        print(chr(c+64),end=" ")
        c+=1
    for k in range(1,i+1):
        print(a,end=" ")
        a+=1
    print('')


# In[63]:


N = 3
for i in range(1, N + 1):
    for j in range(1, i):
        print("  ", end="")
       
    for j in range(1, 2 * (N - i) + 2):
        print("* ", end="")

    print()

# Question
# take a input from user that is no of days
# I have to samve some Rs every day
# when i reach the next week I have to save double of previous week same with 3
# give the output of how much money he will save in the input days
# In[92]:


total_days=int(input("Enter the days : "))
week_length=7
total_savings=0
total_week=total_days//week_length
extra_days=total_days-(total_week*week_length)
for day in range(1,total_week+1):
    total_savings=total_savings+(day*week_length)
total_savings=total_savings+(extra_days*day)
print("Total savings within",total_days,"days is ₹",total_savings)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




