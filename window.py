import sys
sys.path.append("/var/projects/raspbian-timetracking/timetracking")

import logging as logging
from Tkinter import *
from FullScreen import *
from Functions import *
from main import *

#Create database table before start
logging.createTableIfNotExists()

#Fenster erstellen
root=Tk()

#CONST
MAXWIDTH = root.winfo_screenwidth()
MAXHEIGHT = root.winfo_screenheight()

###Frames erstellen
#Head frame
head = Frame(root, width = MAXWIDTH, height = MAXHEIGHT * 0.2 )
head["bg"] = 'red'
#Body frame
body = Frame(root, width = MAXWIDTH, height = MAXHEIGHT * 0.6 )
body["bg"] = 'green'
#Footer frame
footer = Frame(root, width = MAXWIDTH, height = MAXHEIGHT * 0.2 )
footer["bg"] = 'red'
#Frames platzieren
head.pack( side=TOP )
footer.pack( side=BOTTOM )
body.pack( side=BOTTOM )

def loginAndQuit():
    logging.login(5)
    root.destroy()

def logoutAndQuit():
    logging.logout(5)
    root.destroy()
    
###Buttons
#Login Button
login = Button(footer, text='Login', width = 5, height = 2, command = lambda: loginAndQuit(), \
               font = ("Helvetica", int(MAXHEIGHT * 0.05)))
login.place(relx=0, anchor=NW)

#Logout Button
logout = Button(footer, text='Logout', width = 5, height = 2, command = lambda: logoutAndQuit(), \
               font = ("Helvetica", int(MAXHEIGHT * 0.05)))
logout.place(relx=1, anchor=NE)


app=FullScreenApp(root)
root.mainloop()
