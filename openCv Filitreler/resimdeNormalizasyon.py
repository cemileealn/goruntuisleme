import cv2 as cv
import numpy as np

resim=cv.imread("img.png")
print(resim.shape)

gri=cv.cvtColor(resim,cv.COLOR_BGR2GRAY)
cv.imshow("Original",gri)
cv.waitKey(0)
print(gri.shape) # tek boyuta düştü suan

gri=np.float32(gri)
print(gri)


# NORM_MİNMAX Güneş / gölge / bulut farklarını dengeler VE Farklı irtifa ve saatlerde çekilen görüntüleri aynı ölçeğe getirir
resim2=np.zeros(gri.shape,dtype=np.float32)
cv.normalize(gri,resim2 ,alpha=0, beta=1.0,norm_type= cv.NORM_MINMAX)
print(resim2)
print(np.uint8(resim2*255))
cv.imshow("normalize",resim2)
cv.waitKey(0)

# NORM_L1 karar verir: Bu bölgede hedef olma ihtimali ne kadar Hangi alan daha önemli?
resim3 = np.zeros(gri.shape, dtype=np.float32)
cv.normalize(gri, resim3, alpha=1.0, beta=0, norm_type=cv.NORM_L1)
print(np.uint8(resim3*255))
cv.imshow("normalize",resim3)
cv.waitKey(0)





