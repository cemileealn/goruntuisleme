import cv2 as cv
import numpy as np

resim11 = cv.imread("../nesne algılama ve detaylı görüntü analizi/sp.jpg")
resim22 = cv.imread("sp2.jpg")


cv.imshow("resim11",resim11)
cv.waitKey(0)

cv.imshow("resim22",resim22)
cv.waitKey(0)
# Eğer boyutlar farklıysa önce yanı boyuta getiririz :
resim22 = cv.resize(resim22, (resim11.shape[1], resim11.shape[0]))

birlesenResim = np.hstack((resim11, resim22))

cv.imshow("Birlestirilmis Resim", birlesenResim)
cv.waitKey(0)
cv.destroyAllWindows()
