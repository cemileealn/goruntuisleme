import cv2 as cv

resim1 = cv.imread("../nesne algılama ve detaylı görüntü analizi/hedef.png")
resim2 = cv.imread("../nesne algılama ve detaylı görüntü analizi/hedef.png")
resim3 = cv.imread("hulk.jpg")

# Resimler okunmuş mu kontrol (çok önemli)
if resim1 is None or resim2 is None or resim3 is None:
    print("Resimlerden biri okunamadı!")
    exit()

# HSV dönüşümü
hsv1 = cv.cvtColor(resim1, cv.COLOR_BGR2HSV)
hsv2 = cv.cvtColor(resim2, cv.COLOR_BGR2HSV)
hsv3 = cv.cvtColor(resim3, cv.COLOR_BGR2HSV)

# Histogramlar (H ve S kanalları)
hist1 = cv.calcHist([hsv1], [0,1], None, [60,64], [0,180,0,256])
hist2 = cv.calcHist([hsv2], [0,1], None, [60,64], [0,180,0,256])
hist3 = cv.calcHist([hsv3], [0,1], None, [60,64], [0,180,0,256])

# Normalize
cv.normalize(hist1, hist1, 0, 1.0, cv.NORM_MINMAX)
cv.normalize(hist2, hist2, 0, 1.0, cv.NORM_MINMAX)
cv.normalize(hist3, hist3, 0, 1.0, cv.NORM_MINMAX)

# Histogram karşılaştırma
sonuc12 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
sonuc13 = cv.compareHist(hist1, hist3, cv.HISTCMP_CORREL)

print("Hedef - Yeşil benzerliği:", sonuc12)
print("Hedef - Hulk benzerliği:", sonuc13)
