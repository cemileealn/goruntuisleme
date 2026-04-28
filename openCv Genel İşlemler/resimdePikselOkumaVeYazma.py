import cv2 as cv

resim=cv.imread("../opencv.png")
resim1=cv.namedWindow("opencv",cv.WINDOW_AUTOSIZE)
cv.imshow("opencv",resim)
cv.waitKey(0)
h,w,ch=resim.shape  #h=satır(yükseklik)  w=sutun(genişlik) ch = kanal sayısı rgb
print(h,w,ch)


for row in range(h): # 0 dan başla ve tum satırları gezer
    for col in range(w): # satırdayken tüm sutunları gezer
        b,g,r=resim[row,col]
        b=255-b  # 255 olanları sıyah renge donusturur
        g=255-g
        r=255-r
        resim[row,col]=b,g,r # değişen rgb renklerını  ılgılı satır ve sutuna atar

cv.imshow("resim",resim)
cv.waitKey(0)
