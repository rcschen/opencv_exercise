import cv2
import numpy as np
from util import *

imgRoi = '../data/source/messi5.jpg'
img = cv2.imread(imgRoi)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)

dst = cv2.cornerHarris(gray, 2,3,0.04)
print dir(dst)
print "===="
print dst.max()
show(dst)

rows,cols,channels = img.shape

checkList = dst > 0.00001*dst.max()
for i in range(rows):
   for j in range(cols):
       if checkList[i][j]:
          img[i][j]=[0,0,255]
       else:
          img[i][j]=[255,255,255]


show(img)

if cv2.waitKey(0) & 0xff == 27:
   cv2.destoryAllWindows()
