#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy import stats
from scipy.stats import iqr
from scipy.stats import skew

image_1=plt.imread("test.jpg")
plt.imshow(image_1)
plt.show()


# In[2]:


import os
cwd=os.getcwd()
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def reverse(x):
    return 255-x

image_1[:,:,0]=reverse(image_1[:,:,0])
image_1[:,:,1]=reverse(image_1[:,:,1])
image_1[:,:,2]=reverse(image_1[:,:,2])

plt.imshow(image_1)
plt.show()


# In[3]:


def histogram(image):
    h1={}
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if(image[i,j,0] in h1.keys()):
                h1[image[i,j,0]]+=1
            else:
                h1[image[i,j,0]]=1
                
    h2={}
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if(image[i,j,1] in h2.keys()):
                h2[image[i,j,1]]+=1
            else:
                h2[image[i,j,1]]=1
                
    h3={}
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if(image[i,j,2] in h3.keys()):
                h3[image[i,j,2]]+=1
            else:
                h3[image[i,j,2]]=1
                
    plt.bar(list(h1.keys()),h1.values(),color='r')
    plt.show()
    plt.bar(list(h2.keys()),h2.values(),color='g')
    plt.show()
    plt.bar(list(h3.keys()),h3.values(),color='b')
    plt.show()
    
histogram(image_1)
    


# In[4]:


def hesapla(image_1):
    print("Renk ortalamasi:")
    print("Kirmizi icin renk ortalamasi:",image_1[:,:,0].mean())
    print("Yesil icin renk ortalamasi:",image_1[:,:,1].mean())
    print("Mavi icin renk ortalamasi:",image_1[:,:,2].mean())
    
    print("Ortanca degerler:")
    print("Kirmizi icin ortanca deger:",np.median(image_1[:,:,0]))
    print("Yesil icin ortanca deger:",np.median(image_1[:,:,1]))
    print("Mavi icin ortanca deger:",np.median(image_1[:,:,2]))
    
    print("Renk modlari:")
    print("Kirmizi icin renk modu:",stats.mode(image_1[:,:,0]))
    print("Yesil icin renk modu:",stats.mode(image_1[:,:,1]))
    print("Mavi icin renk modu:",stats.mode(image_1[:,:,2]))
    
    print("Ceyreklikler:")
    print("Kirmizi icin Q1 degeri:",np.percentile(image_1[:,:,0],25))
    print("Kirmizi icin Q2 degeri:",np.percentile(image_1[:,:,0],50))
    print("Kirmizi icin Q3 degeri:",np.percentile(image_1[:,:,0],75))
    
    print("Yesil icin Q1 degeri:",np.percentile(image_1[:,:,1],25))
    print("Yesil icin Q2 degeri:",np.percentile(image_1[:,:,1],50))
    print("Yesil icin Q3 degeri:",np.percentile(image_1[:,:,1],75))
    
    print("Mavi icin Q1 degeri:",np.percentile(image_1[:,:,2],25))
    print("Mavi icin Q2 degeri:",np.percentile(image_1[:,:,2],50))
    print("Mavi icin Q3 degeri:",np.percentile(image_1[:,:,2],75))
    
    print("IQR degerleri:")
    print("Kirmizi icin IQR degeri:",iqr(image_1[:,:,0]))
    print("Yesil icin IQR degeri:",iqr(image_1[:,:,1]))
    print("Mavi icin IQR degeri:",iqr(image_1[:,:,2]))
    
    print("Skewness degerleri:")
    print("Kirmizi icin skewness degeri:",skew(image_1[:,:,0]))
    print("Yesil icin skewness degeri:",skew(image_1[:,:,1]))
    print("Mavi icin skewness degeri:",skew(image_1[:,:,2]))
    
    print("Range araliklari:")
    print("Kirmizi icin range aralıgı",image_1[:,:,0].max()-image_1[:,:,0].min())
    print("Yesil icin range aralıgı",image_1[:,:,1].max()-image_1[:,:,1].min())
    print("Mavi icin range aralıgı",image_1[:,:,2].max()-image_1[:,:,2].min())
    
hesapla(image_1)
    
    


# In[ ]:




