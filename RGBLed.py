import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
try:
    while(True):
        request=input("RGB---->")
        if(len(request)==3):
            GPIO.output(14,int(request[0]))
            GPIO.output(18,int(request[1]))
            GPIO.output(23,int(request[2]))
except KeyboardInterrupt:
    GPIO.cleanup()
##import RPi.GPIO as GPIO
##GPIO.setmode(GPIO.BCM)
##GPIO.setup(18,GPIO.OUT)
##GPIO.setup(23,GPIO.OUT)
##GPIO.setup(24,GPIO.OUT)
##counter=0
##while counter>=5:
##    GPIO.output(18,GPIO.HIGH)
##    GPIO.output(23,GPIO.HIGH)
##    GPIO.output(24,GPIO.HIGH)
##    counter+=1
##    print(counter)
##GPIO.cleanup()
