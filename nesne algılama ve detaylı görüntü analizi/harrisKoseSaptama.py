import cv2 as cv
import numpy as np

resim = cv.imread("img.png")

def harris(goruntu):

    blok_boyu = 2
    kernel_boyu = 3
    k_degeri = 0.04

    gri = cv.cvtColor(goruntu, cv.COLOR_BGR2GRAY)
    gri = np.float32(gri)

    harris_sonuc = cv.cornerHarris(gri, blok_boyu, kernel_boyu, k_degeri)

    esik = 0.01 * harris_sonuc.max()

    goruntu[harris_sonuc > esik] = [0, 255, 0]

    return goruntu

yeni_sonuc = harris(resim)

cv.imshow("yeni", yeni_sonuc)
cv.waitKey(0)
cv.destroyAllWindows()
