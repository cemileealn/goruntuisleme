import cv2 as cv

 # resimdeki insanaları tespıt etmekte kullanılır

resim=cv.imread("insan.jpg")
hog=cv.HOGDescriptor()

hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

kutu,agirlik=hog.detectMultiScale(resim,winStride=(4,4),padding=(8,8),scale=1.25)
for (x,y,genislik,yukseklik) in kutu:
    cv.rectangle(resim,(x,y),(x+genislik,y+yukseklik),(0,255,0),2)

cv.imshow("resim",resim)
cv.waitKey(0)
