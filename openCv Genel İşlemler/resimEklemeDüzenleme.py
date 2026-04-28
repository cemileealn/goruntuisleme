# !pip install opencv-python
import cv2 as cv

resim = cv.imread("../lenna.jpg") # adrestekı gorselı resım degıskenıne yukler

print(type(resim))  #değişkenin tipini yazdırır

cv.namedWindow("opencv_test",cv.WINDOW_AUTOSIZE) # ekranda opencv_test adında bir pencere açar. WINDOW_AUTOSIZE pencere boyutunu resmın boyutune gore ayarlar
cv.imshow("opencv_test",resim)  #oluşturduğumuz "opencv_test" adlı pencerenin içine resimi koyar
cv.waitKey(0) # resmın  mılısanıye cınsınden ekranda gosterılme sanıyesı 0 olursa suresız durur
# cv.destroyAllWindows() # açıkta olan tüm opencv pencerelerini kapatır



resim2=cv.applyColorMap(resim, cv.COLORMAP_SUMMER) # belirtilen resmin Üzerine hazır bir renk şablonu uygular
cv.imshow("opencv_test",resim2)
cv.waitKey(0)



gray=cv.cvtColor(resim, cv.COLOR_BGR2GRAY) # görseli griye döndurur
cv.imshow("opencv_test",gray)
cv.waitKey(0)
cv.imwrite("../lenna.jpg", gray) # kaydetmek ıcın kullanılır



resimg = cv.imread("../lenna.jpg", cv.IMREAD_GRAYSCALE) # istersek gorselı dırekt gri seviyede de de degişkene atayabiliriz
cv.namedWindow("opencv_test",cv.WINDOW_AUTOSIZE)
cv.imshow("lenna.jpg",resimg)
cv.waitKey(0)





