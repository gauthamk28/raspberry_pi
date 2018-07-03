import random, time
import RPi.GPIO as GPIO
import colorsys
 
RUNNING = True
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
red = 14
green = 18
blue = 23
 
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)


Freq = 100
 
RED = GPIO.PWM(red, Freq)
RED.start(100)
GREEN = GPIO.PWM(green, Freq)
GREEN.start(100)
BLUE = GPIO.PWM(blue, Freq)
BLUE.start(100)

outval = 128

def wheel_color(position):
    """Get color from wheel value (0 - 384)."""
    
    if position < 0:
        position = 0
    if position > 384:
        position = 384

    if position < 128:
        r = 127 - position % 128
        g = position % 128
        b = 0
    elif position < 256:
        g = 127 - position % 128
        b = position % 128
        r = 0
    else:
        b = 127 - position % 128
        r = position % 128
        g = 0

    return r, g, b

try:
   while(True):
      for pos in range(0,385):
         r, g, b = wheel_color(pos)
         print (r, g, b)
         percenttestr = (r/128.0)*100.0
         percenttestg = (g/128.0)*100.0
         percenttestb = (b/128.0)*100.0
         print (percenttestr)
         print (percenttestg)
         print (percenttestb)
         RED.ChangeDutyCycle(percenttestr)
         GREEN.ChangeDutyCycle(percenttestg)
         BLUE.ChangeDutyCycle(percenttestb)
         time.sleep(0.1)

         
except KeyboardInterrupt:
   GPIO.cleanup()
