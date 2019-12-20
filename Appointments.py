from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime

# connect to the database for appointments
conn1 = sqlite3.connect('Database.db')

# create a cursor
c1 = conn1.cursor()

class WindowForAppointments:
    def __init__(self,a,val10):
        self.userID = val10
        self.a = a
        self.d1 = []
        self.d2 = []

        # create a frame
        self.left2 = Frame(a, width=600, height = 720, bg='pink')
        self.left2.pack(side=LEFT)

        self.right2 = Frame(a, width= 600, height = 720, bg = 'lightgreen')
        self.right2.pack(side=RIGHT)

        # heading
        self.lh2 = Label(self.left2, text="Appointments",font = ('arial 40 bold'),fg='black',bg='pink')
        self.lh2.place(x=0,y=0)

        # Fixed Labels
        self.drnameleft = Label(self.left2, text="Doctors", font=('arial 20 bold'), fg='black', bg='pink')
        self.drnameleft.place(x=0, y=80)

        self.date1 = Label(self.left2, text="Date1", font=('arial 20 bold'), fg='black', bg='pink')
        self.date1.place(x=250, y=80)

        dr_namedate = c1.execute("SELECT DrName,Date1 FROM Drbasic")
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

        # NHS number
        self.id = Label(self.right2, text="NHS number:   "+ str(self.userID), font=('arial 17 bold'), fg='black', bg='lightgreen')
        self.id.place(x=0, y=50)

        re_ptloginname = c1.execute("SELECT ptID,ptName FROM ptbasic")

        for row in re_ptloginname:
            if row[0] == int(self.userID):
                ptloginname = row[1]

        self.ptloginname =ptloginname

        # patients' name
        self.ptname = Label(self.right2, text="Patient's Name:  "+ ptloginname, font=('arial 17 bold'), fg='black', bg='lightgreen')
        self.ptname.place(x=0,y=100)

        self.ptloginname = ptloginname

        # Dr's name
        self.drnameright = Label(self.right2, text="Dr's Name:  " , font=('arial 17 bold'), fg='black',bg='lightgreen')
        self.drnameright.place(x=0, y=150)

        self.apptimeright = Label(self.right2, text="Appointment Date:  ", font=('arial 17 bold'), fg='black', bg='lightgreen')
        self.apptimeright.place(x=0, y=200)

        # entry for right labels
        self.drnameright_ent = Entry(self.right2, width=10)
        self.drnameright_ent.place(x=200, y=150)

        self.apptime_ent = Entry(self.right2, width=10)
        self.apptime_ent.place(x=200, y=200)

        # Button to add an appointment
        self.submit = Button(self.right2, text = 'Add appointment', width=20, height=2,bg='white',command = self.add_appointment)
        self.submit.place(x=200, y=300)


    # Function to call when the button is clicked
    def add_appointment(self):

        self.val12 = self.drnameright_ent.get()
        self.val13 = self.apptime_ent.get()
        self.val14 = 1
        self.val15 = datetime.datetime.now()

        dr_date_available = c1.execute("SELECT Drname,Date1 FROM Drbasic")
        dict2 = {}

        for row in dr_date_available:
            name = row[0]
            date = row[1]
            dict2[name] = date

        if dict2.get(self.val12) != self.val13:
            tkinter.messagebox.showinfo('Warning', 'Please fill up the date again.')

        elif self.val12 == '' or self.val13 == '' :
            tkinter.messagebox.showinfo('Warning','Please fill up all the boxes')

        else:
            re_dr_ID = c1.execute("SELECT Drname,DrID FROM Drbasic")
            for ro in re_dr_ID:
                if self.val12 == ro[0]:
                    self.val16 = ro[1]

            co = 0
            result = c1.execute("SELECT * FROM appointments")
            for r in result:
                co +=1

            app_ID_num = co+1

            sql2 = "INSERT INTO 'appointments' (ptID, ptName, appointmentTime, isApproved,DrName,DrID,systemTime,appID) VALUES(?,?,?,?,?,?,?,?)"
            c1.execute(sql2,(int(self.userID), self.ptloginname, self.val13, self.val14, self.val12, self.val16, self.val15,app_ID_num))
            conn1.commit()
            tkinter.messagebox.showinfo('Confirmation', 'Appointment for '+ self.ptloginname+ ' has been submitted.')