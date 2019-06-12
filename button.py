import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
button_pin = 18
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#button_pin is pulled down
#connect the other pin to 3.3v

def button_pressed(button_pin,previous_state):
#returns (button state, previous state) 
  GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
  state = GPIO.input(button_pin)
  button = not previous_state and state 
  previous_state = state
  return (button, previous_state)
  time.sleep(0.05)


previous_state = False
while True:
    button,previous_state = button_pressed(button_pin,previous_state)
    if button:
        print('Button Pressed')
        #put your code here)
