from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime

# connect to the database for appointments
conn_bookapp = sqlite3.connect('Database.db')

# create a cursor
c_bookapp = conn_bookapp.cursor()

class WindowForAppointments:
    def __init__(self,a,val10):

        self.userID = val10
        self.a = a
        self.d1 = []

        # create a frame
        self.left2 = Frame(a, width=500, height = 720, bg='pink')
        self.left2.pack(side=LEFT)
        self.right2 = Frame(a, width= 700, height = 720, bg = 'lightgreen')
        self.right2.pack(side=RIGHT)

        # heading
        self.lh2 = Label(self.left2, text="Appointments",font = ('arial 40 bold'),fg='black',bg='pink')
        self.lh2.place(x=0,y=0)

        # Fixed Labels
        self.drnameleft = Label(self.left2, text="Doctors", font=('arial 20 bold'), fg='black', bg='pink')
        self.drnameleft.place(x=0, y=80)
        self.date1 = Label(self.left2, text="Date", font=('arial 20 bold'), fg='black', bg='pink')
        self.date1.place(x=250, y=80)

        # Print the Dr. and their dates
        dr_namedate = c_bookapp.execute("SELECT staffName,Date1 FROM staffbasic WHERE isDr = 1 ")
        count = 0
        for row in dr_namedate:
            n = row[0]
            d1 = row[1]
            count += 1
            self.drname = Label(self.left2, text=n, font=('arial 20 bold'), fg='black', bg='pink')
            self.drname.place(x=0, y=50 + 60 * count)
            self.d1.append(Label(self.left2, text=d1, font=('arial 20 bold'),fg='black',bg='pink'))
        count = 1

        for td in self.d1:
            td.place(x=250, y=50 + 60 * count)
            count += 1

        # right labels:NHS number
        self.id = Label(self.right2, text="NHS number:   "+ str(self.userID), font=('arial 17 bold'), fg='black', bg='lightgreen')
        self.id.place(x=0, y=50)

        # right labels:pt name
        re_ptloginname = c_bookapp.execute("SELECT ptID,ptName FROM ptbasic")
        for row in re_ptloginname:
            if row[0] == int(self.userID):
                ptloginname = row[1]

        self.ptname = Label(self.right2, text="Patient's Name:  "+ ptloginname, font=('arial 17 bold'), fg='black', bg='lightgreen')
        self.ptname.place(x=0,y=100)
        self.ptloginname = ptloginname

        # Dr's name
        self.drnameright = Label(self.right2, text="Dr's Name:  " , font=('arial 17 bold'), fg='black',bg='lightgreen')
        self.drnameright.place(x=0, y=150)
        # Appointment Date
        self.apptimeright = Label(self.right2, text="Appointment Date:  ", font=('arial 17 bold'), fg='black', bg='lightgreen')
        self.apptimeright.place(x=0, y=200)

        # cancelling the appointment
        self.appnoenter = Label(self.right2, text="Enter your appointment no.  ", font=('arial 17 bold'), fg='black', bg='lightgreen')
        self.appnoenter.place(x=300, y=50)

        # entry for right labels
        self.drnameright_ent = Entry(self.right2, width=8)
        self.drnameright_ent.place(x=155, y=150)
        self.apptime_ent = Entry(self.right2, width=8)
        self.apptime_ent.place(x=155, y=200)
        self.cancelbooking_ent = Entry(self.right2, width = 2)
        self.cancelbooking_ent.place(x=530, y=50)

        # Button to add an appointment
        self.submit = Button(self.right2, text='Add appointment', width=15, height=2, bg='white', command=self.add_appointment)
        self.submit.place(x=100, y=250)
        # Button to cancel an appointment
        self.cancel = Button(self.right2, text='Cancel appointment', width=15, height=2, bg='white',command=self.cancel_appointment)
        self.cancel.place(x=360, y=100)

        # Title for the bookings made
        self.viewptname = Label(self.right2, text="Appointment No.", font=('arial 17 bold'), fg='black', bg='lightgreen')
        self.viewptname.place(x=0, y=320)
        self.viewappDate = Label(self.right2, text="Appointment Date", font=('arial 17 bold'), fg='black', bg='lightgreen')
        self.viewappDate.place(x=180, y=320)
        self.viewstate = Label(self.right2, text="State", font=('arial 17 bold'), fg='black',bg='lightgreen')
        self.viewstate.place(x=390, y=320)
        self.viewdrname = Label(self.right2, text="Dr's name", font=('arial 17 bold'), fg='black',bg='lightgreen')
        self.viewdrname.place(x=530, y=320)

        # content for the bookings made
        booking = c_bookapp.execute("SELECT appID,appointmentTime,isApproved,DrName,ptID FROM appointments WHERE ptID = (?)",(self.userID,))
        li_appID = []
        can_available = []
        count2 = 0
        for b in booking:
            appID_view = b[0]
            app_time_view = b[1]
            isApproved_view = b[2]
            drname_view = b[3]
            count2+=1
            li_appID.append(b[0])

            self.appID_view = Label(self.right2, text=appID_view, font=('arial 17 bold'), fg='blue', bg='lightgreen')
            self.appID_view.place(x=50, y=300 + 60 * count2)
            self.apptime_view = Label(self.right2, text=app_time_view, font=('arial 17 bold'), fg='blue', bg='lightgreen')
            self.apptime_view.place(x=230, y=300 + 60 * count2)
            self.drname_view = Label(self.right2, text=drname_view, font=('arial 17 bold'), fg='blue', bg='lightgreen')
            self.drname_view.place(x=530, y=300 + 60 * count2)

            if int(b[2]) == 1:
                isApproved_view = "Not approved"
                can_available.append(appID_view)
            elif int(b[2]) == 0:
                isApproved_view = "Already cancelled"
            elif int(b[2]) == 3:
                isApproved_view = "Already approved"

            self.approved_view = Label(self.right2, text=isApproved_view, font=('arial 17 bold'), fg='blue',bg='lightgreen')
            self.approved_view.place(x=350, y=300 + 60 * count2)
        self.li_appID = li_appID
        self.can_available = can_available

        for row in dr_namedate:
            n = row[0]
            d1 = row[1]
            count += 1
            self.drname = Label(self.left2, text=n, font=('arial 20 bold'), fg='black', bg='pink')
            self.drname.place(x=0, y=50 + 60 * count)
            self.d1.append(Label(self.left2, text=d1, font=('arial 20 bold'), fg='black', bg='pink'))

    # Function to call when the submit button is clicked
    def add_appointment(self):

        self.val12 = self.drnameright_ent.get()
        self.val13 = self.apptime_ent.get()
        self.val14 = 1
        self.val15 = datetime.datetime.now()

        dr_date_available = c_bookapp.execute("SELECT staffname,Date1 FROM staffbasic WHERE isDr = 1")
        dict2 = {}
        for row in dr_date_available:
            name = row[0]
            date = row[1]
            dict2[name] = date

        isDuplicate = c_bookapp.execute("SELECT ptID,appointmentTime FROM appointments")
        dict_dup ={}
        for dup in isDuplicate:
            dup_ptID =dup[0]
            dup_time = dup[1]
            dict_dup[dup_ptID] = dup_time

        if dict_dup.get(int(self.userID)) == self.val13:
            tkinter.messagebox.showinfo('Warning', 'Duplicate appointment on the same day.')

        elif self.val12 == '' or self.val13 == '' :
            tkinter.messagebox.showinfo('Warning','Please fill up all the boxes')

        elif dict2.get(self.val12) != self.val13:
            tkinter.messagebox.showinfo('Warning', 'Invalid. Please check the both boxes again.')

        else:
            re_dr_ID = c_bookapp.execute("SELECT staffname,staffID FROM staffbasic WHERE isDr =1")
            for ro in re_dr_ID:
                if self.val12 == ro[0]:
                    self.val16 = ro[1]

            app_newID = 0
            result = c_bookapp.execute("SELECT appID FROM appointments ORDER BY appID")
            for r in result:
                print(r[0])
                app_newID = int(r[0]) + 1

            sql2 = "INSERT INTO 'appointments' (ptID, ptName, appointmentTime, isApproved,DrName,DrID,systemTime,appID) VALUES(?,?,?,?,?,?,?,?)"
            c_bookapp.execute(sql2,(int(self.userID), self.ptloginname, self.val13, self.val14, self.val12, self.val16, self.val15,app_newID))
            conn_bookapp.commit()
            tkinter.messagebox.showinfo('Confirmation', 'Appointment for '+ self.ptloginname+ ' has been submitted.')

            # content for the bookings made
            booking = c_bookapp.execute("SELECT appID,appointmentTime,isApproved,DrName,ptID FROM appointments WHERE ptID = (?)",(self.userID,))
            li_appID = []
            can_available = []
            count2 = 0
            for b in booking:
                appID_view = b[0]
                app_time_view = b[1]
                drname_view = b[3]
                count2 += 1
                li_appID.append(b[0])

                self.appID_view = Label(self.right2, text=appID_view, font=('arial 17 bold'), fg='blue',bg='lightgreen')
                self.appID_view.place(x=50, y=300 + 60 * count2)
                self.apptime_view = Label(self.right2, text=app_time_view, font=('arial 17 bold'), fg='blue',bg='lightgreen')
                self.apptime_view.place(x=230, y=300 + 60 * count2)
                self.drname_view = Label(self.right2, text=drname_view, font=('arial 17 bold'), fg='blue',bg='lightgreen')
                self.drname_view.place(x=530, y=300 + 60 * count2)

                if int(b[2]) == 1:
                    isApproved_view = "Not approved"
                    can_available.append(appID_view)
                elif int(b[2]) == 0:
                    isApproved_view = "Already cancelled"
                elif int(b[2]) == 3:
                    isApproved_view = "Already approved"

                self.approved_view = Label(self.right2, text=isApproved_view, font=('arial 17 bold'),fg='blue', bg='lightgreen')
                self.approved_view.place(x=350, y=300 + 60 * count2)

            self.li_appID = li_appID
            self.can_available = can_available

# Function to call when the cancel button is clicked
    def cancel_appointment(self):
        self.val17 = self.cancelbooking_ent.get()

        if int(self.val17) not in self.li_appID:
            tkinter.messagebox.showinfo('Warning', 'Invalid appointment no')
        elif int(self.val17) not in self.can_available:
            tkinter.messagebox.showinfo('Warning', 'You can not cancel this appointment.')
        else:
            c_bookapp.execute("UPDATE appointments SET isApproved = 0 WHERE appID = (?)",(self.val17))
            conn_bookapp.commit()
            tkinter.messagebox.showinfo('Confirmation', 'Cancellation for appoint no. ' +str(self.val17)+' is successful.')

            booking = c_bookapp.execute("SELECT appID,appointmentTime,isApproved,DrName,ptID FROM appointments WHERE ptID = (?)",(self.userID,))
            li_appID = []
            can_available = []
            count2 = 0
            for b in booking:
                appID_view = b[0]
                app_time_view = b[1]
                isApproved_view = b[2]
                drname_view = b[3]
                count2 += 1
                li_appID.append(b[0])

                self.appID_view = Label(self.right2, text=appID_view, font=('arial 17 bold'), fg='blue',bg='lightgreen')
                self.appID_view.place(x=50, y=300 + 60 * count2)
                self.apptime_view = Label(self.right2, text=app_time_view, font=('arial 17 bold'), fg='blue',bg='lightgreen')
                self.apptime_view.place(x=230, y=300 + 60 * count2)
                self.drname_view = Label(self.right2, text=drname_view, font=('arial 17 bold'), fg='blue',bg='lightgreen')
                self.drname_view.place(x=530, y=300 + 60 * count2)

                if int(b[2]) == 1:
                    isApproved_view = "Not approved"
                    can_available.append(appID_view)
                elif int(b[2]) == 0:
                    isApproved_view = "Already cancelled"
                elif int(b[2]) == 3:
                    isApproved_view = "Already approved"

                self.approved_view = Label(self.right2, text=isApproved_view, font=('arial 17 bold'), fg='blue',bg='lightgreen')
                self.approved_view.place(x=350, y=300 + 60 * count2)