from tkinter import *
import tkinter.messagebox, datetime
import tkinter.font as tkFont
import sqlite3
from pt_see_appointments import WindowtoseeAppointments

today = datetime.date.today()
t = str(today).split('-')

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

        # connect to the database for appointments
        conn_ptlo = sqlite3.connect('Database.db')
        # create a cursor
        c_ptlo = conn_ptlo.cursor()
        re_ptloginname = c_ptlo.execute("SELECT ptName FROM ptbasic WHERE ptID = (?)", (self.userID,))

        for row in re_ptloginname:
            ptloginname = row[0]

        self.ptloginname = ptloginname
        self.ptname = Label(self.left2, text="Patient's Name: " + self.ptloginname, font=self.f1, fg='black',bg='pink')
        self.ptname.place(x=0, y=100)

        conn_ptlo.commit()
        conn_ptlo.close()

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
        self.drid_ent.place(x=155, y=150)
        self.aDno_ent = Entry(self.left2, width=5)
        self.aDno_ent.place(x=155, y=200)

        # Button to add an appointment
        self.submit = Button(self.left2, text='Add appointment', width=15, height=2, bg='white',command=self.add_appointment)
        self.submit.place(x=350, y=250)

        # set a scrollbar
        scrollbar = Scrollbar(self.downLeft)
        scrollbar.pack(side=RIGHT, fill=Y)
        # set a Listbox to fit the downLeft Frame
        drnameList = Listbox(self.downLeft, yscrollcommand=scrollbar.set, width=550, height=350,font=self.f1)

        # connect to the database for appointments
        conn_drname = sqlite3.connect('Database.db')
        # create a cursor
        c_drname = conn_drname.cursor()
        # Print the Dr. and their dates
        dr_namedate = c_drname.execute("SELECT DrName,DrID,available_date,adID FROM appointmentdate ")

        li_adID = []
        for row in dr_namedate:
            name = row[0]
            id = row[1]
            d1 = row[2]
            appointmentDateID = row[3]
            li_adID.append(row[3])
            appD = str(d1).split('-')

            if (appD[0] > t[0]) or (appD[0] == t[0] and appD[1] > t[1]) or (appD[0] == t[0] and appD[1] == t[1] and (appD[2] > t[2])):
                drnameList.insert(END, str(name) + '                ' + str(d1) +'                ' + str(id) +
                                  '          '     + str(appointmentDateID))

        conn_drname.commit()
        conn_drname.close()

        drnameList.pack(side=LEFT, fill = BOTH)
        scrollbar.config(command=drnameList.yview)
        self.li_adID = li_adID

        # right labels
        self.idright = Label(self.right2, text="NHS number: " + str(self.userID), font=self.f1, fg='black', bg='lightgreen')
        self.idright.place(x=0, y=50)
        self.ptname = Label(self.right2, text="Patient's Name: " + ptloginname, font=self.f1, fg='black', bg='lightgreen')
        self.ptname.place(x=0, y=100)
        # cancelling the appointment
        self.appnoenter = Label(self.right2, text="Enter your appointment no.  ", font=self.f1, fg='black', bg='lightgreen')
        self.appnoenter.place(x=0, y=150)
        # entry for right labels
        self.cancelbooking_ent = Entry(self.right2, width = 3)
        self.cancelbooking_ent.place(x=200, y=150)
        # Button to cancel an appointment
        self.cancel = Button(self.right2, text='Cancel appointment', width=15, height=2, bg='white',command=self.cancel_appointment)
        self.cancel.place(x=300, y=150)
        # Button to see appointment detail
        self.see = Button(self.right2, text='See appointments', width=15, height=2, bg='white',command=self.see_appointment)
        self.see.place(x=300, y=350)
        self.seedt = Label(self.right2, text="The columns are the appointment number, the date, the state, and the Dr.name in order." ,
                           font=self.f1, fg='black',bg='lightgreen')
        self.seedt.place(x=0, y=400)

    # Function to see the patient's booking detail
    def see_appointment(self):

        rootsee = Tk()
        r5 = WindowtoseeAppointments(rootsee,self.userID)

        rootsee.geometry('400x200+0+0')
        rootsee.mainloop()


    # Function to call when the submit button is clicked
    def add_appointment(self):

        try :
            self.val12 = int(self.drid_ent.get())
            self.val13 = int(self.aDno_ent.get())
            self.val14 = datetime.datetime.now()

            self.prestuff_check_valid()

            if self.val13 in self.li_dup_adID:
                tkinter.messagebox.showinfo('Warning', 'Duplicate appointment on the same day.')

            elif self.val13 not in self.li_adID:
                tkinter.messagebox.showinfo('Warning', 'Invalid appointment Date no.')

            elif self.dict_IDpairs.get(self.val12)!= self.val13:
                tkinter.messagebox.showinfo('Warning', 'Invalid pairs.')

            else:
                conn_addapp = sqlite3.connect('Database.db')
                c_addapp = conn_addapp.cursor()

                sql2 = "INSERT INTO 'appointments' (ptID, ptName, appointmentTime, isApproved,DrName,DrID," \
                       "systemTime,adID) VALUES(?,?,?,?,?,?,?,?)"
                c_addapp.execute(sql2,(self.userID, self.ptloginname, self.val15, 1, self.val16, self.val12, self.val14,self.val13))
                conn_addapp.commit()
                conn_addapp.close()
                tkinter.messagebox.showinfo('Confirmation', 'Appointment for '+ self.ptloginname + ' has been submitted.')
                self.see_appointment()

        except ValueError:
            tkinter.messagebox.showinfo('Warning', 'Please fill up an integer.')


    def prestuff_check_valid(self):

        # search the appointmentDate using self.val13
        conn_find_date = sqlite3.connect('Database.db')
        c_find_date = conn_find_date.cursor()

        re_find_date = c_find_date.execute("SELECT available_date FROM appointmentDate WHERE adID = (?)",(self.val13,))
        for row in re_find_date:
            self.val15 = row[0]

        conn_find_date.commit()
        conn_find_date.close()

        # Find the Drname by id
        conn_find_name = sqlite3.connect('Database.db')
        c_find_name = conn_find_name.cursor()

        re_dr_ID = c_find_name.execute("SELECT staffname FROM staffbasic WHERE staffID = (?)", (self.val12,))
        for ro in re_dr_ID:
            self.val16 = ro[0]

        conn_find_name.commit()
        conn_find_name.close()

        # calculate the duplicate appointment
        conn_dup = sqlite3.connect('Database.db')
        c_dup = conn_dup.cursor()

        re_isDup = c_dup.execute("SELECT adID FROM appointments WHERE ptID = (?) ", (self.userID,))
        li_dup_adID = []
        for re in re_isDup:
            li_dup_adID.append(re[0])

        conn_dup.commit()
        conn_dup.close()
        self.li_dup_adID = li_dup_adID

        # store the valid drID and their adID in to a dictionary
        conn_IDpairs = sqlite3.connect('Database.db')
        c_IDpairs = conn_IDpairs.cursor()

        re_IDpairs = c_IDpairs.execute("SELECT DrID,adID FROM appointmentDate ")
        dict_IDpairs = {}

        for re in re_IDpairs:
            dict_IDpairs[int(re[0])] = int(re[1])

        conn_IDpairs.commit()
        conn_IDpairs.close()
        self.dict_IDpairs = dict_IDpairs

    # Function to cancel an appointment
    def cancel_appointment(self):

        self.val17 = self.cancelbooking_ent.get()
        cancel_available = []

        # connect to the database for appointments
        conn_cancel = sqlite3.connect('Database.db')
        # create a cursor
        c_cancel = conn_cancel.cursor()

        cancel_list = c_cancel.execute("SELECT appID FROM appointments WHERE isApproved = 1 AND ptID = (?)",(self.userID,))
        for c in cancel_list:
            cancel_available.append(c[0])

        if self.val17 == '' :
            tkinter.messagebox.showinfo('Warning', 'Please fill the box for cancelling.')
        elif int(self.val17) not in cancel_available:
            tkinter.messagebox.showinfo('Warning', 'You can not cancel this appointment.')
        elif not self.val17.isdigit():
            tkinter.messagebox.showinfo('Warning', 'Please enter an integer.')
        else:
            c_cancel.execute("UPDATE appointments SET isApproved = 0 WHERE appID = (?)",(self.val17,))
            conn_cancel.commit()
            conn_cancel.close()
            tkinter.messagebox.showinfo('Confirmation', 'Cancellation for appoint no. ' +str(self.val17)+' is successful.')
            self.see_appointment()