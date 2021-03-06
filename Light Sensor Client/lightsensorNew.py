from time import sleep
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import client_v1

SPI_PORT   = 0
SPI_DEVICE = 0

mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
lightChannel=0
sleeptime = 1
lightRange = 150

def getReading(channel):
    return mcp.read_adc(channel)

def getLDR():
    lightData=getReading(lightChannel)
    return light_voltage


s = client_v1.setupSocket()

while True:
    light_data=getReading(lightChannel)
    if light_data>lightRange:
         pass
    else:
         client_v1.sendReceive(s, "light Detected")
    sleep(sleeptime)

