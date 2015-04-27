import cv2
from util import *
imgRoi = '../data/source/roi.jpg'
imgCVLog = '../data/source/opencvLog.png'
img1 = cv2.imread(imgRoi)
print img1.shape
img2 = cv2.imread(imgCVLog)
print img2.shape
img1withimg2 = cv2.addWeighted(img2[0:img1.shape[0], 0:img1.shape[1]],0.7,img1,0.3,0)
print img1withimg2.shape
show(img1withimg2)
