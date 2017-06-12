import numpy as np
import cv2
from detect_util import *

#testing the facial recognition in real time with the cam in your computer
camera_zero = cv2.VideoCapture(0)
while(camera_zero.isOpened):
    ret, frame = camera_zero.read()
    if ret:
        face = drawRectsInface(frame)
        cv2.imshow('frame', face)
        if cv2.waitKey(1) == 27: #close the window if press ESC key
            break
    else:
        break

#free all sub routines in the variables
camera_zero.release()
cv2.destroyAllWindows()
