import cv2
from util import *
imgRoi = '../data/source/roi.jpg'
imgCVLog = '../data/source/opencvLog.png'
img1 = cv2.imread(imgRoi)
img2 = cv2.imread(imgCVLog)
rows,cols,channels = img1.shape
log = img1[0:rows, 0:cols ]
img1gray = cv2.cvtColor(img1[0:rows,0:cols],cv2.COLOR_BGR2GRAY)
show(img1gray)
ret, mask = cv2.threshold(img1gray, 10, 255, cv2.THRESH_BINARY)
print ret
print mask
show(mask)
mask_inv = cv2.bitwise_not(mask)
show(mask_inv)
img2_bg = cv2.bitwise_and(log,log,mask = mask_inv)
print img2_bg
#show(img1_bg)
img1_fg = cv2.bitwise_and(img1,img1,mask = mask)
print img1_fg
dst = cv2.add(img1_fg,img2_bg)
show(dst)
img2[0:rows, 0:cols ] = dst
show(img2)
