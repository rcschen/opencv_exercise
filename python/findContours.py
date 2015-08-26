import cv2
import numpy as np
from util import *

imgRoi = '../data/source/messi5.jpg'
img = cv2.imread(imgRoi)
show(img)
def findContours(img):
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,127,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 
    return contours, hierarchy

def drawContours(img, contourColor):
    contours, h = findContours(img)
    cv2.drawContours(img, contours, -1, contourColor, -1, hierarchy=h[0])
    return img

#c, h = findContours(img)
#print c
#print '--------------'
#print h
show(  drawContours(img, (0,255,0)) )
#show(c)
#show(h)

if cv2.waitKey(0) & 0xff == 27:
   cv2.destoryAllWindows()
