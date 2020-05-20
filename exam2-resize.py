import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    # Resize image to W,H = 320,240
    img = cv2.resize(img, (320, 240))
    cv2.imshow('myView', img)
    cv2.waitKey(1)
