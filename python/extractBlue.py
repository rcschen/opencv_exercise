import cv2
import numpy as np
from util import *

img = cv2.imread('../data/source/roi.jpg')

#the img data structure
print img
print '----------------------------'
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 252, 255])

mask = cv2.inRange(hsv, lower_blue, upper_blue)
#show(mask)
for i in mask:
    print i
res = cv2.bitwise_and(img, img, mask=mask)
print "show mask"

show(img)
show(mask)
show(res)
