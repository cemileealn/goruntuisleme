import cv2 as cv
import numpy as np

resim=cv.imread("img.png")
cv.imshow("lena",resim)
cv.waitKey(0)

gri=cv.cvtColor(resim,cv.COLOR_BGR2GRAY)
cv.imshow("gri",gri)
cv.waitKey(0)

esik,binary=cv.threshold(gri,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)
cv.imshow("binary",binary)
cv.waitKey(0)
print(esik)
