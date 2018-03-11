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
