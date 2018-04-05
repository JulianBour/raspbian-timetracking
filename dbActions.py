#!/usr/bin/env python
import MySQLdb
import timestamp
from datetime import datetime
import time

def getConnection():
	db = MySQLdb.connect(host="localhost",
                     user="ambimax",
                     passwd="20ambimax08",
                     db="ambimax_timetracking")
	return db

def checkIfUserTableAlreadyExists(db, tableName):
	cursor = db.cursor()
	query = "SHOW TABLES LIKE " + '\'' + tableName + '\''
	tableExists = cursor.execute(query)
	cursor.close()
	return tableExists

def createUserTable(db, tableName):
	cursor = db.cursor()
	##TODO add 'id' for search stuff
	query = "CREATE TABLE " + tableName  + " (day int(2), month int(2), year int(4),"\
	"calendar_week tinyint(2), login_time time, logout_time time, is_logged_in tinyint(1),"\
	"time_at_work time)"
	cursor.execute(query)
	print 'Successfully created ' + tableName
	cursor.close()

def addNewRecord(db, tableName):
	timeArray = timestamp.currentTimestamp()
	cursor = db.cursor()
	query = "INSERT INTO " + tableName + " (day,month,year,calendar_week,login_time,"\
	"is_logged_in) VALUES (" +\
	str(timeArray[0]) + "," + str(timeArray[1]) +"," + str(timeArray[2]) + "," +\
	str(timeArray[3]) + "," + "\'" + timeArray[4] + "\'" + ", 1)"
	success = cursor.execute(query)
	db.commit()
	if success:
		print 'Successfully logged in!'
	else:
		print 'Something went wrong during Logging in! Please contact jb@ambimax.de'
	cursor.close()

def staffIsLoggedIn(db, tableName):
	cursor = db.cursor()
	query = "SELECT is_logged_in FROM " + tableName + " WHERE is_logged_in=1"
	success = cursor.execute(query)
	return success

def staffLogout(db, tableName):
	timeString = timestamp.currentTimestamp()[4]
	cursor = db.cursor()
	query = "SELECT login_time FROM " + tableName + " WHERE is_logged_in=1"
	cursor.execute(query)
	logInTime = cursor.fetchone()[0]
	deltaTime = timestamp.getCurrentTimeAsDatetime() - logInTime

	query = "UPDATE " + tableName + " SET logout_time=\'" + timeString + "\',is_logged_in=0, time_at_work=\'" +\
	deltaTime.strftime("%H:%M:%S") +  "\'  WHERE is_logged_in=1"
	success = cursor.execute(query)
	if success:
                print 'Successfully logged out!'
        else:
                print 'Something went wrong during logging out! Please contact jb@ambimax.de'
	db.commit()
        cursor.close()
