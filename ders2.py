#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import matplotlib.image mpimg
import numpy as np
img=mpimg.imread("test.jpg")
get_ipython().run_line_magic('matpoltlib', 'inline')
plt.imshow(img)

def myFunction1(myImage):
    print("Eksen sayisi:",myImage.ndim)
    print("Eksen degerleri:",myImage.shape)
    
    print("En kucuk kirmizi renk degeri:",np.min(myImage[:,:,0]))
    print("En buyuk kirmizi renk degeri:",np.max(myImage[:,:,0]))
    
    print("En kucuk yesil renk degeri:",np.min(myImage[:,:,1]))
    print("En buyuk yesil renk degeri:",np.max(myImage[:,:,1]))
    
    print("En kucuk mavi renk degeri:",np.min(myImage[:,:,2]))
    print("En buyuk mavi renk degeri:",np.max(myImage[:,:,2]))
    
myFunction1(img)


# In[ ]:





# In[ ]:




