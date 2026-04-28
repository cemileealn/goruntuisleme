import cv2 as cv

video = cv.VideoCapture(0)

def videoAnlik(image, opt=1):
    if opt == 0:
        return cv.bitwise_not(image)
    elif opt == 1:
        return cv.GaussianBlur(image, (15,15), 0)
    elif opt == 2:
        return cv.Canny(image, 100, 200)
    else:
        return image

index = 2

while True:
    ret, frame = video.read()
    if not ret:
        break

    result = videoAnlik(frame, index)

    cv.imshow('Orijinal', frame)
    cv.imshow('Islenmis', result)

    c = cv.waitKey(50) & 0xFF

    if c == ord('1'):
        index = 0
    elif c == ord('2'):
        index = 1
    elif c == ord('3'):
        index = 2
    elif c == 27:  # ESC
        break

video.release()
cv.destroyAllWindows()
