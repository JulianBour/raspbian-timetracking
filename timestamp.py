#!/usr/bin/env python
from datetime import datetime

## TODO evtl object; (day,month,year,calendarweek,time)
def currentTimestamp():
	timestamp = datetime.now()
	day = timestamp.day
	month = timestamp.month
	year = timestamp.year
	calendarweek = timestamp.date().isocalendar()[1]
	time = timestamp.time()
	time = time.strftime("%H:%M:%S")
	return (day, month, year, calendarweek, time)
