import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    cv2.imshow('x', img)
    cv2.waitKey(1)
