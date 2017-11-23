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

(options, args) = op.parse_args()
count = 0
trig = int(options.trig)
period = float(options.period)
print("Period: ", str(period), " Trig: ", str(trig))

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
	time.sleep(period)
	if(GPIO.input(23) ==1):
		count = 0
	else:
		count+=1
	if(count >= trig):
		print("shotdown")
		time.sleep(1)
		call("sudo shutdown -h now", shell=True)
	else:
		print("count: ", str(count), "/", str(trig))		
