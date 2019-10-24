#!/usr/bin/env python
# coding: utf-8

# In[31]:


#Question 1
x = list(range(1,101))


# In[32]:


#Question 2
list(x[:5])


# In[33]:


#Question 3
len(x)


# In[34]:


#Question 4
list(x[-10:])


# In[35]:


#Question 5
list((x[:5], x[-10:]))


# In[159]:


#Question 6
[i for i in x if i%20 == 0]


# In[160]:


#Question 7
list = [90, -5, 870, 20, 400, 1000, 95]
list.sort(reverse = True)
list[0]


# In[161]:


#Question 8
list = [90, -5, 870, 20, 400, 1000, 95]
max = 0
for i in list:
    if i> max:
        max = i
print (max)


# In[162]:


#Question 9
GPA = 3.9
salary = 6430*GPA + 1980
salary


# In[163]:


x = [2.8, 3.4, 3.2, 3.8]
salary = [6430*i + 1980 for i in x]
salary

