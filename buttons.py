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
  
  button = previous_state ^ state 
  print ('state is ', state, ' previous state is ', previous_state, ' button is ', button ) 
  previous_state = button
  time.sleep(0.2)
  return (button, previous_state)
  
def button_handler(pin):
   roaming = not roaming
   pass

#def main():
#  previous_state = False
#  while True:
#    button,previous_state = button_pressed(button_pin,previous_state)
#    if button:
#        print('Button Pressed')
#        time.sleep(0.2)
        #put your code here)




if __name__ == "__main__":
    main()