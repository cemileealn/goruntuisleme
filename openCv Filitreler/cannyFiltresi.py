import cv2 as cv
import numpy as np

resim=cv.imread("img.png")
cv.imshow("oyuncu ",resim)
cv.waitKey(0)

kenarlar=cv.Canny(resim,100,200)
cv.imshow("edge",kenarlar)
cv.waitKey(0)