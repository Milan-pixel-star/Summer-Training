#!/usr/bin/env python
# coding: utf-8

# In[1]:


# functions -- A block of code which we can reuse according to our need
'''
def function_name():
        statement
'''


# In[2]:


def msg():   # function decleration
    print("Hello")


# In[4]:


msg()  # function calling
msg()
msg()


# In[9]:


def msg(x):  # x is paramater
    print("Hello",x)
    
msg("Milan")  # it as an argument


# In[10]:


def msg(x,y):
    print("x and y : ",x,y)
msg(10,20)


# In[11]:


def msg(x,y):
    print("x and y : ",x,y)
print(msg(10,20))


# In[13]:


def msg(x,y):
    print("x and y : ",x,y)
    return x+y
out=msg(10,20)
print(out)


# In[18]:


def funx(x):
    x=x+5
    
x=10
print("Before func :", x)
funx(x)  # python follows call by reference
print('After func :', x)  #int is immutable


# In[24]:


def func(x):
    x[0]="aman"
    print(x,id(x))
    

mylist=[10,20]
print("Mylist",mylist,id(mylist))
func(mylist)


# In[25]:


# create a function with 3 paramaters if 1st(excellent) > 2nd(good) > 3rd(average)

def func(x,y,z):
    if(x>y and x>z):
        print("Excellent")
    elif (y>x and y>z):
        print("Good")
    else:
        print("Average")

func(10,5,7)


# In[38]:


# a function which ar a scenario i.e it should return LCM of two numbers

def func(x, y):
    if x > y:
        greatest=x
    else:
        greatest=y

    while True:
        if (greatest%x==0) and (greatest%y==0):
            lcm = greatest
            break
        greatest += 1
    return lcm

num1 = 2
num2 = 9
print("The L.C.M. is", func(num1, num2))


# In[44]:


# Types of arguments
#positional argument
def employee(eid,ename,email):
    print(f'Eid is : {eid} \nEname is : {ename} \nEmail is : {email}')

employee("1","Raju","@email")


# In[46]:


# argument
def employee(eid,ename,email):
    print(f'Eid is : {eid} \nEname is : {ename} \nEmail is : {email}')

employee(ename="Raju",email="@email",eid='01')


# In[47]:


#default argument
def employee(eid,ename,email="regex software"):
    print(f'Eid is : {eid} \nEname is : {ename} \nEmail is : {email}')

employee("1","Raju") # required positional default


# In[49]:


# variable length argument
def facebook( *data ):
    print(data)
facebook(10,20,30) # not easy to identify the type of value


# In[55]:


# key word variable length argument
# args(variable length argument-- directuly , tuple), kwargs(key word length argument-- keyword,dictonary)
def facebook(**data):
    print(data,type(data))

facebook(username='Milan',salary=100)


# In[60]:


def func():
    print("Hello")

x=func # we can store function in a variable also
print(func)
print(x)
x()


# In[69]:


# high oreder functions --> functions which takes another function as a argument
def square(x):
    return x*x 
    
def addno(x,func):
    print(x,func)
    
addno(10,ssquare)


# In[71]:


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)


# In[ ]:




