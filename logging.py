#!/usr/bin/env python
import MySQLdb
import timestamp
from datetime import datetime
import time

TABLE_NAME = "timetracking"

def getConnection():
	db = MySQLdb.connect(host="localhost",
                     user="ambimax",
                     passwd="20ambimax18",
                     db="ambimax_management")
	return db

def executeQuery(query):
        db = getConnection()
        cursor = db.cursor()
        success = cursor.execute(query)
        db.commit()
	cursor.close()
	db.close()
	return success

def createTableIfNotExists():
        query = "CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " (log_id int NOT NULL auto_increment, staff_id int(3), " \
	"log_in datetime, log_out datetime, PRIMARY KEY (log_id))"
        executeQuery(query)

def login(staffId):
	query = "INSERT INTO " + TABLE_NAME + " (staff_id, log_in) VALUES (" + str(staffId) + ", NOW())"
	success = executeQuery(query)
	if success:
		print 'Successfully logged in!'
	else:
		print 'Something went wrong during logging in! Please contact pk@ambimax.de'

def logout(staffId):
	query = "INSERT INTO " + TABLE_NAME + " (staff_id,log_out) VALUES (" + str(staffId) + ", NOW())"
	success = executeQuery(query)
	if success:
		print 'Successfully logged out!'
	else:
		print 'Something went wrong during logging out! Please contact pk@ambimax.de'
