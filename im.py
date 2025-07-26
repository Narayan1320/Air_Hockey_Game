import cv2
import numpy as np
def onchange(a):
    pass
cv2.namedWindow("mywindow")
cv2.resizeWindow("mywindow",600,150)
cv2.createTrackbar("Red","mywindow",0,255,onchange)
cv2.createTrackbar("Green","mywindow",0,255,onchange)
cv2.createTrackbar("Blue","mywindow",0,255,onchange)
image = np.zeros((512,512,3),np.uint8)

while True:
    r = cv2.getTrackbarPos("Red","mywindow")
    g = cv2.getTrackbarPos("Green","mywindow")
    b = cv2.getTrackbarPos("Blue","mywindow")
    image[:] = [b,g,r]
    cv2.imshow("newimg",image)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()