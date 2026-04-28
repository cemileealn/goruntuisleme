import cv2 as cv

# -------------------------------
# Eşikleme fonksiyonu (Otsu)
# -------------------------------
def esikleme_otsu(goruntu):
    # Gürültüyü azalt
    bulanik = cv.GaussianBlur(goruntu, (3, 3), 0)

    # Gri tonlamaya çevir
    gri = cv.cvtColor(bulanik, cv.COLOR_BGR2GRAY)

    # Otsu ile otomatik eşikleme
    esik_degeri, ikili_goruntu = cv.threshold(gri,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)

    cv.imshow("ikili_goruntu", ikili_goruntu)
    return ikili_goruntu


# -------------------------------
# Canny kenar bulma fonksiyonu
# -------------------------------
def canny_kenar(goruntu):
    alt_esik = 100
    ust_esik = alt_esik * 2

    kenarlar = cv.Canny(goruntu, alt_esik, ust_esik)
    cv.imshow("canny_kenarlar", kenarlar)

    return kenarlar


# -------------------------------
# ANA PROGRAM
# -------------------------------
giris_goruntu = cv.imread("img.png")

cv.imshow("giris", giris_goruntu)
cv.waitKey(1)

# Aşamalar
ikili = esikleme_otsu(giris_goruntu)
kenarlar = canny_kenar(giris_goruntu)

# Kontur bulma
konturlar, hiyerarsi = cv.findContours(kenarlar,cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# Konturları çiz
for i in range(len(konturlar)):
    cv.drawContours(giris_goruntu,konturlar,i,(0, 0, 255),1,8)

cv.imshow("konturlar", giris_goruntu)
cv.waitKey(0)
