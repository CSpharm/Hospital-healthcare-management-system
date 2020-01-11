import sqlite3
from tkinter import *
import tkinter.messagebox
import tkinter.font as tkFont

import datetime
from pt_see_appointments import WindowtoseeAppointments

class WindowForAppointments:

    def __init__(self,a,val10):

        self.userID = val10
        self.a = a

        # right Frame
        self.right2 = Frame(a, width= 650, height = 720, bg = 'lightgreen')
        self.right2.pack(side=RIGHT)
        # left Frame
        self.left2 = Frame(a, width=550, height=720, bg='pink')
        self.left2.pack(side=LEFT)

        # topLeft Frame
        self.topLeft = Frame(self.left2, width= 550, height = 350, bg = 'pink')
        self.topLeft.pack(side=TOP)
        # downLeft Frame
        self.downLeft = Frame(self.left2, width= 550, height = 350, bg ='pink')
        self.downLeft.pack(side=BOTTOM)

        # create font
        self.f1 = tkFont.Font(family='times', size='16')
        # Left heading
        self.lh2 = Label(self.left2, text="Add Appointments",font =self.f1,fg='black',bg='pink')
        self.lh2.place(x=0,y=0)
        # Right heading
        self.rh2 = Label(self.right2, text="Cancel Appointments", font=self.f1, fg='black', bg='light green')
        self.rh2.place(x=0, y=0)

        # Left labels
        self.id = Label(self.left2, text="NHS number: " + str(self.userID), font=self.f1, fg='black',bg='pink')
        self.id.place(x=0, y=50)

        # Show the pt's name
        self.show_ptname()
        # Show the scrollbar
        self.show_scrollbar()

        # Fixed Left Labels
        # Dr's ID
        self.dridup = Label(self.left2, text="Dr's ID:  ", font=self.f1, fg='black', bg='pink')
        self.dridup.place(x=0, y=150)
        # Appointment Date
        self.dateup = Label(self.left2, text="Appointment Date no.  ", font=self.f1, fg='black', bg='pink')
        self.dateup.place(x=0, y=200)
        self.drnameleftd = Label(self.left2, text="Doctors", font=self.f1, fg='black', bg='pink')
        self.drnameleftd.place(x=0, y=310)
        self.dated = Label(self.left2, text="Date", font=self.f1, fg='black', bg='pink')
        self.dated.place(x=110, y=310)
        self.dridd = Label(self.left2, text="Dr. ID", font=self.f1, fg='black', bg='pink')
        self.dridd.place(x=220, y=310)
        self.laDno = Label(self.left2, text="Appointment Date no.", font=self.f1, fg='black', bg='pink')
        self.laDno.place(x=280, y=310)

        # Entry for left labels
        self.drid_ent = Entry(self.left2, width=6)
        self.drid_ent.place(x=175, y=150)
        self.aDno_ent = Entry(self.left2, width=5)
        self.aDno_ent.place(x=175, y=200)

        # Button to add an appointment
        self.submit = Button(self.left2, text='Add appointment', width=15, height=2, bg='white',command=self.add_appointment)
        self.submit.place(x=350, y=250)

        # right labels
        self.idright = Label(self.right2, text="NHS number: " + str(self.userID), font=self.f1, fg='black', bg='lightgreen')
        self.idright.place(x=0, y=50)
        self.ptname = Label(self.right2, text="Patient's Name: " + self.ptloginname, font=self.f1, fg='black', bg='lightgreen')
        self.ptname.place(x=0, y=100)
        self.appnoenter = Label(self.right2, text="Enter your appointment no.  ", font=self.f1, fg='black', bg='lightgreen')
        self.appnoenter.place(x=0, y=150)

        # entry for right labels
        self.cancelbooking_ent = Entry(self.right2, width = 3)
        self.cancelbooking_ent.place(x=230, y=150)

        # Button to cancel an appointment
        self.cancel = Button(self.right2, text='Cancel appointment', width=15, height=2, bg='white',command=self.cancel_appointment)
        self.cancel.place(x=350, y=150)

        # Button to see appointment detail
        self.see = Button(self.right2, text='See appointments', width=15, height=2, bg='white',command=self.see_appointment)
        self.see.place(x=300, y=350)
        self.seedt = Label(self.right2, text="The columns are the appointment number, the date, the state, and the Dr.name in order." ,
                           font=self.f1, fg='black',bg='lightgreen')
        self.seedt.place(x=0, y=400)

    def show_ptname(self):

        # find ptname using ptID
        # connect to the database for appointments
        conn_ptlo = sqlite3.connect('Database.db')
        c_ptlo = conn_ptlo.cursor()

        re_ptloginname = c_ptlo.execute("SELECT ptName FROM ptbasic WHERE ptID = (?)", (self.userID,))

        for row in re_ptloginname:
            self.ptloginname = row[0]

        # commit and close the db
        conn_ptlo.commit()
        conn_ptlo.close()

        # Label to show the ptname
        self.ptname = Label(self.left2, text="Patient's Name: " + self.ptloginname, font=self.f1, fg='black', bg='pink')
        self.ptname.place(x=0, y=100)

    def show_scrollbar(self):

        # get the date of today
        today = datetime.date.today()
        t = str(today).split('-')

        # set a scrollbar
        scrollbar = Scrollbar(self.downLeft)
        scrollbar.pack(side=RIGHT, fill=Y)

        # set a Listbox to fit the downLeft Frame
        drnameList = Listbox(self.downLeft, yscrollcommand=scrollbar.set, width=550, height=350, font=self.f1)

        # find the appointment details from the DB
        conn_drname = sqlite3.connect('Database.db')
        c_drname = conn_drname.cursor()
        dr_namedate = c_drname.execute("SELECT DrName,DrID,available_date,adID FROM appointmentdate ")

        # create a list to store the valid adIDs
        self.li_adID = []

        for row in dr_namedate:
            name = row[0]
            id = row[1]
            d1 = row[2]
            appointmentDateID = row[3]

            self.li_adID.append(row[3])
            appD = str(d1).split('-')

            # limit the condition to the dates (start from today)
            if (appD[0] > t[0]) or (appD[0] == t[0] and appD[1] > t[1]) \
                    or (appD[0] == t[0] and appD[1] == t[1] and (appD[2] >= t[2])):
                drnameList.insert(END, str(name) + '                ' + str(d1) + '                ' + str(id) +
                                  '            ' + str(appointmentDateID))
        # commit and close the db
        conn_drname.commit()
        conn_drname.close()

        # pack the listbox and configure the scrollbar
        drnameList.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=drnameList.yview)

    def see_appointment(self):

        # see their comming appointments in a new page
        # create a object
        rootsee = Tk()
        WindowtoseeAppointments(rootsee,self.userID)
        rootsee.geometry('400x200+0+0')

        # end the loop
        rootsee.mainloop()

    def add_appointment(self):

        try :
            # get the user inputs
            self.val12 = int(self.drid_ent.get())
            self.val13 = int(self.aDno_ent.get())
            self.val14 = datetime.datetime.now()

            # Check valid or not
            self.check_valid()

            if self.val13 in self.li_dup_adID:
                tkinter.messagebox.showinfo('Warning', 'Duplicate appointment on the same day.')

            elif self.val13 not in self.li_adID:
                tkinter.messagebox.showinfo('Warning', 'Invalid appointment Date no.')

            elif self.val12 not in self.exi_drID:
                tkinter.messagebox.showinfo('Warning', 'Invalid DrID.')

            elif self.dict_IDpairs.get(self.val13)!= self.val12:
                tkinter.messagebox.showinfo('Warning', 'Invalid pairs.')

            else:
                # add an appointment to the DB
                conn_addapp = sqlite3.connect('Database.db')
                c_addapp = conn_addapp.cursor()

                sql2 = "INSERT INTO 'appointments' (ptID, ptName, appointmentTime, isApproved,DrName,DrID," \
                       "systemTime,adID) VALUES(?,?,?,?,?,?,?,?)"
                c_addapp.execute(sql2,(self.userID, self.ptloginname, self.val15, 1, self.val16, self.val12, self.val14,
                                       self.val13))

                # commit and close the DB
                conn_addapp.commit()
                conn_addapp.close()
                # show successful message
                tkinter.messagebox.showinfo('Confirmation','Appointment for '+ self.ptloginname + ' has been submitted.')

                # show upcoming appointments
                self.see_appointment()

        except ValueError:
            # catch non-integer inputs
            tkinter.messagebox.showinfo('Warning', 'Please fill up an integer.')

    def check_valid(self):

        # find the appointmentDate by self.val13
        conn_find_date = sqlite3.connect('Database.db')
        c_find_date = conn_find_date.cursor()
        re_find_date = c_find_date.execute("SELECT available_date FROM appointmentDate WHERE adID = (?)",(self.val13,))

        # store the available date to self.val15
        for row in re_find_date:
            self.val15 = row[0]

        # commit and close the DB
        conn_find_date.commit()
        conn_find_date.close()


        # Find the Drname by self.val12
        conn_find_name = sqlite3.connect('Database.db')
        c_find_name = conn_find_name.cursor()
        re_dr_name = c_find_name.execute("SELECT staffname FROM staffbasic WHERE staffID = (?)", (self.val12,))

        # store the Dr name to self.val16
        for ro in re_dr_name:
            self.val16 = ro[0]

        # commit and close the DB
        conn_find_name.commit()
        conn_find_name.close()

        # calculate the duplicate appointment
        conn_dup = sqlite3.connect('Database.db')
        c_dup = conn_dup.cursor()
        re_isDup = c_dup.execute("SELECT adID FROM appointments WHERE ptID = (?) AND (isApproved != 0)", (self.userID,))

        # create a list to store adID
        self.li_dup_adID = []

        for re in re_isDup:
            self.li_dup_adID.append(re[0])

        # commit and close the DB
        conn_dup.commit()
        conn_dup.close()

        # store the valid drID and their adID in to a dictionary
        conn_IDpairs = sqlite3.connect('Database.db')
        c_IDpairs = conn_IDpairs.cursor()
        re_IDpairs = c_IDpairs.execute("SELECT DrID,adID FROM appointmentDate ")

        # create a dictionary to store adID and DrIDs
        self.dict_IDpairs = {}
        # create a list to store DrIDs
        self.exi_drID = []

        for re in re_IDpairs:
            self.exi_drID.append(re[0])
            self.dict_IDpairs[re[1]] = re[0]

        # commit and close the DB
        conn_IDpairs.commit()
        conn_IDpairs.close()

    # Function to cancel an appointment
    def cancel_appointment(self):

        try:
            self.val17 = self.cancelbooking_ent.get()

            # check if the appointment can be cancelled ( isApproved = 1)
            # create a empty list to store
            cancel_available = []

            conn_check_can = sqlite3.connect('Database.db')
            c_check_can = conn_check_can.cursor()
            cancel_list = c_check_can.execute("SELECT appID FROM appointments WHERE isApproved = 1 AND ptID = (?)",(self.userID,))

            for c in cancel_list:
                cancel_available.append(c[0])

            # commit and close the DB
            conn_check_can.commit()
            conn_check_can.close()

            # Show message if the input is not in the cancel list
            if int(self.val17) not in cancel_available:
                tkinter.messagebox.showinfo('Warning', 'You can not cancel this appointment.')

            else:
                # cancel an appointment
                conn_cancel = sqlite3.connect('Database.db')
                c_cancel = conn_cancel.cursor()
                c_cancel.execute("UPDATE appointments SET isApproved = 0 WHERE appID = (?)", (self.val17,))

                # commit and close the DB
                conn_cancel.commit()
                conn_cancel.close()

                # Show successful message
                tkinter.messagebox.showinfo('Confirmation',
                                            'Cancellation for appoint no. ' + str(self.val17) + ' is successful.')
                # Show upcoming appointments
                self.see_appointment()

        except ValueError:
            tkinter.messagebox.showinfo('Warning', 'Please enter an integer.')

