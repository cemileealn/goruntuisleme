import cv2 as cv
import numpy as np

# -----------------------------
# Video dosyasını okuma modunda açar
# -----------------------------
video = cv.VideoCapture("../video.mp4")

# Video karelerinin yüksekliğini alır (pixel cinsinden)
yukseklik = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))

# Video karelerinin genişliğini alır (pixel cinsinden)
genislik = int(video.get(cv.CAP_PROP_FRAME_WIDTH))

# Videonun saniyedeki kare sayısını (FPS) alır
fps = video.get(cv.CAP_PROP_FPS)

# -----------------------------
# Video yazmak için codec (sıkıştırma formatı) belirlenir
# DIVX: Windows için yaygın ve stabil
# -----------------------------
fourcc = cv.VideoWriter_fourcc('D', 'I', 'V', 'X')

# -----------------------------
# VideoWriter: yeni bir video dosyası oluşturur
# Parametreler:
# 1) Dosya adı
# 2) Codec
# 3) FPS
# 4) Frame boyutu (genişlik, yükseklik)
# 5) Renkli mi? (True = renkli)
# -----------------------------
oku = cv.VideoWriter("../video_out.mp4", fourcc, fps, (genislik, yukseklik), True)

# -----------------------------
# Video bitene kadar kare kare oku
# -----------------------------
while True:

    # Videodan bir kare okur
    # ret: okuma başarılı mı?
    # frame: okunan görüntü
    ret, frame = video.read()

    # Eğer kare okunamadıysa (video bittiysa) döngüden çık
    if not ret:
        break

    # Okunan kareyi ekranda gösterir
    cv.imshow("Original", frame)

    # Okunan kareyi yeni video dosyasına yazar
    oku.write(frame)

    # 30 ms bekler, ESC (27) basılırsa çık
    if cv.waitKey(30) == 27:
        break

# -----------------------------
# Video okuma kaynağını serbest bırakır
# AÇIKLAMA:
# - Video dosyasıyla olan bağlantıyı kapatır
# - Bellekte tutulan kaynakları boşaltır
# - Bunu yapmazsan dosya kilitli kalabilir
# -----------------------------
video.release()

# -----------------------------
# Video yazma işlemini sonlandırır
# AÇIKLAMA:
# - Video dosyasının düzgün şekilde kaydedilmesini sağlar
# - Header bilgileri tamamlanır
# - Aksi halde video bozuk olabilir
# -----------------------------
oku.release()

# -----------------------------
# Açılmış tüm OpenCV pencerelerini kapatır
# AÇIKLAMA:
# - imshow ile açılan pencereleri temizler
# - Bellek sızıntısını önler
# -----------------------------
cv.destroyAllWindows()
