import cv2 as cv
import numpy as np

resim=cv.imread("img.png")


def kose_tespiti(resim):
    gri = cv.cvtColor(resim, cv.COLOR_BGR2GRAY)
    koseler = cv.goodFeaturesToTrack(gri, 200, 0.05, 10)

    for nokta in koseler:
        print(nokta)

        mavi = np.random.randint(0, 256)
        yesil = np.random.randint(0, 256)
        kirmizi = np.random.randint(0, 256)

        x = np.int32(nokta[0][0])
        y = np.int32(nokta[0][1])

        cv.circle(resim, (x, y), 5, (int(mavi), int(yesil), int(kirmizi)), 1)

    pencere_boyutu=(3,3)  # Arama penceresi boyutu
    kor_bolge=(-1,-1)   # Kör bölge (hesaplama yapılmayacak merkez alan)

    # Durdurma kriterleri
    # 40 iterasyon ya da 0.001 hassasiyete ulaşınca dur
    durdurma=(cv.TERM_CRITERIA_EPS+cv.TERM_CRITERIA_COUNT,40,0.001)

    iyilesen_koseler=cv.cornerSubPix(gri,koseler,pencere_boyutu,kor_bolge,durdurma)

    # Köşeleri yazdırma
    for i in range(iyilesen_koseler.shape[0]):
        print("İyileştirilmiş Köşe [", i, "] (",iyilesen_koseler[i, 0, 0], ",",iyilesen_koseler[i, 0, 1], ")")

    return  resim

yeni_goruntu=kose_tespiti(resim)
cv.imshow("resim",resim)
cv.waitKey(0)











