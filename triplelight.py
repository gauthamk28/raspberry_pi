#Traffic Signal program
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
#GPIO.setup(23,GPIO.OUT)
#GPIO.setup(25,GPIO.OUT)
GPIO.output(18,GPIO.HIGH)
#GPIO.output(23,GPIO.HIGH)
#GPIO.output(25,GPIO.HIGH)
GPIO.cleanup()
