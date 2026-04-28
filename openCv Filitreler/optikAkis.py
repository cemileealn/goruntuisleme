import cv2 as cv
import numpy as np

# Video kaynağını aç
cap = cv.VideoCapture("video2.mp4")


# İlk kareyi oku
ret, frame1 = cap.read()
if not ret:
    print("Video okunamadı")
    exit()

# İlk kareyi griye çevir
onceki_gri = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)

# HSV görüntü oluştur (akış görselleştirme için)
hsv = np.zeros_like(frame1)
hsv[..., 1] = 255   # Saturation sabit

def dense_optical_flow(hsv, onceki_gri):
    while True:
        ret, frame2 = cap.read()
        if not ret:
            break

        # Yeni kareyi griye çevir
        sonraki_gri = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)

        # Farneback Dense Optical Flow
        flow = cv.calcOpticalFlowFarneback(
            onceki_gri,        # önceki frame
            sonraki_gri,       # sonraki frame
            None,
            0.5,               # pyr_scale
            3,                 # levels
            15,                # winsize
            3,                 # iterations
            5,                 # poly_n
            1.2,               # poly_sigma
            0                  # flags
        )

        # X ve Y akışlarını al
        mag, ang = cv.cartToPolar(flow[..., 0], flow[..., 1])

        # Açıyı renk (Hue) olarak ata
        hsv[..., 0] = ang * 180 / np.pi / 2

        # Büyüklüğü parlaklık (Value) olarak ata
        hsv[..., 2] = cv.normalize(mag, None, 0, 255, cv.NORM_MINMAX)

        # HSV → BGR
        bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

        # Görüntüleri göster
        cv.imshow("dense_optical_flow", bgr)
        cv.imshow("frame", frame2)

        k = cv.waitKey(30) & 0xff
        if k == 27:  # ESC
            break

        # Bir sonraki döngü için güncelle
        onceki_gri = sonraki_gri

    cap.release()
    cv.destroyAllWindows()

# Fonksiyonu çalıştır
dense_optical_flow(hsv, onceki_gri)
