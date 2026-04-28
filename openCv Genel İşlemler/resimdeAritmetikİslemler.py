# !pip install opencv-python

import cv2 as cv
import numpy as np

scr1=cv.imread("../hulk.jpg")
scr2=cv.imread("../hulk.jpg")
h,w,ch = scr1.shape  # boy, genişlik ,kanal(RGB)
print(h,w,ch)

# add metodu ekleme işlemi için kullanılır
birlesmisResim = np.zeros(scr1.shape, scr1.dtype) # scr1  boyutunda ve scr1 tıpınde  0 lardan olusan bır pencere olusturduk
cv.add(scr1,scr2,birlesmisResim) #scr1 ve scr2 birlesmisResim adlı pencerede birleştirdik
cv.imshow("birleşmiş_resım",birlesmisResim)  # resmı ılgılı sayfaya koyduk
cv.waitKey(0)

# subtract metodu cıkarma işlemi için kullanılır
cikarilmisResim=np.zeros(scr1.shape, scr1.dtype)
cv.subtract(scr1,scr2,cikarilmisResim)
cv.imshow("cikarilmis",cikarilmisResim)
cv.waitKey(0)


# carpma metodu olarak multiply  metodu kullanılır
carpilmisResim=np.zeros(scr1.shape, scr1.dtype)
cv.multiply(scr1,scr2,carpilmisResim)
cv.imshow("carpilmis",carpilmisResim)
cv.waitKey(0)


# bölme işlemi için divide metodu kullanılır
bolunmusResim=np.zeros(scr1.shape, scr1.dtype)
cv.divide(scr1,scr2,bolunmusResim)
cv.imshow("bolunmus",bolunmusResim)
cv.waitKey(0)