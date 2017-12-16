import cv2

clicked=False


def onMouse(event,x,y,flags,param):
    global clicked
    if event==cv2.EVENT_LBUTTONUP:
        clicked=True




camera=cv2.VideoCapture(0)
cv2.namedWindow('MyWindow-Mouse Event')
cv2.setMouseCallback('MyWindow-Mouse Event',onMouse)

print('Отображение данных с камеры. Для отображение кликните по окну или нажмите кнопку')
success,frame=camera.read()
while success and cv2.waitKey(1)==-1 and not clicked:
    cv2.imshow('MyWindow-Mouse Event',frame)
    success,frame=camera.read()


camera.release()
cv2.destroyAllWindows()

