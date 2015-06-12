import cv2
import numpy as np
from util import *

imgRoi = '../data/source/messi5.jpg'
img = cv2.imread(imgRoi)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift=cv2.SIFT()
kp = sift.detect(gray, None)
img1=cv2.drawKeypoints(gray, kp)
show(img1)
img2=cv2.drawKeypoints(gray,kp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

show(img2)

kp,des = sift.detectAndCompute(img, None)
print len(kp)
print len(des)
for i in des:
    print len(i)
    break
if cv2.waitKey(0) & 0xff == 27:
   cv2.destoryAllWindows()
