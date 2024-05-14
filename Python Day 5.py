#!/usr/bin/env python
# coding: utf-8

# #lambda functions
# #annoymous function #name #function start with lambda

# In[1]:


def func(x):
    return x+10
func


# In[2]:


lambda x: x+10


# In[3]:


out=lambda x: x+10
out(5)


# High oreder function
# map, filter, reduce

# map --> it do not loads the whole data it just takes only a element and returns the output
# map(fun,iterable<list)

# In[4]:


def square(x):
    return x*x

mylist=[10,20,30,40,50]

list(map(square,mylist))


# In[5]:


mylist=[10,20,30,40,50]

list(map(lambda x: x*x,mylist))


# In[9]:


mylist=[10,20,30,40,50]

list(filter(lambda x:x%2==0,mylist)) # filter applyes a condition 


# In[16]:


# open the file
# perform read / write operations
# close the file
#open(file, accesmode)
fileobj=open("regex.txt","r")
x=fileobj.read()
fileobj.close()


# In[37]:


# r-->read
# w-->write
# r+ --> read and write
# w+ --. it will re-create the file and remove the old content with new one
fileobj=open("regex.txt","r+") 
print("Before write",fileobj.tell()) # tell functions tells the position of the function
x=fileobj.read()
fileobj.write("I am Milan Kachhawaha")
fileobj.seek(12) # seek will help to change the position of the cursor
print("After write write",fileobj.tell()) 
fileobj.close()


# In[38]:


print(x)


# In[39]:


# reading file with "with key word"
with open("regex.txt","r") as fileobj:
    x=fileobj.read()
print(x)


# In[51]:


# reading lines line by line
with open("regex.txt","r") as fileobj:
    for line in fileobj.readlines():
        print(line.strip()) # strip function removes the extra sapaces


# In[57]:


with open("regex.txt","r") as fileobj:
    for line in fileobj.readlines():
        for word in line.split(','):
            print(word)


# In[64]:


# exception handeling
# try and except
try:
    print("Hello")
    x=10
    x/num
    print("hey")
except(ZeroDivisionError,NameError) as z:
    print("Error handeling :",z)


# In[68]:


try:
    print("Hello")
    x="Milan"
    x[10]
    print("hey")
except(ZeroDivisionError,NameError) as z:
    print("Error handeling :",z)
except Exception as e:  # Exception handles all the error except syntax error
    print(e,": error occured")


# In[69]:


try:
    print("Hello")
    x="Milan"
    try: 
        x[10]
    except:
        print("dividing it by num")
    print("hey")
except(ZeroDivisionError,NameError) as z:
    print("Error handeling :",z)
except Exception as e:  # Exception handles all the error except syntax error
    print(e,": error occured")


# In[71]:


try:
    print("Hello")
    print("hey")

except Exception as e:  
    print(e,": error occured")

else: # when try block has no error in it the only else will be priented
    print("Try block  has no error")


# In[72]:


try:
    print("Hello")
    print("hey")

except Exception as e:  
    print(e,": error occured")

finally: # it will run in ervery condition whether there is an error or not
    print("Try block  has no error")


# Assignment 
# Question 1
# open browser --> open inastagram --> insert the values --> sign up to make account
# 
# Question 2
# Create a function which will take a number from a user and one a number is being provided you have to draw the same of messagesnto your friend.
# 
# 

# In[79]:


import webbrowser
import urllib.request
webbrowser.open('http://www.instagram.com/', new=2)  


# In[ ]:





# In[ ]:




