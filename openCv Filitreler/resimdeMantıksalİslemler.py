import cv2 as cv
import numpy as np

resim="lenna.jpg"

scr1= np.zeros(shape=[400,400,3],dtype=np.uint8)
scr1[100:200,100:200,1]=255
scr1[100:200,100:200,2]=255
cv.imshow("lenna",scr1)
cv.waitKey(0)


scr2= np.zeros(shape=[400,400,3],dtype=np.uint8)
scr2[150:250,150:250,2]=255
cv.imshow("lenna",scr2)
cv.waitKey(0)


# AND operatörü
andgoruntu=cv.bitwise_and(scr1,scr2)
cv.imshow("andgoruntu",andgoruntu)
cv.waitKey(0)

# OR operatörü
orGoruntu=cv.bitwise_or(scr1,scr2)
cv.imshow("orGoruntu",orGoruntu)
cv.waitKey(0)

# XOR operatoru
xorGoruntu=cv.bitwise_xor(scr1,scr2)
cv.imshow("xorGoruntu",xorGoruntu)
cv.waitKey(0)

# DEĞİL operatoru
resim2=cv.imread("../lenna.jpg")
cv.namedWindow("resim2",cv.WINDOW_NORMAL)
cv.imshow("resim2",resim2)
cv.waitKey(0)
degilgoruntu=cv.bitwise_not(resim2)
cv.imshow("degilgoruntu",degilgoruntu)
cv.waitKey(0)

