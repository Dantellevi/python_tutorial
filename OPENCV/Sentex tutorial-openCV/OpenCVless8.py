import cv2
import numpy as np

#filters
cap=cv2.VideoCapture(0)

while True:
    _, frame= cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([30, 150, 50])

    upper_red = np.array([255, 255, 180])

    dark_red=np.uint8([[[12,22,121]]])
    dark_red=cv2.cvtColor(dark_red,cv2.COLOR_BGR2HSV)

    mask=cv2.inRange(hsv,lower_red,upper_red)
    res=cv2.bitwise_and(frame,frame,mask=mask)

    kernel=np.ones((15,15), np.float32)/225
    smothed=cv2.filter2D(res, -1, kernel)
    blur= cv2.GaussianBlur(res,(15,15),0)
    median = cv2.medianBlur(res, 15)
    bilateral = cv2.bilateralFilter(res, 15, 75, 75)
    cv2.imshow('frame',frame)
    #cv2.imshow('mask', mask)
    #cv2.imshow('res', res)
    #cv2.imshow('smothed', smothed)
    #cv2.imshow('median', median)
    #cv2.imshow('bilateral Blur', bilateral)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows ()
cap.release()
