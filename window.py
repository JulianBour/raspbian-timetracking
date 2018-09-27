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
loginButton = Button(footer, text='Login', width = 7, height = 2, command = lambda: staffLogin(),\
                font = ("Helvetica", int(MAXHEIGHT * 0.05)))
logoutButton = Button(footer, text='Logout', width = 7, height = 2, command = lambda: staffLogout(), \
                font = ("Helvetica", int(MAXHEIGHT * 0.05)))
cancelButton = Button(footer, text='Abbruch', width = 7, height = 2, command = lambda: cancel(), \
                font = ("Helvetica", int(MAXHEIGHT * 0.05)))
devExitButton = Button(head, text='EXIT', width = 7, height = 2, command = lambda: devExit(), \
                font = ("Helvetica", int(MAXHEIGHT * 0.05)))
#Labels
bodyMessage="Willkommen"
authMessageLabel = Label(body, text=bodyMessage, font = ("Helvetica", int(MAXHEIGHT * 0.1)))
#TODO def add buttons
###

def cancel():
    clearLogFooter()
    createStandardFooter()
    createStandardBody()

def devExit():
    root.destroy()

def createStandardBody():
    bodyMessage="Willkommen"
    authMessageLabel.config(text=bodyMessage, font = ("Helvetica", int(MAXHEIGHT * 0.1)))
    authMessageLabel.place(relx = 0.5,rely = 0.5, anchor = CENTER)

def createLogFooter():
    cancelButton.place(relx = 0.4,rely = 0, anchor = NW)

def clearLogFooter():
    cancelButton.place_forget()

def createStandardFooter():
    loginButton.place(relx=0, anchor=NW)
    logoutButton.place(relx=1, anchor=NE)

def clearStandardFooter():
    loginButton.place_forget()
    logoutButton.place_forget()

def staffLogin():
    bodyMessage="Bitte jetzt den Finger auf den Scanner legen"
    authMessageLabel.config(text=bodyMessage, font = ("Helvetica", int(MAXHEIGHT * 0.05)))

    clearStandardFooter()
    createLogFooter()

def staffLogout():
    bodyMessage="Bitte jetzt den Finger auf den Scanner legen"
    authMessageLabel.config(text=bodyMessage, font = ("Helvetica", int(MAXHEIGHT * 0.05)))

    clearStandardFooter()
    createLogFooter()

    #TODO staffId = scanner.scanFinger()
    #TODO logging.login(staffId)
    #TODO If success then delete label and print success and delete after 5 seconds

#TODO remove function in final version
def logoutAndQuit():
    logging.logout(5)

#create Footer
createStandardFooter()
createStandardBody()

#TOTO remove dev buttons
devExitButton.place(relx=0.5, anchor=NW)

app=FullScreenApp(root)
root.mainloop()
