import cv2
from util import *
imgRoi = '../data/source/messi5.jpg'
imgCVLog = '../data/source/opencv_logo.png'
img1 = cv2.imread(imgRoi)
img2 = cv2.imread(imgCVLog)
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]
show(roi)

img2gray = cv2.cvtColor(img2[0:rows,0:cols],cv2.COLOR_BGR2GRAY)
show(img2gray)

ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
print ret
print mask
show(mask)

mask_inv = cv2.bitwise_not(mask)
show(mask_inv)
img1_fg = cv2.bitwise_and(roi,roi,mask = mask_inv)
print img1_fg
show(img1_fg)

img2_bg = cv2.bitwise_and(img2,img2,mask = mask)
print img2_bg
show(img2_bg)
dst = cv2.add(img1_fg,img2_bg)
show(dst)
img1[0:rows, 0:cols ] = dst
show(img1)
