import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def gri_histogram(gri_resim):
    h, w = gri_resim.shape
    histogram = np.zeros(256, dtype=np.int32)

    for satir in range(h):
        for sutun in range(w):
            piksel_degeri = gri_resim[satir, sutun]
            histogram[piksel_degeri] += 1

    piksel_degerleri = np.arange(256)

    plt.figure() # grafik penceresi açar
    plt.bar(piksel_degerleri, histogram)  # histogrami cubuk grafiği olarak cizer
    plt.xlabel("Piksel Değeri (0-255)") # garafiğin x eksenını ısımlendırır
    plt.ylabel("Frekans") # grafiğin y eksenini isimlendirir
    plt.title("Gri Seviye Histogramı") # grafik başlığı
    plt.show() # grafiği ekranda gösterir

# ---- ANA PROGRAM ----
orijinal_resim = cv.imread("../nesne algılama ve detaylı görüntü analizi/hedef.png")

cv.imshow("Orijinal Resim", orijinal_resim)
cv.waitKey(0)

gri_resim = cv.cvtColor(orijinal_resim, cv.COLOR_BGR2GRAY)
gri_histogram(gri_resim)

esikleme=cv.equalizeHist(gri_resim)
cv.imshow("Esikleme", esikleme)
cv.waitKey(0)