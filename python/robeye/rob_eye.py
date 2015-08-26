import cv2
import urllib
import numpy as np
import time
import corner 
import sys
import math
import time

class ROBeye():
      def __init__(self):
         self._stream=urllib.urlopen('http://192.168.1.235:8080/?action=stream')
         self.controlFlag = True
         self._bytes  = ''

      def showFrame(self):
          while self.controlFlag:
             self._bytes+=self._stream.read(1024)
             a = self._bytes.find('\xff\xd8')
             b = self._bytes.find('\xff\xd9')
             if a!=-1 and b!=-1:
                jpg = self._bytes[a:b+2]
                self._bytes= self._bytes[b+3:]
                i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
                return i

      def showFeature(self, method = "test"):
          while self.controlFlag:
                feature = getattr(corner,method)(self.showFrame())
                cv2.imshow( 'i', feature )
                if cv2.waitKey(1) == 27:
                   exit(0)
     
      def searchWayToGo(self, method = 'cannyEdge' ):
          start = time.time()
          while self.controlFlag:
                now = time.time()
                feature = getattr(corner,method)(self.showFrame())
                
                if now - start > 0.1: 
                   weight, high = feature.shape
                   anchor = weight/2
                   feature = normalizeAvailableArea( feature, weight, high, 0)
                   farthest_posisitons = findFarthestPosition(feature, weight, high, 3, 0 )
                   selected_posisiton = findNearestPosition(farthest_posisitons, anchor, weight, high)
                   print ">>>>>>>>>>>>>>>>>>>>>",selected_posisiton
                   start = now
                   cv2.imshow( 'i', feature )
                   if cv2.waitKey(1) == 27:
                      exit(0)

      def test(self, method = 'cannyEdge'):
          while self.controlFlag:

              feature = getattr(corner,method)(self.showFrame())
              print feature
   
              weight, high = feature.shape
              print feature.shape
              cv2.imshow( 'i', feature[60:weight, 80:high])
              if cv2.waitKey(1) == 27:
                   exit(0)
      
def filewrite(content):
    with open('test','wa') as f: f.write(content)
def fileread():
    with open('test','r') as f: f.read()

def findNearestPosition( p_list, anchor, weight, high ):
    o_list = []
    for p in p_list:
        destination = p[0] - anchor
        o_list.append( (p, destination) )
    if len(o_list) == 0:
       return((anchor, high),0)
    sorted_list = sorted(o_list, key = lambda x: math.fabs(x[1]) )    
     
    if len(sorted_list) > 0:
       return sorted_list[0]
    else:
       return ((anchor, high),0)

def normalizeAvailableArea( feature, weight, high, margin = 20 ):
    mid = weight / 2
    j = high-1
    while j > 0 :
        rightAnchor = mid
        leftAnchor = mid
        goRight = False
        goLeft = False
        while rightAnchor < weight or leftAnchor > 0:
            if rightAnchor < weight:
               if goRight: 
                  feature[rightAnchor][j] = 255
               else:
                  if feature[rightAnchor][j] > 0:
                     goRight = True
            if leftAnchor > 0:
               if goLeft:
                  feature[leftAnchor][j] = 255
               else:
                  if feature[leftAnchor][j] > 0:
                     goLeft = True
            rightAnchor = rightAnchor + 1
            leftAnchor = leftAnchor - 1                 
        j = j-1 
    return feature

def findFarthestPosition( feature, weight, high, norm = 4, margin = 20 ):
    position = []
    horizontal = 0
    while horizontal + norm < weight :
       if  horizontal < weight -margin and horizontal > margin:
          for j in reversed(range(high)):
              break2 = False
              for k in range(norm):
                  index = horizontal + k
                  if feature[index][j] > 0:
                     position.append( (index,j) )
                     break2 = True
                     break
              if break2:
                 break

              if j == 1:
                  position.append( (horizontal,j) )

       horizontal = horizontal + norm
    sorted_position = sorted( position, key = lambda x:x[1])
    farthest_positions = [ p for p in sorted_position if p[1] == sorted_position[1][1] ]
    return farthest_positions
 
if __name__ == '__main__':
   robeye = ROBeye()
   if len(sys.argv) > 1:
      selectedMethod = sys.argv[1]   
   else:
      print "Not a valid input"
      exit()
   if selectedMethod in dir(corner):
      robeye.showFeature(selectedMethod)
   elif selectedMethod == "showme" :
      print [ f for f in dir(corner) if f.find('_') == -1 ]
   elif selectedMethod == "way" :
      robeye.searchWayToGo()
   elif selectedMethod == "debug" :
      robeye.test()

   else:
      print [ f for f in dir(corner) if f.find('_') == -1 ]
      print "No corner function can be used!!"
