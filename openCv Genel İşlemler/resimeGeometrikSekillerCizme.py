import cv2 as cv
import numpy as np

resim=np.zeros((512,512,3),np.uint8)

#KARE
cv.rectangle(resim,(100,100),(300,300),(255,0,0),2,cv.LINE_8,0)

# DAİRE
cv.circle(resim,(256,256),50,(0,0,255),2,cv.LINE_8,0)

#ELİPS
cv.ellipse(resim,(256,256),(150,150),360,0,360,(0,255,0),2,cv.LINE_8,0)

cv.imshow("resim",resim)
cv.waitKey(0)
