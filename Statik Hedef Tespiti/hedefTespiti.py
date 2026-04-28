import cv2 as cv
import numpy as np

goruntu = cv.VideoCapture("hedefVideo4.mp4")

min_alan = 1000

while True:
    okundu_mu, kare = goruntu.read()
    if not okundu_mu:
        print("goruntu yok")
        break

    gri = cv.cvtColor(kare, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gri, (5, 5), 0)
    binary = cv.adaptiveThreshold(blur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 9, 2)

    konturlar, _ = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for kontur in konturlar:
        alan = cv.contourArea(kontur)

        if alan > min_alan:
            x, y, w, h = cv.boundingRect(kontur)
            cv.rectangle(kare, (x, y), (x + w, y + h), (0, 0,255), 2)

    cv.imshow("kamera", kare)
    cv.imshow("binary", binary)

    if cv.waitKey(1) & 0xFF == 27:
        break

goruntu.release()
cv.destroyAllWindows()
