import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    img = cv2.resize(img, (320, 240))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Blur image with 3x3 filter
    img = cv2.blur(img, (3, 3))
    cv2.imshow('myView', img)
    cv2.waitKey(1)
