import cv2 as cv
import numpy as np

resim=cv.imread("img.png")

def kose_tespiti(resim):
    gri=cv.cvtColor(resim,cv.COLOR_BGR2GRAY)
    koseler=cv.goodFeaturesToTrack(gri,200,0.05,10)
# 35 max secılecek  kose sayısı SİHA sistemlerinde bu sayı genelde 200–1000 arası olur
# En güçlü köşe değeri Rmax
# Onun %5’i altındaki noktalar elenir.
#Seçilen köşeler arasında minimum mesafe (piksel). Köşelerin üst üste binmesini engellemek

    for nokta in koseler:
        print(nokta)

        mavi=np.random.randint(0,256)
        yesil=np.random.randint(0,256)
        kirmizi=np.random.randint(0,256)

        x=np.int32(nokta[0][0])
        y=np.int32(nokta[0][1])

# cv.circle() komutu görüntü üzerine daire çizmek için kullanılır.
        cv.circle(resim,(x,y),5,(int(mavi), int(yesil), int(kirmizi)),1)
    return resim

yeni_goruntu=kose_tespiti(resim)
cv.imshow("resim",yeni_goruntu)
cv.waitKey(0)