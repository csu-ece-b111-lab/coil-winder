#coilwinder project
import sys
import RPi.GPIO as GPIO
import time

#setup GPIO ports motors
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)



#setup pwm for core motor (port,frequency in Hz)
p = GPIO.PWM(12,100)
a = GPIO.PWM(36,100)

#setup pwm for moving motor(port, frequency om Hz)
b = GPIO.PWM(33,500)
c = GPIO.PWM(35,500)

#start pwm ports
p.start(1)
a.start(1)
#b.start(1)
c.start(1)


while 1:
	wiregauge =int(input('Wire Gauge:  '))
	if(wiregauge == 12):
		print('12gauge')
	if(wiregauge == 14):
		print('14gauge')
	if(wiregauge == 16):
		print('16gauge')
	if(wiregauge == 18):
		print('18gauge')

print ('hello world')



