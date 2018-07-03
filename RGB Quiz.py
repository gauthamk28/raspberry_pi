import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.output(14,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
GPIO.output(23,GPIO.LOW)
rans=0
counter=0
ansone=int(input("What is 1+1= : "))
if ansone==2:
           print("Right answer")
           rans+=1
           GPIO.output(18,GPIO.HIGH)
           GPIO.output(23,GPIO.HIGH)
           time.sleep(2)
           GPIO.output(18,GPIO.LOW)
           GPIO.output(23,GPIO.LOW)
else:
           print("Wrong answer")
           GPIO.output(14,GPIO.HIGH)
           GPIO.output(23,GPIO.HIGH)
           time.sleep(2)
           GPIO.output(14,GPIO.LOW)
           GPIO.output(23,GPIO.LOW)
anstwo=int(input("What is 2+2= : "))
if anstwo==4:
           print("Right answer")
           rans+=1
           GPIO.output(18,GPIO.HIGH)
           GPIO.output(23,GPIO.HIGH)
           time.sleep(2)
else:
           print("Wrong answer")
           GPIO.output(14,GPIO.HIGH)
           GPIO.output(23,GPIO.HIGH)
           time.sleep(2)
print("Number of Right answers:",rans)
if rans==2:
    print("Hall of Fame")
    while counter<=5:
        GPIO.output(14,GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(14,GPIO.LOW)
        GPIO.output(18,GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(18,GPIO.LOW)
        GPIO.output(23,GPIO.HIGH)
        time.sleep(0.2)
        counter+=1
GPIO.cleanup()
