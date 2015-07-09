import cv2
import numpy as np
from util import *
img = cv2.imread('../data/source/roi.jpg')
show(img)
x, y , w, h = 4, 5, 28, 29
cv2.rectangle(img, (x,y), (x+w,y+h), 255,2) 
show(img)
