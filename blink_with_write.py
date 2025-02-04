import RPi.GPIO as GPIO
import time
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
import sys


DEBUG = False
if (len(sys.argv)> 1): DEBUG = True if (int(sys.argv[1])> 0) else False

switchPin = 13
ledPin = 11

GPIO.setup(switchPin, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT, initial = GPIO.LOW)

fileName = "data.txt"


try:
   rate = float(input("pick a blink rate"))
except ValueError:
   print("Invalid input. Using default value of 1.")
   rate = 1

try:
   timeLength = float(input("pick a length of time."))
except ValueError:
   print("Invalid input. Using default value of 10.")
   timeLength = 10
start_time = time.time()


#DEBUG = False
#if '--debug' in sys.argv:
   #DEBUG = TRUE
input_state = GPIO.input(switchPin)
while (time.time() - start_time) < timeLength:
   with open(fileName, "a") as file:
         input_state = GPIO.input(switchPin)
         delta = time.time() - start_time
         file.write(f"{delta}\t{input_state}\n")
         if DEBUG:
            print(f'LED is on: {input_state}\n')
         if input_state == GPIO.HIGH:
            GPIO.output(ledPin, GPIO.HIGH)
            sleep(.5/rate)
            GPIO.output(ledPin, GPIO.LOW)
            sleep(.5/rate)

GPIO.cleanup()


