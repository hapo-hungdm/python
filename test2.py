import cv2 as cv

gst = "rtspsrc location=rtsp://usser:pass@ip:port/url latency=0 ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! appsink"
capture = cv.VideoCapture(gst, cv.CAP_GSTREAMER)

print("Is pipeline open: ", capture.isopened())
while capture.isOpened() :
     ret, frame = capture.read()
     print("Is receiving frames: ", ret)
     cv.imshow("Stream", frame)
     
     if cv.waitKey(25) & 0xFF == ord("q"):
          break

capture.release()
cv.destroyAllWindows()
