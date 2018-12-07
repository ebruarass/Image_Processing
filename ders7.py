#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#A. 28x28 boyutlarında içeriği 0 ve 1 olan bir matris üretiniz.
#B. A'da üretilen matriste 1'leri içeren MBR dikdörtgeni üreten fonksiyonu yazınız.
#C. Kendisine aktarılan 2 vektörün benzerliğini döndüren fonksiyonu yazınız.
#D. A'da yazılan fonksiyonu kullanarak 100 farklı matris elde edip,1. üretilen ile
#diğerlerini karşılaştırıp, yakınlığını ve benzerliğini listeleyiniz.


# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import random as random

#soru a
def my_create_m():
    return np.random.randint(0,2,(28,28))


# In[2]:


#soru b
def MBR_create_28_by_28_with_0_1(matris_a):
    m=matris_a.shape[0]
    n=matris_a.shape[1]
    x_min=m
    x_max=0    #başlangıç değerleri olası en olumsuz durum
    y_min=n
    y_max=0
    for i in range(m):
        for j in range(n):
            if (matris_a[i,j]==1 and x_min>i):    # resim/matris üzerinden 
                x_min=i                          # x_min, .... güncelleniyor
            if (matris_a[i,j]==1 and x_max<i):
                x_max=i
            if (matris_a[i,j]==1 and y_min>j):
                y_min=j
            if (matris_a[i,j]==1 and y_max<j):
                y_max=j
    return (x_min,x_max,y_min,y_max)


# In[3]:


#soru c
def get_similarity(character_a,character_b):
    m=character_a.shape[0]
    n=character_a.shape[1]
    my_similarity=0
    for i in range(m):
        for j in range(n):
            my_similarity=my_similarity+character_a[i,j]*character_b[i,j] #pixelleri çarpım olarak değilde direk aynı mı farklımı diye kontrol edebilirsin
    return my_similarity


# In[4]:


#soru d
def get_similarity_for_100_characters(kac_karakter=100):
    characters=[]
    for i in range(kac_karakter):
        new_char=my_create_m()
        characters.append(new_char)
    for i in range(kac_karakter):
        benzerlik=get_similarity(characters[0],characters[i])
        print("0 -- "+str(i)+"  ",benzerlik)


# In[5]:


print(my_create_m())
print(MBR_create_28_by_28_with_0_1(my_create_m()))
c_1=my_create_m()
c_2=my_create_m()
print(get_similarity(c_1,c_2))


# In[6]:


#d şıkkı versiyon 2
a=my_create_m()
benzerlik_max=0
c=np.zeros((28,28))
for i in range(100):
    b=my_create_m()
    if(get_similarity(a,b)>benzerlik_max):
        benzerlik_max=get_similarity(a,b)
        c=b
        
print("En Yüksek Benzerlik : ",benzerlik_max)
plt.imshow(a,interpolation='nearest',cmap='gray')
plt.show()
plt.imshow(c,interpolation='nearest',cmap='gray')
plt.show()
    
get_similarity_for_100_characters()
    


# In[ ]:




