import cv2
import urllib
import numpy as np
import threading
import time

class Frame:
      def __init__(self, frame):
          self.timeStamp = time.time()
          self.frame = frame

      def showFrame(self):
          cv2.imshow( 'i', self.frame )
          if cv2.waitKey(1) == 27:
                   exit(0)
    
      def applyProcessToFrame(self, *par ):
          processName = par.__getitem__(0)
          if not processName in dir(imgprocess):
             print "Selected process is not found: ", processName
          tmp_par = list(par)
          tmp_par[0] = self.frame
          par = tuple(tmp_par)
          try:
             feature = getattr(imgprocess, processName)(*par)
             return Frame( feature )

          except Exception as e:
             print "Run image process error:", e
             return None         


class Stream:
     def __init__(self, url):
         self._video = urllib.urlopen(url)
         self.frameSize = 1024

         self._bytes = ''

     def captureFrame(self):
          #_bytes = ''
         
          while True:
               try:
                  self._bytes += self._video.read(self.frameSize)
                  startAnchor = self._bytes.find('\xff\xd8')
                  endAnchor = self._bytes.find('\xff\xd9')
                  if startAnchor != -1 and endAnchor != -1:
                     jpg = self._bytes[startAnchor: endAnchor+2]
                     self._bytes = self._bytes[endAnchor+3:]
                     frame = cv2.imdecode(np.fromstring(jpg, dtype = np.uint8), cv2.CV_LOAD_IMAGE_COLOR)
                     return Frame(frame)
               except Exception as e:
                  print 'Can not capture frame: ',e
                  return None

     def ctn(self):
          while True:
               self.captureFrame().showFrame()


if __name__ == '__main__':

   url ='http://192.168.2.110:8080/?action=stream' 
   Stream(url).ctn()
