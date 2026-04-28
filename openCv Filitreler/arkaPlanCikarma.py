import cv2 as cv

# Video kaynağını aç
video_kaynak = cv.VideoCapture("video.mp4")

# MOG2 arka plan çıkarıcı oluştur
arka_plan_cikarici = cv.createBackgroundSubtractorMOG2(history=150, varThreshold=100)# Geçmiş kare sayısı , Ön plan / arka plan ayrım eşiği

while True:
    # Videodan bir kare oku
    okundu_mu, kare = video_kaynak.read()


    # Ön plan maskesini hesapla
    on_plan_maskesi = arka_plan_cikarici.apply(kare)

    # Öğrenilmiş arka plan görüntüsünü al
    arka_plan = arka_plan_cikarici.getBackgroundImage()

    # Görüntüleri ekranda göster
    cv.imshow("orijinal_kare", kare)
    cv.imshow("on_plan_maskesi", on_plan_maskesi)

    # Arka plan hazırsa göster (ilk karelerde None olabilir)
    if arka_plan is not None:
        cv.imshow("arka_plan", arka_plan)

    # Klavye kontrolü (ESC ile çıkış)
    tus = cv.waitKey(10) & 0xff
    if tus == 27:   # ESC
        break

# Kaynakları serbest bırak
video_kaynak.release()
cv.destroyAllWindows()
