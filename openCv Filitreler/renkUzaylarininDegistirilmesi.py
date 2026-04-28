import cv2 as cv

resim=cv.imread('img.png')
cv.imshow('resim',resim)


gri=cv.cvtColor(resim,cv.COLOR_BGR2GRAY)
cv.imshow('gri',gri)


hsv=cv.cvtColor(resim,cv.COLOR_BGR2HSV)

cv.imshow('hsv',hsv)


h, s, v = cv.split(hsv)

cv.imshow("Hue", h)
cv.imshow("Saturation", s)
cv.imshow("Value", v)
cv.waitKey(0)
cv.destroyAllWindows()

