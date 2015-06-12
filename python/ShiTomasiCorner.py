import cv2
import numpy as np
from util import *

imgRoi = '../data/source/messi5.jpg'
img = cv2.imread(imgRoi)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int0(corners)
print corners

rows,cols,channels = img.shape

for c in corners:
   x,y = c.ravel()
   cv2.circle(img,(x,y),3,255,-1)
show(img) 
for i in range(rows):
    for j in range(cols):
        if [[i,j]] in corners :
           img[i][j]=[0,0,255]
        else:
           img[i][j]=[255,255,255]

show(img)

if cv2.waitKey(0) & 0xff == 27:
   cv2.destoryAllWindows()
