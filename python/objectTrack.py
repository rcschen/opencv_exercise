import cv2
from util import *
import numpy as np

imgRoi = '../data/source/messi5.jpg'
imgCVLog = '../data/source/opencv_logo.png'
img1 = cv2.imread(imgRoi)
img2 = cv2.imread(imgCVLog)
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]
#show(roi)
show(img2)
img2gray = cv2.cvtColor(img2[0:rows,0:cols],cv2.COLOR_BGR2GRAY)
#show(img2gray)
lower_blue = np.array([200,0,0])
upper_blue = np.array([255,0,0])

maskRange = cv2.inRange(img2, lower_blue, upper_blue)
print maskRange
show(maskRange)
blueres = cv2.bitwise_and(img2,img2, mask= maskRange)
show(blueres)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
print ret
print mask
show(mask)

