#!/usr/bin/env python
import logging


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
	if not dbActions.checkIfUserTableAlreadyExists(connection, userTable):
		dbActions.createUserTable(connection, userTable)
	#log time if table already exist
	else:
		staffIsLoggedIn = dbActions.staffIsLoggedIn(connection, userTable)
		if staffIsLoggedIn > 0:
			dbActions.staffLogout(connection, userTable)
		else:
			dbActions.addNewRecord(connection, userTable)


	#system pause 
	###TODO set on 5 sec for final version 
	time.sleep(2)

