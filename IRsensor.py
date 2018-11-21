#Proximity Sensor

import RPi.GPIO as GPIO

LEDpin = 8
IRpin = 16

GPIO.setmode(GPIO.BCM) 
GPIO.setup(LEDpin,GPIO.OUT) 
GPIO.setup(IRpin,GPIO.IN)
 
while True:
  GPIO.output(LEDpin,not GPIO.input(IRpin))