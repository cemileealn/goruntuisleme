import cv2 as cv
import numpy as np

# 1) Görüntüyü oku (video ise frame olarak düşün)
goruntu = cv.imread("img.png")

# Kontrol
if goruntu is None:
    print("Görüntü okunamadı")
    exit()

# 2) Gri seviye
gri = cv.cvtColor(goruntu, cv.COLOR_BGR2GRAY)

# 3) Gürültü azaltma (sahada şart)
gri = cv.GaussianBlur(gri, (5, 5), 0)

# 4) Adaptif eşikleme (asıl kritik adım)
binary = cv.adaptiveThreshold(gri,255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2    )

# 5) Küçük gürültüleri temizleme
kernel = np.ones((3, 3), np.uint8)
binary = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)

# 6) Sonuçları göster
cv.imshow("Orijinal", goruntu)
cv.imshow("Gri", gri)
cv.imshow("Adaptif Threshold", binary)

cv.waitKey(0)
cv.destroyAllWindows()
