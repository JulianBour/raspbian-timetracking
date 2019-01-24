import sys
sys.path.append("/var/projects/raspbian-timetracking/timetracking")

import alogging as alogging
import fingerprint as fp
import userManagement as um
import ttk as ttk
from Tkinter import *
from FullScreen import *
from Functions import *
from main import *
import time as time

#Create database table before start
alogging.createTableIfNotExists()

#Fenster erstellen
root=Tk()

#CONST
MAXWIDTH = root.winfo_screenwidth()
MAXHEIGHT = root.winfo_screenheight()
ORANGE = '#f4811e'
BLACK = '#000000'
WHITE = '#FFFFFF'
GREY = '#949191'
RED = '#FF0000'

###Frames erstellen
#Head frame
standardHead = Frame(root, width = MAXWIDTH, height = MAXHEIGHT * 0.2 )
standardHead["bg"] = ORANGE
adminHead = Frame(root, width = MAXWIDTH, height = MAXHEIGHT * 0.2 )
adminHead["bg"] = RED
#Body frame
body = Frame(root, width = MAXWIDTH, height = MAXHEIGHT * 0.6 )
body["bg"] = GREY
#Footer frame
footer = Frame(root, width = MAXWIDTH, height = MAXHEIGHT * 0.2 )
footer["bg"] = ORANGE
#Frames platzieren
standardHead.pack( side=TOP )
footer.pack( side=BOTTOM )
body.pack( side=BOTTOM )

###Buttons
#Standard Buttons
LogFooterButton = Button(standardHead, text='Admin', width = 7, height = 2, command = lambda: createAdminHead(),\
                font = ("Helvetica", int(MAXHEIGHT * 0.05)))
loginButton = Button(footer, text='Login', width = 7, height = 2, command = lambda: staffLogin(),\
                font = ("Helvetica", int(MAXHEIGHT * 0.05)))
logoutButton = Button(footer, text='Logout', width = 7, height = 2, command = lambda: staffLogout(), \
                font = ("Helvetica", int(MAXHEIGHT * 0.05)))
cancelButton = Button(footer, text='Abbruch', width = 7, height = 2, command = lambda: cancel(), \
                font = ("Helvetica", int(MAXHEIGHT * 0.05)))
#Dev Buttons
#TODO remove for final version
devExitButton = Button(standardHead, text='EXIT', width = 7, height = 2, command = lambda: devExit(), \
                font = ("Helvetica", int(MAXHEIGHT * 0.05)))
#Admin Buttons
addFingerprintButton = Button(adminHead, text='Add finger', width = 7, height = 2, command = lambda: addFingerprint(), \
                font = ("Helvetica", int(MAXHEIGHT * 0.05)))
closeAdminHeadButton = Button(adminHead, text='Exit admin', width = 7, height = 2, command = lambda: exitAdminHead(), \
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

def addFingerprint():
    tempUsers = um.getAllStaffNames()


    users = []
    i = 0
    for x in tempUsers:
        users.insert(i, ''.join(x))
        i = i + 1

    tkvar = StringVar(root)
    tkvar.set('SELECT USER')
    popupMenu = ttk.Combobox(body, values = users, height = 10, justify = CENTER, width = 30)
    #popupMenu = OptionMenu(body, tkvar, *users)

    popupMenu.config(font=('Helvetica', 30))
    #menu = popupMenu.nametowidget(popupMenu.menuname)
    #menu.configure(font=('Helvetica', 30))

    popupMenu.place(relx = 0.5,rely = 0.5, anchor = CENTER)




    #TODO show users as buttons
    #for x in users
     #   bodyMessage=x


    #TODO start
    #bodyMessage = fp.addFinger()
    authMessageLabel.config(text=bodyMessage, font = ("Helvetica", int(MAXHEIGHT * 0.05)))

def devExit():
    root.destroy()

def createAdminHead():
    standardHead.pack_forget()
    adminHead.pack( side=TOP )
    addFingerprintButton.place(relx=0, anchor=NW)
    closeAdminHeadButton.place(relx=1, anchor=NE)

def exitAdminHead():
    adminHead.pack_forget()
    standardHead.pack( side=TOP )

def createStandardHead():
    LogFooterButton.place(relx=0, anchor=NW)

    #TOTO remove dev buttons
    devExitButton.place(relx=0.5, anchor=NW)

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
    #TODO alogging.login(staffId)
    #TODO If success then delete label and print success and delete after 5 seconds

#TODO remove function in final version
def logoutAndQuit():
    alogging.logout(5)

#create Footer
createStandardHead()
createStandardFooter()
createStandardBody()


app=FullScreenApp(root)
root.mainloop()
