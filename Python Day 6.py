#!/usr/bin/env python
# coding: utf-8

# In[1]:


# polymorphism
# many forms
# if any variable, operator, object behave differently then it is polymorphism


# In[2]:


1+2


# In[3]:


"1"+"2"


# In[6]:


class vehicle:
    def info(self):
        print("This is vehcile class")
    
    def info(self,x):
        print("This is second vehcile class") # overriding --> function paramater and name is same but implementation is differnt
        
c1=vehicle()
c1.info(100)  # method overloading is not supported in python 


# In[9]:


class vehicle:
    def info(self):
            print("This is vehcile class")

class tatamotors(vehicle):
    def info(self):
        print("This is tata class")

t1=tatamotors()
t1.info()


# In[16]:


class employee:
    def __init__(self, num1):
        self.num1=num1
    
    def __repr__(self):# when we have to print an object we use reper to show output
        return f"Employee class has value {self.num1}"
e1=employee(10)
print(e1)


# In[17]:


class employee:
    def __init__(self, num1):
        self.num1=num1
    
    def __repr__(self):# when we have to print an object we use reper to show output
        return f"Employee class has value {self.num1}"
employee(10)


# In[18]:


class employee:
    def __init__(self, num1):
        self.num1=num1
    
    def __repr__(self):# when we have to print an object we use reper to show output
        return f"Employee class has value {self.num1}"
e1=employee(10)
print(e1)

e2=employee(10)
print(e2)   
e1+e2 #operators don't work on class objects


# In[23]:


class employee:
    def __init__(self, num1):
        self.num1=num1
    
    def __repr__(self):# when we have to print an object we use reper to show output
        return f"Employee class has value {self.num1}"
    
    def __add__(x,y):
        print("hello",x.num1,y.num1)
e1=employee(10)
print(e1)

e2=employee(90)
print(e2)
e1+e2
# problem ca be solved using __add__ type of functions


# In[24]:


# method overloading and operator loading


# ''' 2 make two class objects and two instance method  if obj1>obj2 then true else false only 
# if obj1.var+obj.var2 > obj2.var only then return false else t`rue'''

# In[36]:


class employee:
    def __init__(self, num1,num2):
        self.num1=num1
        self.num2=num2
    
    def __repr__(self):# when we have to print an object we use reper to show output
        return f"Employee class has value {self.num1}"
    
    def __gt__(self,obj2):
        if(self.num1+self.num2>obj2.num1):
            return False
        else:
            return True
e1=employee(10,20)
e2=employee(35,25)

e1>e2


# In[37]:


# if there are more than 1 file then it is package and each file is called module
# public variable can be accessed in any package
# protected varible can be accessed by its own class and inherited package
# default/package protected variable can be accessed in only one package
# private variable can be accessed by the class but not by the object 


# In[43]:


class parents:
    _amount=100    # _variable means protected variable
    __amount2=200  #__variable for private variable, when private python change the variable name to _classname__variable name
p1=parents()
p1._parents__amount2


# In[47]:


class parents:
    __amount=100 

class son(parents):
    salary=10
s1=son()
s1._parents__amount


# In[ ]:




