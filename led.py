#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time

LED = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
try:
	while True:
		GPIO.output(LED, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(LED, GPIO.LOW)
		time.sleep(0.5)
except:
	print("except")
GPIO.cleanup()
