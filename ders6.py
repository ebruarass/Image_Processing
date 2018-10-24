#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy import stats
from scipy.stats import iqr
from scipy.stats import skew

image= plt.imread("test.jpg")
plt.imshow(image)
plt.show()


# In[2]:


def get_distance(v,w=[1/3,1/3,1/3]):
    a,b,c=v[0],v[1],v[2]
    w1,w2,w3=w[0],w[1],w[2]
    d=((a**2)*w1+(b**2)*w2+(c**2)*w3)**.5
    return d


# In[3]:


def convert_rgb_to_gray_level(im_1):
    m=im_1.shape[0]
    n=im_1.shape[1]
    im2=np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            im2[i,j]=get_distance(im_1[i,j,:])
            
    return im2 
image1=convert_rgb_to_gray_level(image)
plt.imshow(image1,cmap="gray")
plt.show()


# In[4]:


def convert_gray_level_to_BW(grey_level_1):
    m=grey_level_1.shape[0]
    n=grey_level_1.shape[1]
    im_bw=np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if grey_level_1[i,j]>0:
                im_bw[i,j]=1
            else:
                im_bw[i,j]=0
            
    return im_bw

image2=convert_gray_level_to_BW(image1)
plt.imshow(image2,cmap="gray")
plt.show()


# In[5]:


def pixel_external(part_of_image):
    part_of_image= part_of_image.ravel()
    one=0
    zero=0
    for i in part_of_image:
        if(i==1):
            one=one+1
        else:
            zero=zero+1
    
    if(one==3 and zero==1):
        return True
    else:
        return False


# In[6]:


def pixel_internal(part_of_image):
    part_of_image= part_of_image.ravel()
    one=0
    zero=0
    
    for i in part_of_image:
        if(i==1):
            one=one+1
        else:
            zero=zero+1
    
    if(one==1 and zero==3):
        return True
    else:
        return False


# In[7]:


def function(image2):
    E,I=0,0
    m=image2.shape[0]
    n=image2.shape[1]
    
    for l in range(1,m-1):
        for p in range(1,n-1):
            if(pixel_external(image2[l-1:l+1,p-1:p+1])):
                E=E+1
            if(pixel_internal(image2[l-1:l+1,p-1:p+1])):
                I=I+1
         
        
    print(E)
    print(I)
    return((E-I)/4)
function(image2)   


# In[ ]:




