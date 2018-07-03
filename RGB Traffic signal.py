"""
Common Cathode LED
14--->3rd pin
18--->1st pin
23--->4th pin
"""

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.output(14,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
GPIO.output(23,GPIO.LOW)
times=0
while times<3:
    print(times+1,"st time")
    #Red-->23,14(3 Seconds)
    print("STOP!")
    GPIO.output(14,GPIO.HIGH)
    GPIO.output(23,GPIO.HIGH)
    time.sleep(3)
    GPIO.output(14,GPIO.LOW)
    GPIO.output(23,GPIO.LOW)
    #Yellow-->23(1 second))
    print("Alert!")
    GPIO.output(23,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(23,GPIO.LOW)
    #Green-->23,18(2 seconds)
    print("Go!")
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(23,GPIO.HIGH)
    time.sleep(2)
    GPIO.output(18,GPIO.LOW)
    GPIO.output(23,GPIO.LOW)
    times+=1
GPIO.cleanup()
