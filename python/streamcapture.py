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

class OpticalFlow:
     def __init__(self, stream):
         self.stream = stream
         self.color = np.random.randint(0,255,(100,3))
         #self.refindGood()
         self.refindContours()
         self.lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

     def recapture(self):
         self.old_frame = self.stream.captureFrame().frame
         self.old_gray = cv2.cvtColor(self.old_frame, cv2.COLOR_BGR2GRAY)


     def refindGood(self):
         self.recapture()
         feature_params = dict( maxCorners = 100,
                                qualityLevel = 0.3,
                                minDistance = 7,
                                blockSize = 7 )

         self.p0 = cv2.goodFeaturesToTrack(self.old_gray, mask = None, **feature_params)
         self.mask = np.zeros_like(self.old_frame)
         print "ppppppp"
         print self.p0
         print "ppppppp" 
         print type(self.p0)

     def refindContours(self):
         self.recapture()
         ret,thresh = cv2.threshold(self.old_gray,127,255,0)
         #print thresh
         p0list, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
         self.p0 = p0list[0]
         for i in p0list[1:]:
             np.concatenate((self.p0,i),axis=0)
         print "ppppppp"
         print self.p0

         print "ppppppp" 
         print type(self.p0)

         self.mask = np.zeros_like(self.old_frame)
     
     def runof(self):
         while(1):
            frame = self.stream.captureFrame().frame
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            self.p1, st, err = cv2.calcOpticalFlowPyrLK(self.old_gray, frame_gray, self.p0, None, **self.lk_params)
            #print self.p0
            #print self.p0.shape
            #print ">>>>>"
            #print "=======",st
            #print "=======",st
            #print "=======",self.p1

            good_new = self.p1[st==1]
            #print good_new
            if len(good_new) == 0:
               #self.refindGood()   
               self.refindContours()

            #print good_new
            good_old = self.p0[st==1]
            for i,(new,old) in enumerate(zip(good_new,good_old)):
                a,b = new.ravel()
                c,d = old.ravel()
                cv2.line(self.mask, (a,b),(c,d), self.color[i].tolist(), 2)
                cv2.circle(frame,(a,b),5,self.color[i].tolist(),-1)
                img = cv2.add(frame,self.mask)
                #print img 
                Frame(img).showFrame()
  
                self.old_gray = frame_gray.copy()
                self.p0 = good_new.reshape(-1,1,2)




if __name__ == '__main__':

   url ='http://192.168.1.232:8080/?action=stream' 
   stream = Stream(url)
   OpticalFlow(stream).runof()
