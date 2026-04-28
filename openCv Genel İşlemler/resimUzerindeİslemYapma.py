import cv2 as cv
import numpy as np

resim1=cv.imread("../hulk3.jpg")

cv.namedWindow("resim",cv.WINDOW_NORMAL)
cv.imshow("resim",resim1)
cv.waitKey(0)
print(resim1.shape)


m1=np.copy(resim1)
m2=resim1

resim1[10:60, 10:60] = (0,0,0)  # y eksenı assagı yukarı (10 satırsan başla 60 satıra kadar git) : x eksenı sag sol (10 sutundan basla 60. sutuna kadar gıt )= renk aralıgı

cv.imshow("resim1",resim1)
cv.waitKey(0)