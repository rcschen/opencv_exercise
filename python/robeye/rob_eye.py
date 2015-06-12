import cv2
import urllib
import numpy as np
import time
import corner 
import sys

class ROBeye():
      def __init__(self):
         self.stream=urllib.urlopen('http://192.168.1.234:8080/?action=stream')
         self.controlFlag = True
       
      def showFeature(self, method = "test"):
          bytes=''
          while self.controlFlag:
             bytes+=self.stream.read(1024)
             a = bytes.find('\xff\xd8')
             b = bytes.find('\xff\xd9')
             if a!=-1 and b!=-1:
                jpg = bytes[a:b+2]
                bytes= bytes[b+3:]
                i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
                cv2.imshow('i', getattr(corner,method)(i))
                if cv2.waitKey(1) == 27:
                   exit(0)


if __name__ == '__main__':
   robeye = ROBeye()
   if len(sys.argv) >1:
      selectedMethod = sys.argv[1]   
   else:
      print "Not a valid input"
      exit()
   if selectedMethod in dir(corner):
      robeye.showFeature(selectedMethod)
   elif selectedMethod == "showme" :
      print [ f for f in dir(corner) if f.find('_') == -1 ]
   else:
      print [ f for f in dir(corner) if f.find('_') == -1 ]
      print "No corner function can be used!!"
