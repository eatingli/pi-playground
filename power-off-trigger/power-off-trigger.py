#!/usr/bin/python3
from subprocess import call
from optparse import OptionParser
import time
import RPi.GPIO as GPIO

op = OptionParser()
op.add_option("-t", "--trig", dest="trig", default=10,
                  help="count times to showdown")
op.add_option("-p", "--period", dest="period", default=5,
                  help="period of counting (second)")
op.add_option("-g", "--gpio-pin", dest="gpio_pin", default=23,
                  help="period of counting (second)")

(options, args) = op.parse_args()
count = 0
trig = int(options.trig)
period = float(options.period)
gpio_pin = int(options.gpio_pin)
print( "Pin: ", str(gpio_pin), "Period: ", str(period), " Trig: ", str(trig))

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	time.sleep(period)
	if(GPIO.input(gpio_pin) ==1):
		count = 0
	else:
		count+=1
	if(count >= trig):
		print("shotdown")
		time.sleep(1)
		call("sudo shutdown -h now", shell=True)
	else:
		print("count: ", str(count), "/", str(trig))		
