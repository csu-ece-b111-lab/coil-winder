#coilwinder project
import sys
import RPi.GPIO as GPIO
import time
import 28g
while 1:
	wiregauge =int(input('Wire Gauge(28ga or 18ga):  '))
	if(wiregauge == 28 ):
		28g.start()
	if(wiregauge == 14):
		print('14gauge')
	if(wiregauge == 16):
		print('16gauge')
	if(wiregauge == 18):
		print('18gauge')

print ('program stopping')



