#!/usr/bin/env python
# coding: utf-8

# 1. Assume below list having temperature in Celsius convert in to Fahrenheit (use lambda function
# with map function)
# Amount = [21,23,18,22,19,34,24,35]

# In[12]:


amount = [21, 23, 18, 22, 19, 34, 24, 35]
fer = list(map(lambda c: (c * 9) / 5 + 32, amount))
print(fer)


# 2. Remove the out of sequence number in below list (sequence is 25 to 40)m
#  [25, 28,26,4000,27, 31, 5,28,29,30,34,8,32,33, 35, 32,37,36, 40,38,39, 95]

# In[18]:


seq=[25, 28,26,4000,27, 31, 5,28,29,30,34,8,32,33, 35, 32,37,36, 40,38,39, 95]
for i in seq:
    if i<25 or i>40:
        seq.remove(i)
print(seq)


# 3. Remove duplicate elements in the list , don’t use “set” function write your own code
#  List = [3,5,2,6,8,3,18,5,3,44,21,4,18,2]

# In[20]:


ele=[3,5,2,6,8,3,18,5,3,44,21,4,18,2]
print("Original list : ",ele)
new=[]
for element in ele:
    if element not in new:
        new.append(element)
print("Unique list : ", new)


# 4. Program should add value to list, if the same number given again don’t add to list (don’t use set)

# In[44]:


ele=int(input("Enter the size of list : "))
list1=[]
for i in range(1,ele+1):
    element=int(input("Enter the element : "))
    if element not in list1:
        list1.append(element)

print("Yout list is : ",list1)


# 5. Write a program to find given string is Palindrome or Not (write a function pass the string to
# function , and get return True if string is Palindrome, return False if string is not Palindrome )

# In[45]:


def palindrome(string):
    if string==string[::-1]:
        return True
    else:
        return False

string=str(input("Enter a string : "))
ans=palindrome(string)
print(ans)


# 6. Write the python program for find the line contains MAC address in the given multiline string
# %DAEMON-3-SNMPD_TRAP_WARM_START: trap_generate_warm: SNMP 0E-2B-56-1C-89-
# 
# Internal Use - Confidential
# 
# 0 trap: warm start
# Feb 22 20:35:07 router1 snmpd[359]:
# %DAEMON-6-SNMPD_THROTTLE_QUEUE_DRAINED: trap_throttle_timer_handler: cleared all
# throttled traps
# Feb 23 07:34:56 3C-21-5A-14-81-0A router1 snmpd[359]: %DAEMON-3-
# SNMPD_TRAP_WARM_START: trap_generate_warm: SNMP trap: warm start
# Feb 23 07:38:19 router1 snmpd[359]: %DAEMON-2-SNMPD_TRAP_COLD_START:

# In[49]:


import re
text = "%DAEMON-3-SNMPD_TRAP_WARM_START: trap_generate_warm: SNMP 0E-2B-56-1C-89-Internal Use - Confidential0 trap: warm startFeb 22 20:35:07 router1 snmpd[359]: %DAEMON-6-SNMPD_THROTTLE_QUEUE_DRAINED: trap_throttle_timer_handler: cleared all throttled traps Feb 23 07:34:56 3C-21-5A-14-81-0A router1 snmpd[359]: %DAEMON-3- SNMPD_TRAP_WARM_START: trap_generate_warm: SNMP trap: warm start Feb 23 07:38:19 router1 snmpd[359]: %DAEMON-2-SNMPD_TRAP_COLD_START:trap_generate_cold: SNMP trap: cold start"

mac_regex = r"[0-9A-F]{2}(?:\-|\:){5}[0-9A-F]{2}"

matches = re.findall(mac_regex, text, re.MULTILINE)

if matches:
    print("Lines containing MAC addresses:")
    for line in matches:
        print(line)
else:
    print("No lines found containing MAC addresses.")


# 7. Write the python program for find the line contains IP address in the given multiline string
# %DAEMON-3-SNMPD_TRAP_WARM_START: trap_generate_warm: 253.67.34.9
# SNMP
# trap: warm start
# Feb 22 20:35:07 router1 snmpd[359]: %DAEMON-6-
# SNMPD_THROTTLE_QUEUE_DRAINED: trap_throttle_timer_handler: cleared
# all
# throttled traps
# Feb 23 07:34:56 router1 snmpd[359]: %DAEMON-3-SNMPD_TRAP_WARM_START:
# trap_generate_warm: 10.145.78.2 SNMP trap: warm
# start
# Feb 23 07:38:19 router1 snmpd[359]: %DAEMON-2-SNMPD_TRAP_COLD_START:
# trap_generate_cold: SNMP trap: cold start

# In[50]:


import re
text = """%DAEMON-3-SNMPD_TRAP_WARM_START: trap_generate_warm: 253.67.34.9
SNMP
trap: warm start
Feb 22 20:35:07 router1 snmpd[359]: %DAEMON-6-
SNMPD_THROTTLE_QUEUE_DRAINED: trap_throttle_timer_handler: cleared
all
throttled traps
Feb 23 07:34:56 router1 snmpd[359]: %DAEMON-3-SNMPD_TRAP_WARM_START:
trap_generate_warm: 10.145.78.2 SNMP trap: warm
start
Feb 23 07:38:19 router1 snmpd[359]: %DAEMON-2-SNMPD_TRAP_COLD_START:
trap_generate_cold: SNMP trap: cold start"""

ip_regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

matches = re.findall(ip_regex, text, re.MULTILINE)

if matches:
    print("Lines containing IP addresses:")
    for line in matches:
        print(line)
else:
    print("No lines found containing IP addresses.")


# 8. open browser --> open inastagram --> insert the values --> sign up to make account

# In[55]:


import webbrowser
import urllib.request
webbrowser.open('http://www.instagram.com/', new=2)


# Question 2
# Create a function which will take a number from a user and one a number is being provided you have to draw the same of messagesn to your friend.

# In[ ]:





# In[ ]:




