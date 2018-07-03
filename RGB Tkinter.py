from tkinter import *
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.output(14,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
GPIO.output(23,GPIO.LOW)

def redf():
    GPIO.output(14,GPIO.HIGH)
    GPIO.output(23,GPIO.HIGH)
    time.sleep(2)
    GPIO.output(14,GPIO.LOW)
    GPIO.output(23,GPIO.LOW)
def greenf():
    GPIO.output(23,GPIO.HIGH)
    GPIO.output(18,GPIO.HIGH)
    time.sleep(2)
    GPIO.output(23,GPIO.LOW)
    GPIO.output(18,GPIO.LOW)
def discof():
    counter=0
    while counter<5:
        GPIO.output(14,GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(14,GPIO.LOW)
        GPIO.output(18,GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(18,GPIO.LOW)
        GPIO.output(23,GPIO.HIGH)
        time.sleep(0.2)
        counter+=1
        print(counter)
def xitf():
    GPIO.cleanup()
    window.destroy()
window=Tk()
redb=Button(window,text='Click me for Red color',command=redf)
greenb=Button(window,text='Click me for Green color',command=greenf)
discob=Button(window,text='Disco light',command=discof)
exitb=Button(window,text='Exit',command=xitf)
redb.pack()
greenb.pack()
discob.pack()
exitb.pack()
