import cv2
import numpy as np
from util import *

img_rob = cv2.imread('../data/source/roi.jpg')
img_cvlog = cv2.imread('../data/source/opencv_logo.png')

rows_cv, cols_cv, channels_cv = img_cvlog.shape
rows_rob, cols_rob, channels_rob = img_rob.shape
rows = min(rows_cv, rows_rob)
cols = min(cols_cv, cols_rob)

img_rob_resize = img_rob[0:rows, 0:cols]
img_cvlog_resize = img_cvlog[0:rows, 0:cols]

hsv_rob = cv2.cvtColor(img_rob, cv2.COLOR_BGR2HSV)
hsv_cvlog = cv2.cvtColor(img_cvlog, cv2.COLOR_BGR2HSV)

hsv_rob_resize = hsv_rob[0:rows, 0:cols]
hsv_cvlog_resize = hsv_cvlog[0:rows, 0:cols]

lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])

mask = cv2.inRange(hsv_rob_resize, lower_blue, upper_blue)
show(mask)
print img_rob_resize.size
print img_rob_resize.shape

print img_cvlog_resize.size
print img_cvlog_resize.shape

show(img_cvlog_resize)
res = cv2.bitwise_and(img_rob_resize, img_cvlog_resize, mask=mask)
show(res)
print "----the other hand----"
lower_blue = np.array([100, 0, 0])
upper_blue = np.array([130, 255, 255])

mask = cv2.inRange(hsv_cvlog_resize, lower_blue, upper_blue)
show(mask)

show(img_cvlog_resize)
res = cv2.bitwise_and(img_cvlog_resize, img_rob_resize, mask=mask)
show(res)

