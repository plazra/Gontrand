#!/usr/bin/env python

from __future__ import division
import Adafruit_PCA9685
import time

sCtrl = Adafruit_PCA9685.PCA9685()

# Pulse lengths
servoRange = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600]

def setup():
    global channel
    # Set frequency to 60hz, good for servos.
    sCtrl.set_pwm_freq(60)
    channel = int(input('Enter channel: '))

def loop():
    while True:
##        for r in servoRange:
##            changePulse(r)
##        for r in reversed(servoRange):
##            changePulse(r)
        #changePulse(int(input('Enter freq: ')))
        startPos = int(input('0-10: '))
        sCtrl.set_pwm(channel, 0, servoRange[startPos])
        time.sleep(0.6)
        sCtrl.set_pwm(channel, 0, 0)
        newPos = int(input('0-10: '))
        if(startPos < newPos):
            for p in range(startPos, (newPos + 1), 1):
                sCtrl.set_pwm(channel, 0, servoRange[p])
                time.sleep(0.08)
            startPos = newPos
            sCtrl.set_pwm(channel, 0, 0)
        elif(newPos < startPos):
            for p in range(startPos, (newPos - 1), -1):
                sCtrl.set_pwm(channel, 0, servoRange[p])
                time.sleep(0.08)
            startPos = newPos
            sCtrl.set_pwm(channel, 0, 0)
    
##def changePulse(p):
##    sCtrl.set_pwm(0, 0, p)
##    sCtrl.set_pwm(1, 0, p)
##    time.sleep(0.08)
##    sCtrl.set_pwm(0, 0, 0)
##    sCtrl.set_pwm(1, 0, 0)

def destroy():
    sCtrl.set_pwm(channel, 0, 350)
    #sCtrl.set_pwm(1, 0, 350)
    time.sleep(0.3)
    sCtrl.set_pwm(channel, 0, 0)
    #sCtrl.set_pwm(1, 0, 0)
    
if __name__ == '__main__':     
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
