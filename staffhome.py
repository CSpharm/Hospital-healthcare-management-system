import sqlite3
from tkinter import *
from maptbasic import WindowForMan_ptbasic
from mastabasic import WindowForMan_stabasic
from addGP import WindowForaddGP

# connect to the database on register page
conn_staff_home = sqlite3.connect('Database.db')
c_staff_home = conn_staff_home.cursor()

class WindowForstaffHome:
    def __init__(self,staffh,val28):
        self.staffh = staffh
        self.staffID = val28

        # create a frame
        self.leftsth = Frame(staffh, width=630, height = 720, bg='pink')
        self.leftsth.pack(side=LEFT)
        self.rightsth = Frame(staffh, width= 570, height = 720, bg = 'lightblue')
        self.rightsth.pack(side=RIGHT)

        # headings
        self.lhh = Label(self.leftsth, text="Welcome to UCLH staff home.",font = ('arial 40 bold'),fg='black',bg='pink')
        self.lhh.place(x=0,y=0)

        # Buttons for staff
        # Button to manage ptbasic
        self.bu_man_ptbasic = Button(self.leftsth, text='Manage patients basic files', width=25, height=2, bg='white', command=self.man_ptbasic)
        self.bu_man_ptbasic.place(x=200, y=150)

        # Button to manage staffbasic
        self.bu_man_stabasic = Button(self.leftsth, text='Manage staff basic files', width=25, height=2, bg='white', command=self.man_stabasic)
        self.bu_man_stabasic.place(x=200, y=300)

        re_staID = c_staff_home.execute("SELECT staffID from staffbasic WHERE isDr = 1")
        # Buttons for Dr.
        for staID in re_staID:
            if int(self.staffID) == int(staID[0]):
                self.bu_addGP = Button(self.rightsth, text='Add new GP', width=25, height=2, bg='white',
                                       command=self.addGP)
                self.bu_addGP.place(x=200, y=150)
                self.bu_appapp = Button(self.rightsth, text="Manage patients' prescription" , width=25, height=2, bg='white',
                                        command=self.appapp)
                self.bu_appapp.place(x=200, y=300)
                self.bu_pres = Button(self.rightsth, text='Approve appointments', width=25, height=2, bg='white',
                                      command=self.pres)
                self.bu_pres.place(x=200, y=450)

    def man_ptbasic(self):
        # create the object
        root5 = Tk()
        r5 = WindowForMan_ptbasic(root5, self.staffID)

        # resolution of the window
        root5.geometry('1200x720+0+0')

        # preventing the resize feature
        root5.resizable(False, False)

        # end the loop
        root5.mainloop()

    def man_stabasic(self):

        root6 = Tk()
        r6 = WindowForMan_stabasic(root6, self.staffID)

        # resolution of the window
        root6.geometry('1200x720+0+0')

        # preventing the resize feature
        root6.resizable(False, False)

        # end the loop
        root6.mainloop()

    def addGP(self):

        root7 = Tk()
        r7 = WindowForaddGP(root7)

        # resolution of the window
        root7.geometry('1200x720+0+0')

        # preventing the resize feature
        root7.resizable(False, False)

        # end the loop
        root7.mainloop()

    def appapp(self):
        pass

    def pres(self):
        pass