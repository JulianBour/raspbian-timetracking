#!/usr/bin/env python
import tagio
import time
import user

connection = user.getConnection()

#endless loop for continuous reading
while 1:
	#read staff tag
	staffId = tagio.read()
	name,prename,id = staffId.split("-")
	#remove unnecessary characters
	id = id[:3]
	#generate db table name for the current user
	userTable = name + "_" + prename + "_" + id
	#create new table if db table does not exist
	if not user.checkIfUserTableAlreadyExists(connection, userTable):
		user.createUserTable(connection, userTable)
	#log time if table already exist
	else:
		###TODO remove 'print' for final version
		print 'Timetable already exists and time will be logged now.'
		user.addNewRecord(connection, userTable)
	#system pause 
	###TODO set on 5 sec for final version 
	time.sleep(2)

