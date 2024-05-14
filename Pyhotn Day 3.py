#!/usr/bin/env python
# coding: utf-8

# In[17]:


for i in range(1,6):
    for j in range(i,5):
        print(chr(36),end=" ")
    for j in range(1,i+1):
        print(chr(42),end=" ")
    print("")


# In[18]:


#while loop
# while(conditoin)
#for i in range(1,5)
i=1
while(i<5):
    print("hello",i)
    i+=1


# In[22]:


#list, tuple, dictionary,set
#list -> collection of elements,which has index position 
# mutable data type
# ordered collection of elements
# list is by default function

mylist=[10,20,'nana']
type(mylist)


# In[24]:


mylist[0]


# In[26]:


mylist[0]=100  #updqte the value of list 


# In[31]:


#add the elemeent into the list
mylist.append(50)
# element wile be added at the last
# at a time one element can be added


# In[32]:


mylist


# In[33]:


#to add more than one element ain a list we use extend function
mylist.extend(['hey',99])


# In[34]:


mylist


# In[36]:


help(mylist)


# In[38]:


mylist.pop()  #pop will remove last element from the list
mylist


# In[40]:


mylist.remove(50) # here we have to specify the data in the list which we have to remove


# In[41]:


del mylist[2] # will delete the element from list according to the index position


# In[42]:


list1=[10,20,300,"hey",11.5]


# In[44]:


#is the input is int we have to append its square


# In[58]:


newlist=[]
for i in list1:
    if(type(i) is int):
        newlist.append(i*i)


# In[59]:


newlist


# In[78]:


armno=str(int(input("Enter the number :")))
ans=0
for i in armno:
    ans=ans+int(i)**len(armno)
if int(armno)==ans:
    print("Armstrong")
else:
    print("Not Armstrong")


# In[85]:


num=154
total=0
x=num
while(num>0):
    rem=num%10
    total+=rem**3
    num=num//10
if total==x:
    print("Armstrong")
else:
    print("Not a Armstrong")

# Question
# take a input from user that is no of days
# I have to samve some Rs every day
# when i reach the next week I have to save double of previous week same with 3
# give the output of how much money he will save in the input days
# In[89]:


# tuple -> collection of elements seprated by commas
# tuples are immutable
# tuples are used when their are fixed no of elements 
# tuples are faster than list
# it is not compulsory to give brackets in tuple
mytuple=10,20
type(mytuple)


# In[92]:


mytuple=mytuple+(60,70)
print(mytuple)   #values are added but after changing the values memory address is changed


# In[93]:


# dictionar --> collection of elements in key:value pair
# key: identifer
# value: data
# orderd collection of elements


# In[ ]:





# In[95]:


mydictionary={10:"Milan",20:"Raj"}
mydictionary


# In[96]:


mydictionary[10]


# In[102]:


# update
mydictionary[10]="Aman"
mydictionary


# In[103]:


# update
mydictionary[30]="Aman"
mydictionary


# In[104]:


x=mydictionary.pop(10)
mydictionary
x


# In[105]:


mydictionary


# In[106]:


x


# In[107]:


# string ==> hello


# In[ ]:





# In[115]:


mydictionar


# In[121]:


10 in mydictionar


# In[122]:


# A string "Milan Kachhawaha", take out the vovels


# In[130]:


mydict={}
for char in "Milan Kachhawaha":
    if (char in "aeiou"):
        if (char not in mydict):
            mydict[char]=1
        else:
            mydict[char]=mydict[char]+1
print(mydict)


# In[137]:


for i in range(1,6):
    for j in range(i,5):
        print(i,end=" ")
    for j in range(1,i+1):
        print(chr(42),end=" ")
    print("")


# In[ ]:




