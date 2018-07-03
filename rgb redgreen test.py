import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.output(14,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
GPIO.output(23,GPIO.LOW)
counter=0
while counter<5:
    """GPIO.output(14,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(14,GPIO.LOW)
    time.sleep(0.2)"""
    GPIO.output(23,GPIO.HIGH)
    GPIO.output(18,GPIO.HIGH)
    time.sleep(0.5)
    """GPIO.output(14,GPIO.LOW)
    time.sleep(0.2)"""
    print(counter)
    counter+=1
GPIO.cleanup()
