#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

#function to read nfc tag
def read():
	reader = SimpleMFRC522.SimpleMFRC522()

	try:
        	chipId, staffId = reader.read()
	finally:
        	GPIO.cleanup()
		return staffId
		
#function to write new staff nfc tag
def write():
	reader = SimpleMFRC522.SimpleMFRC522()
	try:
		name = raw_input('Enter the name ("not" prename):')
	        prename = raw_input('Enter the prename:')
	        id = raw_input('Enter the ID:')
	        print("Now place your tag to set the Staff ID")
	        reader.write(name + '-' + vorname + '-' + id)
	        print("the Staff ID was written")
	finally:
		GPIO.cleanup()
