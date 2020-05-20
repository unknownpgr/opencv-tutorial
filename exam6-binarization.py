import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    img = cv2.resize(img, (320, 240))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.blur(img, (3, 3))
    # Do binarization
    img[img > 128] = 255
    img[img < 129] = 0
    cv2.imshow('myView', img)
    cv2.waitKey(1)
