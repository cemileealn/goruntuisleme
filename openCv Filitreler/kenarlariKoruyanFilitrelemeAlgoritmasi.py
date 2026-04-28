import cv2 as cv
import numpy as np

resim=cv.imread("img.png")
cv.imshow("kizResmi",resim)


h,w= resim.shape[:2]

yumusatma=cv.edgePreservingFilter(resim,sigma_s=10,sigma_r=0.4,flags=cv.RECURS_FILTER)

yeniGoruntu=np.zeros([h,w*2,3],dtype=resim.dtype)
yeniGoruntu[0:h,0:w,:]=resim  # sol tarafa orjinal goruntu yerlestırılır

yeniGoruntu[0:h,w:2*w,:]=yumusatma #Sağ tarafa filtrelenmiş görüntü yerleştirilir.

yumusatma=cv.resize(yeniGoruntu,(w,h//2))
cv.imshow("kizResmi",yumusatma)


cv.waitKey(0)
cv.destroyAllWindows()
