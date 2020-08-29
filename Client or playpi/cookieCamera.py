import picamera

# Setup the camera such that it closes
# when we are done with it.
print("About to take a picture.")
with picamera.PiCamera() as camera:
    camera.resolution = (1280,720)
    camera.capture("/home/pi/Desktop/cookie/newimage.jpg")
print("Picture taken.")
