#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

#write new nfc tag
try:
	name = raw_input('Enter the name ("not" prename):')
	prename = raw_input('Enter the prename:')
	id = raw_input('Enter the ID:')
	print("Now place your tag to set the Staff ID")
	reader.write(name + '-' + prename + '-' + id)
	print("the Staff ID was written")

finally:
	GPIO.cleanup()


