import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

rate = float(input("pick a blink rate"))
timeLength = float(input("length of time"))

int counter = 0


