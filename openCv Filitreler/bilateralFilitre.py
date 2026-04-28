import cv2 as cv
import numpy as np

# BİLATERAL FİLTRE
resim=cv.imread("img.png")
cv.imshow("hedef",resim)
cv.waitKey(0)

h,w=resim.shape[:2]

filtre=cv.bilateralFilter(resim,0,50,10)
cv.imshow("hedef",filtre)


cv.waitKey(0)
cv.destroyAllWindows()