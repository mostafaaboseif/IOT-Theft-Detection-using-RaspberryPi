import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

blinkCount = 3
count = 0
LEDPin = 22

# Setup the pin the LED is connected to
GPIO.setup(LEDPin, GPIO.OUT)

try:
    while count < blinkCount:
        GPIO.output(LEDPin, True)
        print("LED ON")
        sleep(3)
        GPIO.output(LEDPin, False)
        print("LED OFF")
        sleep(1)
        count += 1
finally:
    # Reset the GPIO Pins to a safe state
    GPIO.cleanup()
