import cv2
import cv2 as cv
import numpy as np


resim=cv.imread("sp.jpg")


matris=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]] , dtype="float32")
matris_resim=cv.filter2D(resim,cv2.CV_32F,matris)
matris_resim=cv.convertScaleAbs(matris_resim)

cv.imshow("resim",matris_resim)
cv.waitKey(0)
cv.destroyAllWindows()


