import cv2 as cv
import numpy as np

resim=cv.imread("../lenna.jpg")
cv.imshow("lenna",resim)
cv.waitKey(0)

# X eksenıne göre döndürme

dondur_x=cv.flip(resim,0)
cv.imshow("dondur",dondur_x)
cv.waitKey(0)

# Y eksenine göre döndürme
dondur_y=cv.flip(resim,1)
cv.imshow("dondur",dondur_y)
cv.waitKey(0)

# X ve Y eksenine göre döndürme
dondur_xy=cv.flip(resim,-1)
cv.imshow("dondur",dondur_xy)
cv.waitKey(0)