import cv2 as cv

resim = cv.imread("miuul.jpg")
cv.imshow("resim", resim)

h, w = resim.shape[:2] # 0. indeksten başla 2. indekse kadar al 
print(h, w)

kopya = resim.copy()

secme = kopya[75:100, 200:300, :]

print(secme.shape[:2])

cv.imshow("secme", secme)
cv.waitKey(0)
cv.destroyAllWindows()