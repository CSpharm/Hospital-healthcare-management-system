import sqlite3
from tkinter import *
from maptbasic import WindowForMan_ptbasic
from mastabasic import WindowForMan_stabasic
from addGP import WindowForaddGP
from dr_see_appointments import WindowFordrseeappointments
from prescription import WindowForpres
import tkinter.font as tkFont
import tkinter.messagebox


# connect to the database on register page
conn_staff_home = sqlite3.connect('Database.db')
c_staff_home = conn_staff_home.cursor()
li_dr_appID = []

class WindowForstaffHome:
    def __init__(self,staffh,val28):
        self.staffh = staffh
        self.staffID = val28
        self.li_dr_appID = li_dr_appID

        # create a frame
        self.leftsth = Frame(staffh, width=630, height = 720, bg='pink')
        self.leftsth.pack(side=LEFT)
        self.rightsth = Frame(staffh, width= 570, height = 720, bg = 'lightblue')
        self.rightsth.pack(side=RIGHT)

        # create font
        self.F1 = tkFont.Font(family='arial', size='20', weight='bold')
        self.F2 = tkFont.Font(family='arial', size='30', weight='bold')

        # headings
        self.lhh = Label(self.leftsth, text="Welcome to UCLH staff home.",font = self.F2,fg='black',bg='pink')
        self.lhh.place(x=0,y=0)
        # right heading
        self.lhh = Label(self.rightsth, text="Your staffID:"+ str(self.staffID), font= self.F1, fg='black',
                         bg='lightblue')
        self.lhh.place(x=0, y=0)

        # Labels for staff
        self.lbapp = Label(self.rightsth, text="Enter the appointment no." , font=self.F1, fg='black',
                         bg='lightblue')
        self.lbapp.place(x=0, y=300)
        self.lbdisa = Label(self.rightsth, text="Enter the appointment no." , font=self.F1, fg='black',
                         bg='lightblue')
        self.lbdisa.place(x=0, y=400)
        self.lbptID = Label(self.rightsth, text="Enter the patient's NHS no.", font=self.F1, fg='black',
                            bg='lightblue')
        self.lbptID.place(x=0, y=510)

        # Buttons for staff
        # Button to manage ptbasic
        self.bu_man_ptbasic = Button(self.leftsth, text='Manage patients basic files', width=25, height=2, bg='white', command=self.man_ptbasic)
        self.bu_man_ptbasic.place(x=200, y=150)

        # Button to manage staffbasic
        self.bu_man_stabasic = Button(self.leftsth, text='Manage staff basic files', width=25, height=2, bg='white', command=self.man_stabasic)
        self.bu_man_stabasic.place(x=200, y=300)

        c_staff_home.execute("SELECT staffID from staffbasic WHERE isDr = 1 AND staffID = (?)",(self.staffID,))
        # Buttons for Dr.
        self.bu_addGP = Button(self.rightsth, text='Add new GP', width=23, height=2, bg='white',
                               command=self.addGP)
        self.bu_addGP.place(x=320, y=100)
        self.bu_seeapp = Button(self.rightsth, text='Your coming appointments', width=24, height=2, bg='white',
                               command=self.seeapp)
        self.bu_seeapp.place(x=320, y=200)
        self.bu_appapp = Button(self.rightsth, text="Approve appointments" , width=23, height=2, bg='white',
                                command=self.appapp)
        self.bu_appapp.place(x=320, y=300)
        self.bu_disapp = Button(self.rightsth, text="Disapprove appointments", width=23, height=2, bg='white',
                                command=self.disapp)
        self.bu_disapp.place(x=320, y=400)
        self.bu_pres = Button(self.rightsth, text="Manage patients' prescription", width=23, height=2, bg='white',
                              command=self.pres)
        self.bu_pres.place(x=320, y=500)

        #Entry for Dr
        self.appapp_ent = Entry(self.rightsth, width=2)
        self.appapp_ent.place(x=200, y=300)
        self.disapp_ent = Entry(self.rightsth, width=2)
        self.disapp_ent.place(x=200, y=400)
        self.ptID_ent = Entry(self.rightsth, width=11)
        self.ptID_ent.place(x=190, y=505)

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
        root7.geometry('630x720+0+0')

        # preventing the resize feature
        root7.resizable(False, False)

        # end the loop
        root7.mainloop()

    def seeapp(self):
        root8 = Tk()
        r8 = WindowFordrseeappointments(root8,self.staffID)

        # resolution of the window
        root8.geometry('650x150+0+0')

        # preventing the resize feature
        root8.resizable(True,True)

        # end the loop
        root8.mainloop()

    def appapp(self):
        self.val50 = self.appapp_ent.get()
        self.li_dr_appID = []

        re_app = c_staff_home.execute(
            "SELECT appID FROM appointments WHERE DrID=(?) AND isApproved = 1 ",(self.staffID,))

        for re in re_app:
            self.li_dr_appID.append(int(re[0]))

        if self.val50 == '':
            tkinter.messagebox.showinfo('Warning', 'Please enter the box.')

        elif (int(self.val50) not in self.li_dr_appID):
            tkinter.messagebox.showinfo('Warning', ' Invalid appointment number. Please check again.')
        else:
            c_staff_home.execute("UPDATE appointments SET isApproved = 2 WHERE appID = (?)", (self.val50,))
            conn_staff_home.commit()
            tkinter.messagebox.showinfo('Confirmation', ' Successful!')

    def disapp(self):
        self.val51 = self.disapp_ent.get()
        self.li_dr_appID = []

        re_disap = c_staff_home.execute(
            "SELECT appID FROM appointments WHERE DrID=(?) AND isApproved = 1", (self.staffID,))

        for re in re_disap:
            self.li_dr_appID.append(int(re[0]))

        if self.val51 == '':
            tkinter.messagebox.showinfo('Warning', 'Please enter the box.')

        elif (int(self.val51) not in self.li_dr_appID):
            tkinter.messagebox.showinfo('Warning', ' Invalid appointment number. Please check again.')

        else:
            c_staff_home.execute("UPDATE appointments SET isApproved = 0 WHERE appID = (?)", (self.val51,))
            conn_staff_home.commit()
            tkinter.messagebox.showinfo('Confirmation', ' Successful!')

    def pres(self):
        self.val52 = self.ptID_ent.get()

        root9 = Tk()
        r9 = WindowForpres(root9, self.val52, self.staffID)

        # resolution of the window
        root9.geometry('1200x720+0+0')

        # preventing the resize feature
        root9.resizable(True, True)

        # end the loop
        root9.mainloop()