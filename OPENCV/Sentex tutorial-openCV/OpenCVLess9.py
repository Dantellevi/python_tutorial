import cv2
import numpy as np

#Morphologis
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([30, 150, 50])

    upper_red = np.array([255, 255, 180])

    dark_red = np.uint8([[[12, 22, 121]]])
    dark_red = cv2.cvtColor(dark_red, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((5, 5), np.float32) / 225
    smothed = cv2.filter2D(res, -1, kernel)
    erosion=cv2.erode(mask,kernel,iterations=1)
    dilation=cv2.dilate(mask,kernel,iterations=1)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('Originals', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()