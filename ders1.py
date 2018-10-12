#!/usr/bin/env python
# coding: utf-8

# In[1]:


liste=[0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1]

for i in liste:
    print(int(i)+1)
    
for i in range(0,len(liste)):
    liste[i]=liste[i]+1
    
print(liste)


# In[2]:


import random
s=random.randint(2,5)
print(s)


# In[3]:


listee=[]
for i in range(10):
    listee.append(random.randint(0,10))
print(listee)


# In[4]:


test_sayisi=100000
def createArray(s):
    myList=[]
    for i in range(s):
        myList.append(random.randint(0,10))
    return myList


# In[5]:


def printArray(array):
    print(array)


# In[6]:


def incArray(array):
    myList1=[]
    for i in array:
        myList1.append(i+1)
    return myList1


# In[7]:


def createArrayVersion(s):
    myList=np.arrange(s)
    return myList


# In[8]:


dizi_1=createArray(test_sayisi)
printArray(dizi_1)
dizi_2=incArray(dizi_1)
printArray(dizi_2)


# In[9]:


import numpy as np
x=np.arrange(10)
x


# In[10]:


myL=createArrayVersion(test_sayisi)
myL=myL+25
myL[10025]


# In[12]:


import matplotlib.pyplot as plt
image_1=plt.imread("test.jpg")
plt.imshow(image_1)
plt.show()


# In[13]:


image_1.shape
type(image_1)


# In[ ]:




