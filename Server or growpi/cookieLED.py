import RPi.GPIO as GPIO
from time import sleep

sleepTime = 5
ledPin = 12

def ledSetup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)

def ledON():
    GPIO.output(ledPin, True)
    sleep(sleepTime)
    GPIO.cleanup()

def callLED():
    ledSetup()
    ledON()
