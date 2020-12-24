#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

lightSensorPin = 4
lightPin = 14

GPIO.setmode(GPIO.BCM)

# init light sensor pin status
# set low voltage as init value
GPIO.setup(lightSensorPin, GPIO.OUT)
GPIO.output(lightSensorPin, GPIO.LOW)
time.sleep(0.5)
GPIO.setup(lightSensorPin, GPIO.IN)

# set light pin
GPIO.setup(lightPin, GPIO.OUT)
GPIO.output(lightPin, GPIO.LOW)

try:
  i = 0
  while True:
    v = GPIO.input(lightSensorPin)
    if (v == GPIO.LOW):
      print(f"Oh, lighting {i} times....")
      GPIO.output(lightPin, GPIO.HIGH)
    else:
      GPIO.output(lightPin, GPIO.LOW)
    i = i + 1

except KeyboardInterrupt:
  pass
