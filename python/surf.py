import cv2
import numpy as np
from util import *

imgRoi = '../data/source/messi5.jpg'
img = cv2.imread(imgRoi)

surf=cv2.SURF()
kp, des = surf.detectAndCompute(img, None)
img1=cv2.drawKeypoints(img, kp, None, (255,0,0),4)
show(img1)
if cv2.waitKey(0) & 0xff == 27:
   cv2.destoryAllWindows()
