import cv2 as cv
import numpy as np
resim=cv.imread("img.png")
cv.imshow("open",resim)

h,w=resim.shape[:2]

x_grad=cv.Sobel(resim,cv.CV_32F,1,0)
y_grad=cv.Sobel(resim,cv.CV_32F,0,1)
# mutlak değer alınır negatif değerler olmaması adına 
x_grad=cv.convertScaleAbs(x_grad)
y_grad=cv.convertScaleAbs(y_grad)

cv.imshow("kizResmi",x_grad)
cv.waitKey(0)
cv.imshow("kizResmi",y_grad)
cv.waitKey(0)

birlestirXY=cv.add(x_grad,y_grad,dtype=cv.CV_16S)
birlestirXY=cv.convertScaleAbs(birlestirXY)
cv.imshow("birlestirXY",birlestirXY)
cv.waitKey(0)
