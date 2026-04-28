import cv2 as cv
import numpy as np

resim=cv.imread("../opencv.png", cv.IMREAD_GRAYSCALE)
cv.imshow("Original", resim)
cv.waitKey(0)
# enküçük ve  enbüyük pisel degerlerını al ve konumlarnı ver

min_deger,max_deger ,min_konum,max_konum=cv.minMaxLoc(resim)

print("mindeger: %.2f , maxdeger: %2f" %( min_deger , max_deger ))

print("minkonum:",min_konum , "maxkonum:",max_konum )

ortalama,stnd_sapma=cv.meanStdDev(resim)
print("stnd_sapma:",stnd_sapma,"ortalama:",ortalama)


resim[np.where(resim<ortalama)]=0 # where kosulu saglayan pıksellerı bulur ve  bu pıksellere ıstenılen komutu uygular
resim[np.where(resim>ortalama)]=255
cv.imshow("Original", resim)
cv.waitKey(0)