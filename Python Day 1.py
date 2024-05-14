#!/usr/bin/env python
# coding: utf-8

# In[1]:


company = "regex"
print("company name is:",company)


# In[2]:


company = "regex"
year = 2024
print("company name is:",company , ", year is :" , year)


# In[3]:


company = "regex"
year = 2024
print( f"company name is {company} year is {year}")


# In[5]:


username ="Milan"
msg=f"hey user {username} "
print(msg)
username="aman"
print(msg)


# In[6]:


city = "Jaipur"
city = "Jodhpur"
print(city)


# In[7]:


city = "jaipur"
print("before:", id(city))
y="jaipur"
print("Y :", id(y))
city = "isha"
print("after:", id(city))


# In[8]:


print(y)


# In[9]:


#operator
# Arithmetic
a=20/3
type(a)
print(a)


# In[10]:


20//3


# In[11]:


10.0+5


# In[12]:


1+5*4/2-7+8


# In[13]:


4//2


# In[14]:


20%3


# In[15]:


3**4


# In[16]:


2**3


# In[17]:


1+5*3-2/1+2


# In[18]:


x=10
x+5
print(x)


# In[19]:


x=10
y=19

x==10 and y>18


# In[21]:


"J" in "Jodhpur"


# In[22]:


"j" in "Jodhpur"


# In[23]:


"pur" in "Jodhpur"


# In[24]:


"purj" in "Jodhpur"


# In[25]:


"purj" in "Jodhpur"


# In[26]:


# identity
# variable -> data type
# object belong to a class
x=10
type(x) is int


# In[27]:


x="abc"
type(x) is not int


# In[28]:


x=500
y=500
x==y
x is y


# In[30]:


x=250
y=250
id(x)


# In[31]:


id(y)


# In[32]:


# conditional statement


# In[33]:


x=10
if(True):
    print("Hello")


# In[35]:


# rather than else we will use multiple condition by using elif
x =12
if( x==10 ):
    print("hello")
else:
    print("condition is false")
if (x == 12) :
    print("hey")
else:
    print("condition is false")


# In[37]:


# rather than else we will use multiple condition by using elif
x =15
if( x==10 ):
    print("hello")
elif (x == 12) :
    print("hey")
else:
    print("condition is false")


# In[38]:


# take three variable an find out the minimum value
a, b, c = 5, 7, 10
if(a <= b and a <= c):
    print(a, "is the smallest")
elif(b <= a and b <= c):
    print(b, "is the smallest")
else:
    print(c, "is the smallest")


# Q1. user input on number of unit in integer
# - for the starting 10 unit price is 50 rs each
# - for the next 20 unit price is 20 rs each
# - for the rest of unit price will be 10 rs
# calculate the total price

# In[41]:


num_units = int(input("Enter the number of units: "))
total_price = 0

if num_units >= 10:
    total_price += 10 * 50 
    num_units -= 10 
if num_units >= 20:
    total_price += 20 * 20 
    num_units -= 20 
total_price += num_units * 10 
print("Total price:", total_price)


# Q2.
# take 3 number as input from a user as 3 side of a triangle
# and check wheather it will create a triangle or not

# In[42]:


a = float(input("Enter the length of a: "))
b = float(input("Enter the length of b: "))
c = float(input("Enter the length of c: "))

if a+b>c and a+c>b and b+c>1:
    print("Yes, triangle can be made")
else:
    print("No, triangle is not possible")


# Q3. take two no. from the user and check wheather both the number are divisible by 6
# (divisibility rule say it should be divided by 2 and 3)

# In[43]:


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if (num1 % 2 == 0 and num1 % 3 == 0 and num2 % 2 == 0 and num2 % 3 == 0):
    print("Both numbers are divisible by 6.")
else:
    print("Both numbers are not divisible by 6.")


# Q4
# - if a user have given me input 1
# print current date
# - if a user give me input 2
# desktop pr ek folder bana na h user dega name
# - if user give me input 3
# to desktop pr ek file banye ga
# - if user give me input 4
# - to system shut down kr dena h

# In[44]:


import os
from datetime import datetime

choice=int(input("Enter the number betwenn 1-4"))
if choice not in range(1,5):
    print("Enter a valid range")
else: 
    if choice==1:
        print(datetime.today().strftime("%Y-%m-%d"))
    elif choice==2:
        folder_name = input("Enter the folder name: ")
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        folder_path = os.path.join(desktop_path, folder_name)
    elif choice==3:
        file_name = input("Enter the file name: ")
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        file_path = os.path.join(desktop_path, file_name)
    elif choice==4:
        confirmation = input("Are you sure you want to shut down the system? (y/n): ").lower()
        if confirmation == 'y':
            print("Shutting down the system...")
            os.system("shutdown -s -t 0")
            print("System shut down.")


# In[ ]:




