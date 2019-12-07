#!/usr/bin/env python
# coding: utf-8
# Write a program which will find all such numbers which are divisible by 7 but are not a multipleof 5, between 2000 and 3200 (both included). The numbers obtained should be printed in acomma-separated sequence on a single line.
# In[1]:


for num in range(2000,3201):
    if num/7 and num/5!=0:
        print(str(num)+',',end="")
        


# Write a Python program to accept the user's first and last name and then getting them printed in
# the the reverse order with a space between first name and last name.

# In[1]:


firstName=input('Enter first name :')
lastName=input('Enter last name :')
print(lastName+" "+firstName)


# Write a Python program to find the volume of a sphere with diameter 12 cm.

# In[2]:


d=12
r=d/2
v=4/3 * 3.14 * r *r * r
print('the volume of a sphere with diameter 12 cm :'+ str(v))


# Write a program which accepts a sequence of comma-separated numbers from console and
# generate a list.

# In[3]:


numbers=input('Enter sequence of comma-separated numbers :')
splitByComma=numbers.split(',')
print(splitByComma)


# In[ ]:




