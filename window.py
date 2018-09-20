import sys
sys.path.append("/var/projects/raspbian-timetracking/timetracking")

import logging as logging
from Tkinter import *
from FullScreen import *
from Functions import *
from main import *
import time as time

#Create database table before start
logging.createTableIfNotExists()

#Fenster erstellen
root=Tk()

#CONST
MAXWIDTH = root.winfo_screenwidth()
MAXHEIGHT = root.winfo_screenheight()
ORANGE = '#f4811e'
BLACK = '#000000'
WHITE = '#FFFFFF'
GREY = '#949191'

###Frames erstellen
#Head frame
head = Frame(root, width = MAXWIDTH, height = MAXHEIGHT * 0.2 )
head["bg"] = ORANGE
#Body frame
body = Frame(root, width = MAXWIDTH, height = MAXHEIGHT * 0.6 )
body["bg"] = GREY
#Footer frame
footer = Frame(root, width = MAXWIDTH, height = MAXHEIGHT * 0.2 )
footer["bg"] = ORANGE
#Frames platzieren
head.pack( side=TOP )
footer.pack( side=BOTTOM )
body.pack( side=BOTTOM )
#Buttons
loginButton = Button(footer, text='Login', width = 5, height = 2, command = lambda: staffLogin(),\
                font = ("Helvetica", int(MAXHEIGHT * 0.05)))
logoutButton = Button(footer, text='Logout', width = 5, height = 2, command = lambda: logoutAndQuit(), \
                font = ("Helvetica", int(MAXHEIGHT * 0.05)))
cancelButton = Button(footer, text='Abbrechen', width = 5, height = 2, command = lambda: cancel(), \
                font = ("Helvetica", int(MAXHEIGHT * 0.05)))
#TODO def add buttons
###

def cancel():
    clearFooter()
    createFooter()

def createFooter():
    loginButton.place(relx=0, anchor=NW)
    logoutButton.place(relx=1, anchor=NE)

def clearFooter():
    loginButton.destroy()
    cancelButton.destroy()
    logoutButton.destroy()

def staffLogin():
    kp = Label(body , text="Bitte jetzt den Finger auf den Scanner legen")
    kp.place(relx = 0.5,rely = 0.5, anchor = CENTER)
    cancelButton.place(relx = 0.5,rely = 0.5, anchor = CENTER)

    
    
    #TODO staffId = scanner.scanFinger()
    #TODO logging.login(staffId)
    #TODO If success then delete label and print success and delete after 5 seconds
    
def logoutAndQuit():
    logging.logout(5)
    root.destroy()
    

#create Footer
createFooter()

app=FullScreenApp(root)
root.mainloop()
