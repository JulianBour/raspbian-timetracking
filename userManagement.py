#!/usr/bin/env python
import MySQLdb

def getConnection():
	db = MySQLdb.connect(host="localhost",
                     user="ambimax",
                     passwd="20ambimax18",
                     db="ambimax_management")
	return db

def getNumberOfUsers():
    query = "select * from users"

    db = getConnection()
    cursor = db.cursor()
    numberOfUsers = cursor.execute(query)
    cursor.close()
    db.close()

    return numberOfUsers

def getUserName(userID):
    query="select name from users"

    db = getConnection()
    cursor = db.cursor()
    cursor.execute(query)
    allUserNames = cursor.fetchall()

    userName = ''.join(allUserNames[userID - 1])

    cursor.close()
    db.close()

    return userName

def getAllStaffNames():
    query="select name from users"

    db = getConnection()
    cursor = db.cursor()
    cursor.execute(query)
    allUserNames = cursor.fetchall()

    cursor.close()
    db.close()

    return allUserNames