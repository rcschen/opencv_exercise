from cv2 import *
from cv2 import cv
import urllib
import numpy as np
k=0
print "!!!!!2"

capture=cv.CaptureFromFile("http://192.168.1.237:8080/?action=stream")
print "!!!!!"
namedWindow("Display",1)

while True:
    frame=cv.QueryFrame(capture)
    if frame is None:
        print 'Cam not found'
        break
    else:
        cv.ShowImage("Display", frame)
    if k==0x1b:
        print 'Esc. Exiting'
        break
