#!/usr/bin/env python
# coding: utf-8

# Q1 Swap the number without using third varible

# In[6]:


var1=int(input("Enter the varibable 1 : "))
var2=int(input("Enter the varibable 2 : "))
print(f"Befor swap {var1,var2}")
var1=var1+var2
var2=var1-var2
var1=var1-var2
print(f"After swap {var1,var2}")


# Q2 : Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the
# digits.

# In[19]:


var1 = str(input("Enter a number: "))
var1 = var1[::-1]
var2 = ""
for i in range(len(var1)):  
    var2 += str(var1[i])
    var2 += " "
print(var2)


# Q3 Write a program that will give you the sum of 3 digits

# In[18]:


var1=int(input('Enter number 1 : '))
var2=int(input('Enter number 2 : '))
var3=int(input('Enter number 3 : '))
print("Sum is : ",var1+var2+var3)


# Q4 Write a program that will take three digits from the user and add the square of each
# digit.

# In[20]:


var1 = str(input("Enter a number: "))
var2 = 0
for i in range(len(var1)):  
    var2 += (int(var1[i]))*(int(var1[i]))
print(var2)


# Q5 Write a program that will check whether the number is armstrong number or not.

# In[27]:


var1=str(input("Enter the number : "))
power=len(var1)
var2 = 0
for i in range(len(var1)):  
    var2 += (int(var1[i]))**power
var1=int(var1)
if var1==var2:
    print("Number is armstrong")
else:
    print("Number is not armstrong")


# Q6 :Write a program that will take user input of (4 digits number) and check whether the
# number is narcissist number or not.

# In[28]:


var1=str(input("Enter the 4 digit number : "))
var2 = 0
for i in range(len(var1)):  
    var2 += (int(var1[i]))**4
var1=int(var1)
if var1==var2:
    print("Number is armstrong")
else:
    print("Number is not armstrong")


# Q7 Display float number with 2 decimal places using print()

# In[34]:


var1=float(input("Enter a number : "))
print(round(var1,2))


# Q8 Print all factors of a given number provided by the user.

# In[35]:


var1=int(input("Enter a number : "))
for i in range(1,var1+1):
    if var1%i==0:
        print(f"{var1} factor is {i}")


# Q9 Accept a list of 5 float numbers as an input from the user

# In[39]:


var1=[]
for i in range(1,6):
    var1.append(float(input(f"Enter the float no {i} : ")))
print(var1)


# Q10 : Write a program to find the volume of the cylinder. Also find the cost when ,when the
# cost of 1litre milk is 40Rs.

# In[40]:


hight=float(input("Enter the hight of cylinder : "))
radius=float(input("Enter the radius of cylinder : "))
volume=3.14*(radius**2)*hight
print(f"Volume of cylinder is : {volume}")
print(f"Cost of milk in cylinder is : {volume*40}Rs")


# In[ ]:




