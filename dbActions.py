#!/usr/bin/env python
import MySQLdb
import timestamp
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
	"time_difference time)"
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
		print 'Time logged!'
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
## TODO inhalt von cursor richtig abfangen (in hh:mm:ss umwandeln, hat momentan (x, SEKUNDENANZAHL)
	print "here"
	for item in cursor:
		print item
	query = "UPDATE " + tableName + " SET logout_time=\'" + timeString + "\',is_logged_in=0 WHERE is_logged_in=1"
	success = cursor.execute(query)
