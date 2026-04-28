import cv2 as cv
import numpy as np

def sablon_bul():

    kaynak = cv.imread("kaynak.png")
    aranan = cv.imread("sablon.png")
    print("Kaynak boyut:", kaynak.shape)
    print("Aranan boyut:", aranan.shape)

    cv.imshow("kaynak", kaynak)
    cv.imshow("aranan", aranan)

    aranan_yukseklik, aranan_genislik = aranan.shape[:2]

    # TM_SQDIFF_NORMED → küçük değer iyi eşleşme
    eslesme_sonucu = cv.matchTemplate(kaynak,aranan,method=cv.TM_SQDIFF_NORMED)

    cv.imshow("eslesme_sonucu", eslesme_sonucu)

    # Küçük değerler eşleşme
    esik = 0.1
    konumlar = np.where(eslesme_sonucu < esik)

    for nokta in zip(*konumlar[::-1]):
        cv.rectangle(kaynak,nokta,(nokta[0] + aranan_genislik, nokta[1] + aranan_yukseklik),(0, 255, 0),2)

    cv.imshow("sonuc", kaynak)


sablon_bul()
cv.waitKey(0)
cv.destroyAllWindows()
