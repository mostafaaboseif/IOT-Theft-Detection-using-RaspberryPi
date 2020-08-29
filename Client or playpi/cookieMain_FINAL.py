from P3picam import motion
import picamera
from datetime import datetime
from subprocess import call
from time import sleep
from cookieClient_FINAL import backup
from cookieClient_FINAL import transmit
from cookieAnalog2 import getTemp
import RPi.GPIO as GPIO

picPath = "/home/pi/Desktop/cookie/images/"
sleepTime = 3
triggerTemp = 22
lightPin = 22 # actual GPIO name, not board number

# Initialize the GPIO
def initGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(lightPin, GPIO.OUT)

def captureImage(currentTime, picPath):
    # Generate the picture's name
    picName = currentTime.strftime("%Y.%m.%d-%H%M%S") + '.jpg'
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.capture(picPath + picName)
    print("We have taken a picture.")
    return picName

def getTime():
    # Fetch the current time
    currentTime = datetime.now()
    return currentTime

def lightItUp():
    try:
        # Turn on the CFL through the transistor/relay
        GPIO.output(lightPin, True)
    except:
        GPIO.output(lightPin, False)
        GPIO.cleanup()

def timeStamp(currentTime, picPath, picName):
    # Variable for file path
    filepath = picPath + picName
    # Create message to stamp on picture
    message = currentTime.strftime("%Y.%m.%d - %H:%M:%S")
    # Create command to execute
    timestampCommand = "/usr/bin/convert " + filepath + " -pointsize 36 \
    -fill red -annotate +700+650 '" + message + "' " + filepath
    # Execute the command
    call([timestampCommand], shell=True)
    print("We have timestamped our picture.")

def tempMonitor():
    temp = float(getTemp())
    print("Our temperature is: " + str(temp) + "C")
    if temp < float(triggerTemp):
        message = "LED_ON"
        print("Transmitting data.")
        response = transmit(message)
        print(response)

initGPIO()
try:
    while True:
        if motion():
            # First get the time.
            currentTime = getTime()
            # Get the lights on.
            lightItUp()
            # Then take a picture.
            picName = captureImage(currentTime, picPath)
            # Then timestamp the picture.
            timeStamp(currentTime, picPath, picName)
            print("Took a picture")
            completePath = picPath + picName
            # Then backup the timestamped picture to the other pi.
            backup(completePath)
            print("Backup complete.")
        else:
            # If the cookie thief isn't detected, might as well
            # monitor our temperature.
            tempMonitor()
except:
    GPIO.output(lightPin, False)
    GPIO.cleanup()
