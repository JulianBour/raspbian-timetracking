#!/usr/bin/env python
import tagio
import time
import user

connection = user.getConnection()


while 1:
	staffId = tagio.read()
	name,prename,id = staffId.split("-")
	id = id[:3]
	userTable = name + "_" + prename + "_" + id
	if not user.checkIfUserTableAlreadyExists(connection, userTable):
		user.createUserTable(connection, userTable)
	#TODO remove 'print' for final version
	else:
		print 'Timetable already exists and time will be logged now.'
		user.addNewRecord(connection, userTable)
	time.sleep(2)

