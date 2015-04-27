import numpy as np
import cv2
from util import *
source = '../data/source/SAMPLE.AVI'
target = '../data/target/output.avi'
cap = cv2.VideoCapture(source)

# Define the codec and create VideoWriter object
fourcc = cv2.cv.CV_FOURCC(*'X264')
out = cv2.VideoWriter( target, fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)
        print frame
        print '###'
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
import os
print '---------', os.path.exists(target)
showVideo(target)
