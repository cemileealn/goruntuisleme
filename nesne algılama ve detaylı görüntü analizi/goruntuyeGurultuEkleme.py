import cv2 as cv
import numpy as np

resim = cv.imread("opencv.png")

if resim is None:
    print("Görüntü okunamadı")
    exit()

def tuz_biber(resim):
    h, w = resim.shape[:2]

    oran = 0.05
    gurultu = int(h * w * oran)

    satir = np.random.randint(0, h, gurultu)
    sutun = np.random.randint(0, w, gurultu)

    for i in range(gurultu):
        if i % 2 == 1:
            resim[satir[i], sutun[i]] = (255, 255, 255)
        else:
            resim[satir[i], sutun[i]] = (0, 0, 0)

    return resim

h, w = resim.shape[:2]

kopya = resim.copy()
kopya = tuz_biber(kopya)

yeniGoruntu = np.zeros((h, w*2, 3), dtype=resim.dtype)

yeniGoruntu[0:h, 0:w, :] = resim
yeniGoruntu[0:h, w:2*w, :] = kopya

cv.imshow("hedef", yeniGoruntu)
cv.waitKey(0)
cv.destroyAllWindows()
