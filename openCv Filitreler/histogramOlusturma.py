import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def gri_histogram(gri):
    h, w = gri.shape
    histogram = np.zeros(256, dtype=np.int32)

    for satir in range(h):
        for sutun in range(w):
            piksel_degeri = gri[satir, sutun]
            histogram[piksel_degeri] += 1

    piksel_degerleri = np.arange(256)

    plt.figure() # grafik penceresi açar
    plt.bar(piksel_degerleri, histogram)  # histogrami cubuk grafiği olarak cizer
    plt.xlabel("Piksel Değeri (0-255)") # garafiğin x eksenını ısımlendırır
    plt.ylabel("Frekans") # grafiğin y eksenini isimlendirir
    plt.title("Gri Seviye Histogramı") # grafik başlığı
    plt.show() # grafiği ekranda gösterir


def renkli_histogram(resim):
    renkler = ('b', 'g', 'r')  # Mavi, Yeşil, Kırmızı

    plt.figure() # yeni grafik penceresi
    for kanal, renk in enumerate(renkler): # kanal 0,1,2 renkleri döner
        histogram = cv.calcHist([resim], [kanal], None, [256], [0, 256]) # hazır hostogram fonksiyonu
        plt.plot(histogram, color=renk) # histogramı cizer

    plt.xlabel("Piksel Değeri")
    plt.ylabel("Frekans")
    plt.title("Renkli Görüntü Histogramı")
    plt.xlim([0, 256]) # x ekseni için sınır belirtir
    plt.show()


# ---- ANA PROGRAM ----
resim = cv.imread("../nesne algılama ve detaylı görüntü analizi/hedef.png")

cv.imshow("Orijinal Resim", resim)
cv.waitKey(0)

gri = cv.cvtColor(resim, cv.COLOR_BGR2GRAY)

gri_histogram(gri)


renkli_histogram(resim)
