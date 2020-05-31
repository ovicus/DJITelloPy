import time, cv2
from djitellopy import Tello

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

# Take off, wait 5 seconds, take a picture and land

tello.takeoff()

time.sleep(5)
cv2.imwrite("picture.png", frame_read.frame)

tello.land()
