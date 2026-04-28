import cv2 as cv
import numpy as np

# -------------------------------------------------
# CANNY KENAR BULMA FONKSİYONU
# -------------------------------------------------
def canny_kenar(goruntu):
    """
    Giriş görüntüsünden Canny algoritması ile kenarları çıkarır.
    """

    # Renkli (BGR) görüntüyü gri seviyeye çeviriyoruz
    # Çünkü Canny tek kanallı (grayscale) görüntü ile çalışır
    gri = cv.cvtColor(goruntu, cv.COLOR_BGR2GRAY)

    # Alt eşik (zayıf kenar eşiği)
    alt_esik = 100

    # Üst eşik (güçlü kenar eşiği)
    # Genellikle alt eşik * 2 olarak seçilir
    ust_esik = alt_esik * 2

    # Canny kenar algılama
    # Giriş: gri görüntü
    # Çıkış: binary (0-255) kenar görüntüsü
    kenarlar = cv.Canny(gri, alt_esik, ust_esik)

    # Kenar görüntüsünü ekranda göster
    cv.imshow("canny_kenarlar", kenarlar)

    # Kenar görüntüsünü geri döndür
    return kenarlar


# -------------------------------------------------
# HOUGH DOĞRU ÇİZGİ TESPİTİ VE ÇİZME FONKSİYONU
# -------------------------------------------------
def hough_dogru_ciz(kenar_goruntu, cizim_goruntusu):
    """
    Canny ile elde edilmiş kenar görüntüsü üzerinde
    Hough Transform kullanarak doğruları tespit eder
    ve bu doğruları verilen görüntü üzerine çizer.
    """

    # Hough Doğru Dönüşümü
    # kenar_goruntu : Binary kenar görüntüsü
    # 1             : rho çözünürlüğü (piksel)
    # np.pi / 180   : theta çözünürlüğü (1 derece)
    # 150           : eşik (kaç oy alan doğru kabul edilecek)
    dogrular = cv.HoughLines(kenar_goruntu,1,np.pi / 180,150)

    # Eğer en az bir doğru tespit edildiyse
    if dogrular is not None:

        # Tespit edilen her doğru için döngü
        for i in range(len(dogrular)):

            # Hough çıktısından rho ve theta değerlerini al
            rho = dogrular[i][0][0]     # Orijine uzaklık
            theta = dogrular[i][0][1]   # Açısal değer (radyan)

            # Kutupsal koordinatları Kartezyen'e çevirmek için
            a = np.cos(theta)
            b = np.sin(theta)

            # Doğru üzerindeki orijine en yakın nokta
            x0 = a * rho
            y0 = b * rho

            # Doğruyu görüntü boyunca uzatmak için iki uç nokta
            nokta1 = (
                int(x0 + 1000 * (-b)),
                int(y0 + 1000 * (a))
            )

            nokta2 = (
                int(x0 - 1000 * (-b)),
                int(y0 - 1000 * (a))
            )

            # Hesaplanan iki nokta arasına doğru çiz
            # (0,0,255) : kırmızı renk (BGR)
            # 1         : çizgi kalınlığı
            # cv.LINE_AA: anti-aliasing (yumuşak çizgi)
            cv.line(cizim_goruntusu,nokta1,nokta2,(0, 0, 255),1,cv.LINE_AA)


# -------------------------------------------------
# ANA PROGRAM
# -------------------------------------------------

# Görüntüyü dosyadan oku
resim = cv.imread("img.png")

# Görüntü okunamazsa programı durdur
if resim is None:
    print("Resim okunamadı!")
    exit()

# Orijinal görüntüyü göster
cv.imshow("orijinal", resim)
cv.waitKey(1)

# Canny fonksiyonu ile kenarları bul
kenarlar = canny_kenar(resim)
cv.waitKey(1)

# Hough Transform ile doğruları tespit et ve çiz
hough_dogru_ciz(kenarlar, resim)

# Sonuç görüntüsünü göster
cv.imshow("sonuc", resim)

# Bir tuşa basılana kadar bekle
cv.waitKey(0)

# Tüm OpenCV pencerelerini kapat
cv.destroyAllWindows()
