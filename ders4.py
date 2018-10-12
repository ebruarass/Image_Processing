#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy import stats
from scipy.stats import iqr
from scipy.stats import skew

image=plt.imread("test.jpg")
plt.imshow(image)
plt.show()


# In[3]:


from math import sqrt
def grey_level(image):
    m,n=(image.shape[0],image.shape[1])
    image_grey_level=image
    for i in range(m):
        for j in range(n):
            image_grey_level[i,j]=sqrt(image[i,j,0]**2+image[i,j,1]**2+image[i,j,2]**2)
        plt.imshow(image_grey_level)
        plt.show()
grey_level(image)


# In[5]:


def get_distance(v,w=[1/3,1/3,1/3]):
    a,b,c=v[0],v[1],v[2]
    w1,w2,w3=w[0],w[1],w[2]
    d=((a**2)*w1+(b**2)*w2+(c**2)*w3)**.5
    return d


# In[6]:


my_RGB=[1,2,3]
grey_level=get_distance(my_RGB)
print(grey_level)


# In[7]:


my_RGB=[10,20,3]
grey_level=get_distance(my_RGB,[.6,.3,.1])
print(grey_level)


# In[8]:


def convert_rgb_to_grey_level(im_1):
    m=im_1.shape[0]
    n=im_1.shape[1]
    im2=np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            im2[i,j]=get_distance(im_1[i,j,:])
    return im2
plt.imshow(image)
plt.show()


# In[9]:


plt.imshow(image,cmap="gray")
plt.show()


# In[10]:


def convert_gray_level_to_bw(grey_level_1):
    m=grey_level_1.shape[0]
    n=grey_level_1.shape[1]
    im_bw=np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if grey_level_1[i,j]>120:
                im_bw[i,j]=1
            else:
                im_bw[i,j]=0
    return im_bw


# In[11]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
im1=mpimg.imread("test.jpg")
im2=convert_rgb_to_gray_level(image)
im3=convert_gray_level_to_bw(im2)
plt.subplot(1,3,1),plt.imshow(im1)
plt.subplot(1,3,1),plt.imshow(im2,cmap='gray')
plt.subplot(1,3,1),plt.imshow(im3,cmap='gray')


# In[ ]:




