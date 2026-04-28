import cv2 as cv
import numpy as np

video_kaynak = cv.VideoCapture("video2.mp4")

arka_plan_cikarici = cv.createBackgroundSubtractorMOG2(
    history=150,
    varThreshold=100
)

def isleme(kare, on_plan_maskesi):

    yapi_elemani = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    on_plan_maskesi = cv.morphologyEx(on_plan_maskesi, cv.MORPH_OPEN, yapi_elemani)

    konturlar, _ = cv.findContours(
        on_plan_maskesi,
        cv.RETR_EXTERNAL,
        cv.CHAIN_APPROX_SIMPLE
    )

    for kontur in konturlar:
        alan = cv.contourArea(kontur)

        if alan < 1500:
            continue

        donen_dikdortgen = cv.minAreaRect(kontur)
        koseler = cv.boxPoints(donen_dikdortgen)
        koseler = np.int32(koseler)

        cv.polylines(kare, [koseler], True, (0, 0, 255), 2)

    return kare


while True:
    okundu_mu, kare = video_kaynak.read()
    if not okundu_mu:
        break

    on_plan_maskesi = arka_plan_cikarici.apply(kare)

    sonuc = isleme(kare, on_plan_maskesi)

    cv.imshow("kare", kare)
    cv.imshow("on_plan", on_plan_maskesi)
    cv.imshow("sonuc", sonuc)

    tus = cv.waitKey(30) & 0xFF
    if tus == 27:
        break

video_kaynak.release()
cv.destroyAllWindows()
