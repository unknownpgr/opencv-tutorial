import cv2
import math

cap = cv2.VideoCapture(0)

while True:
    ret, org = cap.read()
    # Backup original image
    org = cv2.resize(org, (320, 240))
    img = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
    img = cv2.blur(img, (3, 3))
    img = cv2.Canny(img, 50, 150)

    # Detect lines
    # img           = source image
    # 1             = resolution of parameter rho
    # 3.1415 / 180  = resolution of paramter theta in radian
    # 70            = threshold of line detection
    lines = cv2.HoughLines(img, 1, 3.1415 / 180, 70)

    # Loop for every detected line
    if lines is not None:
        for i in range(0, len(lines)):
            # Convert point from polar coordinate to euclidean coordinate
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
        
            # Draw lines on original image
            cv2.line(org, pt1, pt2, (0, 0, 255), 3, cv2.LINE_AA)

    # Show original image
    cv2.imshow('myView', org)
    cv2.waitKey(1)
