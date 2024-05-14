#!/usr/bin/env python
# coding: utf-8

# 1. Define a function generate_n_chars() that takes an integer n and a character c and returns a string, n
# characters long, consisting only of c:s. For example, generate_n_chars(5,"x") should return the string
# "xxxxx". (Python is unusual in that you can actually write an expression 5 * "x" that will evaluate to
# "xxxxx". For the sake of the exercise you should ignore that the problem can be solved in this
# manner.)

# In[3]:


def generate_n_chars(n,s):
    for i in range(1,n+1):
        print("x",end="")

n=int(input("Enter the integer : "))
s=str(input("Enter a string : "))
generate_n_chars(n,s)


# 2. The function max() from exercise 1) and the function max_of_three() from exercise 2) will only
# work for two and three numbers, respectively. But suppose we have a much larger number of
# numbers, or suppose we cannot tell in advance how many they are? Write a function max_in_list()
# that takes a list of numbers and returns the largest one.

# In[4]:


def max_in_list(list1):
    highest=list1[0]
    for x in list1:
        if x>highest:
            highest=x
    return highest

list1=[]
x=int(input("Enter the count of numbers you want to enter : "))
for i in range(1,x+1):
    y=int(input("Enter the value :"))
    list1.append(y)

print("Max no",max_in_list(list1))


# 3. Write a program that maps a list of words into a list of integers representing the lengths of the
# correponding words.

# In[1]:


words=["apple","banana","Milan","Regex","Scoobe-Do"]
word_length=[len(word) for word in words]
print(word_length)


# 4. Write a function find_longest_word() that takes a list of words and returns the length of the longest
# one. Modify the same to do with lambda expression.

# In[19]:


def find_longest_word():
    n=int(input("Enter the length of list : "))
    list1=list(map(lambda list1:(for i in range(1,n+1))))
    for i in range(1,n+1):
        a=str(input(f"Enter the string {i} : "))
        list1.append(a)
    longest_word=0
    for word in list1:
        if len(word)>longest_word:
            longest_word=len(word)
    return longest_word

longest_word_length = find_longest_word()
print(f"The length of the longest word is: {longest_word_length}")


# In[26]:


def find_longest_word():
    list1 = [str(input(f"Enter element {i+1}: ")) for i in range(int(input("Enter the length of list : ")))]
    longest_word=0
    
    '''for word in list1:
        if len(word)>longest_word:
            longest_word=len(word)
    return longest_word'''

longest_word_length = find_longest_word()
print(f"The length of the longest word is: {longest_word_length}")


# 6. Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a
# salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa
# Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori",
# "Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and
# spacing are usually ignored.

# In[ ]:





# 7. A pangram is a sentence that contains all the letters of the English alphabet at least once, for
# example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to check
# a sentence to see if it is a pangram or not.

# In[ ]:




