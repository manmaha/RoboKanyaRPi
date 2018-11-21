#Flash led

import RPi.GPIO as GPIO

RedLED = 8
YellowLED = 21
GPIO.setmode(GPIO.BCM) 
GPIO.setup(RedLED,GPIO.OUT) 
GPIO.setup(YellowLED,GPIO.OUT) 

#set LEDs to flash forever
while True:
  GPIO.output(RedLED,GPIO.HIGH)
  GPIO.output(YellowLED,GPIO.LOW)
  time.sleep(0.5)
  GPIO.output(RedLED,GPIO.LOW)
  GPIO.output(YellowLED,GPIO.HIGH)
  time.sleep(0.5)	    