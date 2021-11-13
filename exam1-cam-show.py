import cv2

# Get videocapture object
cap = cv2.VideoCapture(0)

# Infinite loop
while True:
    # Read from cap. ret is flag for error detection
    ret, img = cap.read()
    # Show image
    cv2.imshow('myView', img)
    # Wait for rendering
    cv2.waitKey(1)
