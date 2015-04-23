import numpy as np
import cv2
from util import *

img = np.zeros((512,512,3), np.uint8)
print "disply a black paper:", img
show(img)
cv2.line(img,(0,0),(511,511),(255,0,0),5)
print "draw a blue diagonal line on the black paper:", img
show(img)
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
print "draw a red rectangle on the black paper:", img
show(img)
cv2.rectangle(img,(384,0),(10,20),(0,0,255),3)
print "draw a red rectangle on the black paper:", img
show(img)
cv2.circle(img,(447,63), 63, (0,0,255), -1)
print "draw a green circle on the black paper:", img
show(img)
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
print "draw a green ellipse on the black paper:", img
show(img)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))
print "draw a polylines on the black paper:", img
show(img)
font = cv2.FONT_HERSHEY_SIMPLEX
#cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255))
print "draw a text: OpenCV on the black paper:", img
show(img)

