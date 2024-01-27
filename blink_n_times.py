import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep from time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering

ITER_COUNT = float(input("How many blinks"))
  
pin1 = 11
pin2 = 13

GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pin2, GPIO.IN)



try:
   while True:
      input_state = GPIO.input(pin2)
      if input_state == GPIO.HIGH:
         while ITER_COUNT > 0: # Run ITER_COUNT times
            ITER_COUNT -= 1 # Decrement counter
            GPIO.output(pin1, GPIO.HIGH) # Turn on
            sleep(1)                     # Sleep for 1 second
            GPIO.output(pin1, GPIO.LOW)  # Turn off
            sleep(1)                     # Sleep for 1 second
         if ITER_COUNT == 0:
            break
except:
   print("error")
GPIO.cleanup()
