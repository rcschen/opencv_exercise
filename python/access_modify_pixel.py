import cv2
import numpy as np

def show(img):
    cv2.imshow('show image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread('../data/source/roi.jpg')

"""
image data structure
[position_x, position_y, position of pixel in [R,B,G]]
"""
#the img data structure
print img
print '----------------------------'

#the pixel of (0,0): [B,G,R]
print 'the pixel of (0,0): [B,G,R]:', img[0,0]

print 'B:',img[0,0,0] #B
print 'G:',img[0,0,1] #G
print 'R:',img[0,0,2] #R
print '----------------------------'

#get value of R at  position (10,10)
print 'get value of R at  position (10,10):', img.item(10,10,2)
#set value of R at position(10, 10) to be 10
img.itemset((10,10,2),100)
print 'set value of R at position(10, 10) to be 100:',img.item(10,10,2)
print '----------------------------'

print 'img shape is(row_size,colume_size, channel_size(RBG)):', img.shape
print 'img size is shape[0]*shape[1]*shope[2]', img.size
print 'img dtype:', img.dtype
print '-------show subset of img and copy it to other position--------------'
show(img)
ball = img[220:280, 270:330]
show(ball)
img[0:60, 0:60] = ball
show(img)
print '----------------------------'
b,g,r = cv2.split(img)
print 'b of img split', b
print 'g of img split', g
print 'r of img split', r
img = cv2.merge((b,g,r))
print 'merge b', img[:,:,0]
print 'merge r', img[:,:,1]
print 'merge g', img[:,:,2]
show(img[:,:,0])
show(img[:,:,1])
show(img[:,:,2])

