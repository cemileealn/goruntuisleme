import cv2 as cv
import numpy as np

resim=cv.imread("../opencv.png")

mv=cv.split(resim) # split komutu kanallara ayırı (0,1,2)
mv[0][:, :]=0 # bgr yanı mavi kanalın tum pıksellerını 0 yaptık


yeniResim=cv.merge(mv) # ayrıdıgımız kanlları merge komutuyla tekrar bırlestırıyoruz
cv.imshow("yeni olusan resim",yeniResim)
cv.waitKey(0)