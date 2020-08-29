import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

blinkCount = 3
count = 0
relayPin = 22
buttonPin = 5

# Setup the pin the LED is connected to
GPIO.setup(relayPin, GPIO.OUT)
# Setup the button
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

buttonPress = True
relayState = False

try:
    while count < blinkCount:
        print("Come on man, press the button!")
        buttonPress = GPIO.input(buttonPin)
        if buttonPress == False and relayState == False:
            GPIO.output(relayPin, True)
            print("relay ON")
            relayState = True
            sleep(0.5)
        elif buttonPress == False and relayState == True:
            GPIO.output(relayPin, False)
            print("relay OFF")
            relayState = False
            count += 1
            sleep(0.5)
        sleep(0.1)
finally:
    # Reset the GPIO Pins to a safe state
    GPIO.output(relayPin, False)
    GPIO.cleanup()
