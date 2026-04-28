import cv2 as cv
import numpy as np

resim=cv.imread('../miuul.jpg')
cv.imshow('resim',resim)


satir=resim.shape[0]
sutun=resim.shape[1]

#KAYDIRMA SHİFTED  (ROLL,YAW)
M=np.float32([[1,0,100],[0,1,20]]) # görüntüyü 100 pıksel saga 20 piksel assaği
kaydir=cv.warpAffine(resim,M,(sutun,satir))
cv.imshow('shifted',kaydir)


#DÖNDÜRME  ROTATİON
M1=cv.getRotationMatrix2D((sutun/2,satir/2),90,1)
dondur=cv.warpAffine(resim,M1,(sutun,satir))
cv.imshow('dondur',dondur)


# BÜYÜTME KÜÇÜLTME SCALİNG
kucult=cv.resize(resim,None,fx=0.3,fy=0.3,interpolation=cv.INTER_NEAREST)  #fx ve fy sıfırdan küçük seçilirse küçültme sıfırdan büyük seçilirse büyütme işlemi yapılır
cv.imshow('kucult',kucult)
cv.waitKey(0)













cv.waitKey(0)

