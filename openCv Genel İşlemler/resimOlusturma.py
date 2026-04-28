from turtledemo.penrose import start

import cv2 as cv
import numpy as np

img = np.ones((550, 770, 3)) # 550 satır 770 sutundan 1lerden oluşan bir görsel oluşturduk

# Renkler (BGR)
mor    = (255,0,255)
siyah  = (0,0,0)
yesil    = (0,255,0)
mavi   = (255,0,0)
kirmizi= (0,0,255)
sari   = (0,255,255)

# Dikdörtgenler
cv.rectangle(img,(100,250),(480,450),mor,3) # (x,y)soldan saga 100-480 arası yanı  380 pıksel assagından yukarıya 250-450 arası yanı  200 pıksel
cv.rectangle(img,(200,150),(580,350),siyah,3)

# Bağlantı çizgileri
cv.line(img,(100,450),(200,350),yesil,2)
cv.line(img,(480,250),(580,150),mavi,2)
cv.line(img,(100,250),(200,150),kirmizi,2)
cv.line(img,(480,450),(580,350),sari,2)


başla=(150,100)
font_thickness=2
fony_size=1
font=cv.FONT_HERSHEY_SIMPLEX

cv.putText(img,"olusan dikdortgen resmi",başla,font,fony_size,font_thickness)
cv.imshow("dikdörtgen",img)
cv.waitKey(0)



