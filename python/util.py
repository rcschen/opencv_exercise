import cv2

def show(img):
    cv2.imshow('show image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def showVideo( videoPath ):
    print cv2.VideoCapture(videoPath)
    cap = cv2.VideoCapture(videoPath)
    #print cap
    while(cap.isOpened()):
          ret, frame = cap.read()
          print '??????' , ret

          print frame
          #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
          cv2.imshow( 'frame',frame)
          if not ret:
             break
          if cv2.waitKey(1) & 0xFF == ord('q'):
             break
    cap.release()
    cv2.destroyAllWindows()

