import picamera
from subprocess import call
from datetime import datetime
from time import sleep

# Our file path
filePath = "/home/pi/Desktop/cookie/timestamped_pics/"
picTotal = 5
picCount = 0

while picCount < picTotal:
    # Grab the current time
    currentTime = datetime.now()
    # Create file name for our picture
    picTime = currentTime.strftime("%Y.%m.%d-%H%M%S")
    picName = picTime + '.jpg'
    completeFilePath = filePath + picName

    # Take picture using new filepath
    with picamera.PiCamera() as camera:
        camera.resolution = (1280,720)
        camera.capture(completeFilePath)
        print("We have taken a picture.")

    # Create our stamp variable
    timestampMessage = currentTime.strftime("%Y.%m.%d - %H:%M:%S")
    # Create time stamp command to have executed
    timestampCommand = "/usr/bin/convert " + completeFilePath + " -pointsize 36 \
    -fill red -annotate +700+650 '" + timestampMessage + "' " + completeFilePath
    # Actually execute the command!
    call([timestampCommand], shell=True)
    print("We have timestamped our picture!")

    # Advance our picture counter
    picCount += 1
    sleep(3)

