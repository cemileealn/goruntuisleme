import cv2 as cv
import numpy as np


# -------------------------------------------------
# CANNY KENAR BULMA (yardımcı fonksiyon)
# -------------------------------------------------
def canny_kenar_bul(goruntu):
    """
    Görüntüden Canny algoritması ile kenarları çıkarır.
    """

    # Görüntüyü griye çevir
    gri = cv.cvtColor(goruntu, cv.COLOR_BGR2GRAY)

    # Canny eşikleri
    alt_esik = 100
    ust_esik = alt_esik * 2

    # Canny kenar bulma
    kenarlar = cv.Canny(gri, alt_esik, ust_esik)

    return kenarlar


# -------------------------------------------------
# ANA PROGRAM
# -------------------------------------------------

# Görüntüyü oku
kaynak_goruntu = cv.imread("resim2.png")
# Okuma kontrolü
if kaynak_goruntu is None:
    print("Görüntü okunamadı!")
    exit()

# Orijinal görüntüyü göster
cv.namedWindow("girdi", cv.WINDOW_AUTOSIZE)
cv.imshow("girdi", kaynak_goruntu)
cv.waitKey(1)

# Kenarları bul
ikili_kenar = canny_kenar_bul(kaynak_goruntu)

cv.imshow("ikili_kenar", ikili_kenar)
cv.waitKey(1)

# -------------------------------------------------
# OLASILIKSAL HOUGH DOĞRU DÖNÜŞÜMÜ
# -------------------------------------------------

dogrular = cv.HoughLinesP(
    ikili_kenar,     # Binary (Canny) görüntü
    1,               # rho çözünürlüğü (piksel)
    np.pi / 180,     # theta çözünürlüğü (1 derece)
    55,              # minimum oy sayısı (threshold)
    None,            # (OpenCV iç kullanımı için)
    50,              # minimum doğru uzunluğu
    10               # maksimum boşluk (gap)
)

# Eğer doğru tespit edildiyse
if dogrular is not None:

    # Tespit edilen her doğru için
    for i in range(len(dogrular)):

        # HoughLinesP çıktısı: [x1, y1, x2, y2]
        x1, y1, x2, y2 = dogrular[i][0]

        # Doğruyu orijinal görüntü üzerine çiz
        cv.line(
            kaynak_goruntu,
            (x1, y1),
            (x2, y2),
            (255, 0, 0),   # Mavi renk (BGR)
            1,             # Çizgi kalınlığı
            cv.LINE_AA     # Yumuşak çizgi
        )

# Sonucu göster
cv.imshow("olasiliksal_hough_dogrulari", kaynak_goruntu)
cv.waitKey(0)
cv.destroyAllWindows()




