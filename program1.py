import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


pin1 = 11 #this is the led pin
pin2 = 13 #this is the switch pin

GPIO.setup(pin2, GPIO.IN)
GPIO.setup(pin1, GPIO.OUT)



try:
   while True:
      if GPIO.input(pin2) == True:
         GPIO.output(pin1, GPIO.HIGH)
      else:
         GPIO.output(pin1, GPIO.LOW)
         
except KeyboardInterrupt:
   print("done") 
   GPIO.cleanup()
      

