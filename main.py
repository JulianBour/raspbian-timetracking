#!/usr/bin/env python
import tagio
import time
import timestamp
import dbActions

connection = dbActions.getConnection()

#endless loop for continuous reading
#replace user by staff
while 1:
	#read staff tag
	staffId = tagio.read()
	name,prename,id = staffId.split("-")
	#remove unnecessary characters
	id = id[:3]
	#generate db table name for the current user
	userTable = name + "_" + prename + "_" + id
	#create new table if db table does not exist
	if not dbActions.checkIfUserTableAlreadyExists(connection, userTable):
		dbActions.createUserTable(connection, userTable)
	#log time if table already exist
	else:
		###TODO remove 'print' for final version
		print('Timetable already exists and time will be logged now.')
		staffIsLoggedIn = dbActions.staffIsLoggedIn(connection, userTable)
		print(staffIsLoggedIn)
		if staffIsLoggedIn > 0:
			dbActions.staffLogout(connection, userTable)
			print(staffIsLoggedIn)
		else:
			dbActions.addNewRecord(connection, userTable)



	#system pause 
	###TODO set on 5 sec for final version 
	time.sleep(2)

