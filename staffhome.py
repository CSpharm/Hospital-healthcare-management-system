import sqlite3
from tkinter import *
import tkinter.font as tkFont
import tkinter.messagebox

from staff_maptbasic import WindowForMan_ptbasic
from staff_mastabasic import WindowForMan_stabasic
from admin_addGPadmin import WindowForaddGPadmin
from admin_confirm_pt_reg import WindowForConfirmPtReg

from dr_appointmentDate import WindowForappDate
from dr_see_appointments import WindowFordrseeappointments
from dr_prescription import WindowForpres
from dr_delete_due_app import WindowFordeletedueapp


class WindowForstaffHome:
    def __init__(self,staffh,staffID):
        self.staffh = staffh
        self.staffID = staffID

        # frame
        self.leftsth = Frame(staffh, width=530, height = 720, bg='pink')
        self.leftsth.pack(side=LEFT)
        self.rightsth = Frame(staffh, width= 670, height = 720, bg = 'lightblue')
        self.rightsth.pack(side=RIGHT)

        # create font
        self.f1 = tkFont.Font(family='times', size='16')

        # headings
        self.lh1 = Label(self.leftsth, text="Welcome to UCLH staff home.",font = self.f1,fg='black',bg='pink')
        self.lh1.place(x=0,y=0)
        self.lh2 = Label(self.leftsth, text="Your staffID:"+ str(self.staffID), font= self.f1, fg='black',
                         bg='pink')
        self.lh2.place(x=0, y=50)

        # page for admin
        conn_admin = sqlite3.connect('Database.db')
        c_admin = conn_admin.cursor()

        re_admin = c_admin.execute("SELECT staffID from staffbasic WHERE isDr = 0 AND staffID = (?)", (self.staffID,))

        for r_admin in re_admin:

            # Labels for admin
            self.ldeaGP = Label(self.leftsth, text="Enter the DrID:", font=self.f1, fg='black', bg='pink')
            self.ldeaGP.place(x=10, y=415)
            self.ldelGP = Label(self.leftsth, text="Enter the DrID:", font=self.f1, fg='black', bg='pink')
            self.ldelGP.place(x=10, y=495)

            # Entry for admin
            self.deacdrID_ent = Entry(self.leftsth, width=6)
            self.deacdrID_ent.place(x=150, y=415)
            self.deldrID_ent = Entry(self.leftsth, width=6)
            self.deldrID_ent.place(x=150, y=495)

            # Buttons for admin
            self.bu_confirm = Button(self.leftsth, text="Confirm patients' registration", width=23, height=2,
                                     bg='white', command=self.con_pt_reg)
            self.bu_confirm.place(x=250, y=90)
            self.bu_admin_man_ptbasic = Button(self.leftsth, text='Manage patients basic files', width=22, height=2,
                                               bg='white', command=self.man_ptbasic)
            self.bu_admin_man_ptbasic.place(x=250, y=170)

            self.bu_admin_man_stabasic = Button(self.leftsth, text='Manage your basic files', width=22, height=2,
                                                bg='white', command=self.man_stabasic)
            self.bu_admin_man_stabasic.place(x=250, y=250)
            self.bu_addGP = Button(self.leftsth, text='Add new GP and admin', width=22, height=2, bg='white',
                                   command=self.addGP_admin)
            self.bu_addGP.place(x=250, y=330)
            self.bu_addGP = Button(self.leftsth, text='Deactivate GP', width=22, height=2, bg='white',
                                   command=self.deactGP)
            self.bu_addGP.place(x=250, y=410)
            self.bu_addGP = Button(self.leftsth, text='Delete GP', width=22, height=2, bg='white',
                                   command=self.delGP)
            self.bu_addGP.place(x=250, y=490)

        conn_admin.commit()
        conn_admin.close()

        # page for dr
        conn_staff_home = sqlite3.connect('Database.db')
        c_staff_home = conn_staff_home.cursor()

        re_staff = c_staff_home.execute("SELECT staffID from staffbasic WHERE isDr = 1 AND staffID = (?)",(self.staffID,))

        for r_sta in re_staff:

            # Labels for Dr
            self.ldetail = Label(self.rightsth, text="The columns are appointment no, pt's NHS no,\n "
                                                     "pt's name,appointment date,\n and approved state in order ",
                                 font=self.f1, fg='black',bg='lightblue')
            self.ldetail.place(x=0, y=200)
            self.lbapp = Label(self.rightsth, text="Enter the appointment no.", font=self.f1, fg='black',
                               bg='lightblue')
            self.lbapp.place(x=0, y=300)
            self.lbdisa = Label(self.rightsth, text="Enter the appointment no.", font=self.f1, fg='black',
                                bg='lightblue')
            self.lbdisa.place(x=0, y=400)
            self.lbptID = Label(self.rightsth, text="Enter the patient's NHS no.", font=self.f1, fg='black',
                                bg='lightblue')
            self.lbptID.place(x=0, y=510)

            # Entry for Dr
            self.appapp_ent = Entry(self.rightsth, width=2)
            self.appapp_ent.place(x=200, y=300)
            self.disapp_ent = Entry(self.rightsth, width=2)
            self.disapp_ent.place(x=200, y=400)
            self.ptID_ent = Entry(self.rightsth, width=11)
            self.ptID_ent.place(x=190, y=505)

            # Buttons for Dr.
            self.bu_dr_man_ptbasic = Button(self.leftsth, text='Manage patients basic files', width=22, height=2,
                                               bg='white', command=self.man_ptbasic)
            self.bu_dr_man_ptbasic.place(x=250, y=170)
            self.bu_admin_man_stabasic = Button(self.leftsth, text='Manage your basic files', width=22, height=2,
                                                bg='white', command=self.man_stabasic)
            self.bu_admin_man_stabasic.place(x=250, y=250)

            self.bu_manDate = Button(self.rightsth, text='Manage my available date', width=23, height=2, bg='white',
                                   command=self.addDate)
            self.bu_manDate.place(x=400, y=100)
            self.bu_seeapp = Button(self.rightsth, text='My coming appointments', width=24, height=2, bg='white',
                                    command=self.seeapp)
            self.bu_seeapp.place(x=400, y=200)
            self.bu_appapp = Button(self.rightsth, text="Approve appointments", width=23, height=2, bg='white',
                                    command=self.appapp)
            self.bu_appapp.place(x=400, y=300)
            self.bu_disapp = Button(self.rightsth, text="Disapprove appointments", width=23, height=2, bg='white',
                                    command=self.disapp)
            self.bu_disapp.place(x=400, y=400)
            self.bu_pres = Button(self.rightsth, text="Manage patients' prescription", width=23, height=2, bg='white',
                                  command=self.pres)
            self.bu_pres.place(x=400, y=500)
            self.bu_deldueapp = Button(self.rightsth, text="Delete due appointments", width=23, height=2, fg='black',
                                       command=self.deldueapp)
            self.bu_deldueapp.place(x=400, y=590)

        conn_staff_home.commit()
        conn_staff_home.close()

    def con_pt_reg(self):

        rootcon = Tk()
        WindowForConfirmPtReg(rootcon, self.staffID)

        # resolution of the window
        rootcon.geometry('700x500+0+0')

        # preventing the resize feature
        rootcon.resizable(False, False)

        # end the loop
        rootcon.mainloop()

    def man_ptbasic(self):

        # create the object
        root_ptbasic = Tk()
        WindowForMan_ptbasic(root_ptbasic , self.staffID)

        # resolution of the window
        root_ptbasic .geometry('1200x720+0+0')

        # preventing the resize feature
        root_ptbasic .resizable(False, False)

        # end the loop
        root_ptbasic .mainloop()

    def man_stabasic(self):

        # create the object
        root_stabasic = Tk()
        WindowForMan_stabasic(root_stabasic, self.staffID)

        # resolution of the window
        root_stabasic.geometry('1200x720+0+0')

        # preventing the resize feature
        root_stabasic.resizable(False, False)

        # end the loop
        root_stabasic.mainloop()

    def addGP_admin(self):

        root_addGP = Tk()
        WindowForaddGPadmin(root_addGP)

        # resolution of the window
        root_addGP.geometry('630x720+0+0')

        # preventing the resize feature
        root_addGP.resizable(False, False)

        # end the loop
        root_addGP.mainloop()

    def deactGP(self):

        try:
            self.val_deact = int(self.deacdrID_ent.get())

        except ValueError:
            tkinter.messagebox.showinfo('Warning', 'The number should be an integer.')

        else:
            # find the active drs
            conn_act = sqlite3.connect('Database.db')
            c_act = conn_act.cursor()
            li_act_dr = []

            re_act = c_act.execute("SELECT staffID FROM staffbasic WHERE (isDr =1) AND (isactivated = 1)")
            for result in re_act:
                li_act_dr.append(result[0])

            conn_act.commit()
            conn_act.close()

            if self.val_deact not in li_act_dr:
                tkinter.messagebox.showinfo('Warning', 'You can not deactivate this GP.')

            else:
                # deactivate the GP
                conn_deact = sqlite3.connect('Database.db')
                c_deact = conn_deact.cursor()

                c_deact.execute("UPDATE staffbasic SET isactivated = 0 WHERE staffID = (?) ", (self.val_deact,))
                conn_deact.commit()
                conn_deact.close()
                tkinter.messagebox.showinfo('Confirmation', ' Successful.')

    def delGP(self):

        try:
            self.val_deldrID = int(self.deldrID_ent.get())

        except ValueError:
            tkinter.messagebox.showinfo('Warning', 'The number should be an integer.')

        else:
            # find the drID
            conn_drID = sqlite3.connect('Database.db')
            c_drID = conn_drID.cursor()

            li_drID = []
            re_drID = c_drID.execute("SELECT staffID FROM staffbasic WHERE isDr = 1 ")
            for result in re_drID:
                li_drID.append(result[0])

            conn_drID.commit()
            conn_drID.close()

            if self.val_deldrID not in li_drID:
                tkinter.messagebox.showinfo('Warning', 'Invalid ID.')

            else:
                # delete the GP
                conn_del = sqlite3.connect('Database.db')
                c_del = conn_del.cursor()

                c_del.execute("DELETE FROM staffbasic WHERE staffID = (?) ", (self.val_deldrID,))
                conn_del.commit()
                conn_del.close()
                tkinter.messagebox.showinfo('Confirmation', ' Successful.')

    def addDate(self):

        root_addDate = Tk()
        WindowForappDate(root_addDate, self.staffID)

        # resolution of the window
        root_addDate.geometry('630x720+0+0')

        # preventing the resize feature
        root_addDate.resizable(False, False)

        # end the loop
        root_addDate.mainloop()

    def seeapp(self):

        root_see_app = Tk()
        WindowFordrseeappointments(root_see_app,self.staffID)

        # resolution of the window
        root_see_app.geometry('650x150+0+0')

        # preventing the resize feature
        root_see_app.resizable(True,True)

        # end the loop
        root_see_app.mainloop()

    def appapp(self):

        try:
            self.val50 = int(self.appapp_ent.get())
            self.li_dr_appID1 = []

        except ValueError:
            tkinter.messagebox.showinfo('Warning', 'Please enter an integer.')

        else:
            # check the valid appointment no.
            conn_app = sqlite3.connect('Database.db')
            c_app = conn_app.cursor()

            # the drID should be the login staffID , and the isApproved state should be 1
            re_app = c_app.execute("SELECT appID FROM appointments WHERE DrID=(?) AND isApproved = 1 ", (self.staffID,))

            for re in re_app:
                self.li_dr_appID1.append(int(re[0]))

            conn_app.commit()
            conn_app.close()

            if self.val50 not in self.li_dr_appID1:
                tkinter.messagebox.showinfo('Warning', ' Invalid appointment number. Please check again.')

            else:
                # approve the appointment
                conn_appapp = sqlite3.connect('Database.db')
                c_appapp = conn_appapp.cursor()

                c_appapp.execute("UPDATE appointments SET isApproved = 2 WHERE appID = (?)", (self.val50,))
                conn_appapp.commit()
                conn_appapp.close()
                tkinter.messagebox.showinfo('Confirmation', ' Successful!')

    def disapp(self):

        self.li_dr_appID2 = []

        try:
            self.val51 = int(self.disapp_ent.get())

        except ValueError:
            tkinter.messagebox.showinfo('Warning', 'Please enter an integer.')

        else:
            # check the available appointment number (DrID should be the login one and isApproved =1)
            conn_dis = sqlite3.connect('Database.db')
            c_dis = conn_dis.cursor()
            re_disap = c_dis.execute("SELECT appID FROM appointments WHERE DrID=(?) AND isApproved = 1", (self.staffID,))

            for re in re_disap:
                self.li_dr_appID2.append(int(re[0]))

            conn_dis.commit()
            conn_dis.close()

            if self.val51 not in self.li_dr_appID2:
                tkinter.messagebox.showinfo('Warning', 'Invalid appointment number. Please check again.')

            else:
                # disapprove the appointment
                conn_disapp = sqlite3.connect('Database.db')
                c_disapp = conn_disapp.cursor()
                c_disapp.execute("UPDATE appointments SET isApproved = 0 WHERE appID = (?)", (self.val51,))

                conn_disapp.commit()
                conn_disapp.close()
                tkinter.messagebox.showinfo('Confirmation', ' Successful!')

    def pres(self):

        try:
            self.val52 = int(self.ptID_ent.get())

        except ValueError:
            tkinter.messagebox.showinfo('Warning', 'Please enter an integer.')

        else:
            # check exist ptID
            conn_p = sqlite3.connect('Database.db')
            c_p = conn_p.cursor()
            self.li_exi_ptID = []

            re_pt_id = c_p.execute("SELECT ptID FROM ptbasic WHERE isconfirmed = 2")
            for r in re_pt_id:
                self.li_exi_ptID.append(r[0])

            conn_p.commit()
            conn_p.close()

            if self.val52 not in self.li_exi_ptID:
                tkinter.messagebox.showinfo('Warning', 'Invalid NHS number.')
            else:
                # Link to the prescription page
                root_pres = Tk()
                WindowForpres(root_pres, self.val52, self.staffID)

                # resolution of the window
                root_pres.geometry('1200x720+0+0')

                # preventing the resize feature
                root_pres.resizable(True, True)

                # end the loop
                root_pres.mainloop()

    def deldueapp(self):

        rootdeldue = Tk()
        WindowFordeletedueapp(rootdeldue,self.staffID)

        # resolution of the window
        rootdeldue.geometry('500x500+0+0')

        # preventing the resize feature
        rootdeldue.resizable(False, False)

        # end the loop
        rootdeldue.mainloop()