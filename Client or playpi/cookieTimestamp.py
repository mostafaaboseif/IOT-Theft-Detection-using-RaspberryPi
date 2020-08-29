import picamera
from subprocess import call

# Our filename
fileName = "/home/pi/Desktop/cookie/newpic.jpg"

# Take a picture using our camera
with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.capture(fileName)
    print("We have taken a picture.")

# Our timestamp's message
print("About to timestamp our picture.")
timestampMessage = "Check out this message!"
# Specify the command we want to call
timestampCommand = "/usr/bin/convert " + fileName + " -pointsize 32 \
-fill red -annotate +700+500 '" + timestampMessage + "' " + fileName
# Execute our command
call([timestampCommand], shell=True)
print("Picture has been timestamped.")
