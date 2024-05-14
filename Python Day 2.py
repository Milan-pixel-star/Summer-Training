#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:


state="Rajasthan"


# In[2]:


state[0]


# In[3]:


state[1]


# In[4]:


#according to the position
#using (slicing operator)
# [start:stop:[step=1]]


# In[6]:


state[0:4] #stoping position is never included


# In[7]:


state[2:6]


# In[8]:


state[0:6]


# In[9]:


state[0:]


# In[11]:


state[0:4]
state[:4]
state[0:4:1]


# In[12]:


state[0:5:1]


# In[13]:


state[0:5:2]


# In[16]:


state[0:4:-1]    


# In[19]:


state[-1:-4]


# In[20]:


#looping (repetative)
#for(i=0;i<condition;i++)
#range function 


# In[21]:


#for i in range (0,10)
#range (start , stop , step)


# In[25]:


for i in range(1,5):
    print(i)


# In[26]:


for i in range(1,8,3):
    print(i)


# In[27]:


# loop 97 to 18 print no which divides with 5 and 7


# In[28]:


for i in range(97,18,-1):
    if(i%5==0 and i%7==0):
        print(i)


# In[29]:


for i in "Hello":
    print(i)


# In[30]:


#if we are able to perform loop om any thing then it is itterable


# In[31]:


data="Hello"


# In[32]:


len(data)


# In[39]:


for i in range(0,5):
    print(i,data,data[i])


# In[48]:


#a for loop to count total characters in a string
a="Rajasthan"
b=0
for i in a:
    b=b+1
print(b)


# In[51]:


a="Milan Kachhawaha"
b=0
for i in a:
    if(i in "aeiou"):
        b=b+1
print(b)


# In[52]:


a="Milan Kachhawaha"
b=0
for i in a:
    if(i not in "aeiou"):
        b=b+1
print(b)


# In[57]:


for i in range(1,5):
    print("hello",i)
    
    for j in range(1,5):
        print("milan",i)


# In[71]:


for i in range(1,5):
    for j in range(1,5):
        print("* ",end="")
    print("")


# In[103]:


for i in range(1,5):
    for j in range(i,5):
        print("* ",end="")
    print("")


# In[100]:


for i in range(1,5):
    for j in range(1,i+1):
        print("* ",end="")
    print("")


# In[85]:


for i in range(1,6):
    for j in range(1,5):
        print(i,end="")
    print("")


# In[105]:


for i in range(1,4):
    for j in range(1,6):
        print(j,end="")
    print("")


# In[92]:


for i in range(1,4):
    for j in range(5,0,-1):
        print(j,end="")
    print("")


# In[106]:


for i in range(1,5):
    for j in range(1,5):
        print(i,end="")
    print("")


# In[107]:


# Take a input string from user 
# min 3 capital character
# min 2 small character 
# min length 5-15 character
# and can have any special character like @,#,!


# In[108]:


# take interger no from user find that no is prime no or not


# In[138]:


a=0
b=0
password=input("Enter the password : ")
if(len(password)>=5 and len(password)<=15):
    for i in range(65,91):
        if(chr(i) in password):
            a+=1
            if(a>=3):
                for i in range(97,123):
                    if(chr(i) in password):
                        b+=1
                        if(b>=2):
                            if(chr(i) in "@#!"):
                                print("Strong Password")


# In[119]:


password="AILasd@#"


# In[121]:


ord(password[0])


# In[122]:


chr(65)


# In[ ]:





# In[ ]:





# In[124]:


ord('A')


# In[ ]:




