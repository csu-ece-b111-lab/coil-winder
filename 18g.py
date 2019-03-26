#coilwinder project
#28gauge wire original core size
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
b = GPIO.PWM(33,20)
c = GPIO.PWM(35,20)




while 1:
	com = input('Type stop to stop :  ')
	print('28gauge')
	p.start(1)
	a.start(1)
	c.start(1)
	if(com == 'stop'):
		break



