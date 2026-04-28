import cv2 as cv
import numpy as np

# Görüntüyü oku ve yeniden boyutlandır
gorsel = cv.imread("cicekKiz.jpg")
gorsel = cv.resize(gorsel, (0, 0), fx=0.5, fy=0.5)

# ROI seçimi
cv.imshow("ROI_Secimi", gorsel)
dikdortgen = cv.selectROI("ROI_Secimi", gorsel, False)

# Seçilen bölge
secilen_bolge = gorsel[dikdortgen[1]:dikdortgen[1]+dikdortgen[3], dikdortgen[0]:dikdortgen[0]+dikdortgen[2]]

# Dikdörtgen çizimi
gorsel_kopya = gorsel.copy()
cv.rectangle(gorsel_kopya, (dikdortgen[0], dikdortgen[1]), (dikdortgen[0]+dikdortgen[2], dikdortgen[1]+dikdortgen[3]), (0,255,0), 2)
cv.imshow("Dikdortgen_Gosterim", gorsel_kopya)

# GrabCut için maske ve modeller
maske = np.zeros(gorsel.shape[:2], dtype=np.uint8)
arka_plan_modeli = np.zeros((1, 65), np.float64)
on_plan_modeli = np.zeros((1, 65), np.float64)

# GrabCut (TEK SATIR)
cv.grabCut(gorsel, maske, dikdortgen, arka_plan_modeli, on_plan_modeli, 5, cv.GC_INIT_WITH_RECT)

# Ön plan maskesi
temiz_maske = np.where((maske == cv.GC_FGD) | (maske == cv.GC_PR_FGD), 255, 0).astype("uint8")

# Sonuç
sonuc_gorsel = cv.bitwise_and(gorsel, gorsel, mask=temiz_maske)

# Gösterimler
cv.imshow("Secilen_Bolge", secilen_bolge)
cv.imshow("GrabCut_Sonuc", sonuc_gorsel)

cv.waitKey(0)
cv.destroyAllWindows()
