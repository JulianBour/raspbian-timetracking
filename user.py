#!/usr/bin/env python
import MySQLdb
import datetime

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
	time_now = datetime.datetime.now()
	print time_now
	cursor = db.cursor()
	query = "INSERT INTO " + tableName + " (day,month,year,calendar_week,login_time,"\
	"logout_time,is_logged_in,time_difference) VALUES "\
	 "(1,3,2018,12, \'02:23:10\',\'12:02:12\',0,\'00:06:01\')"
	print query
	success = cursor.execute(query)
	db.commit()
	if success:
		print 'Time logged!'
	cursor.close()
