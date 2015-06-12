import cv2

cam= "http://192.168.1.237:8080/?action=stream"

cap=cv2.VideoCapture(cam)
if not cap:
   print "Fail to capture video!"
print ">>>>>>>----"

while True:
     print ">>>>>>>"
     ret, current_frame = cap.read()
     print ret
     print current_frame
     if not current_frame :
        print "No frame receive"
        break

     cv2.imshow("oh yeah", current_frame)
     if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
