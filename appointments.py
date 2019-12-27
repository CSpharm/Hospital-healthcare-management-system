from tkinter import *
import sqlite3
import tkinter.messagebox
import tkinter.font as tkFont
from see_appointments import *
import datetime

# connect to the database for appointments
conn_bookapp = sqlite3.connect('Database.db')

# create a cursor
c_bookapp = conn_bookapp.cursor()

class WindowForAppointments:
    def __init__(self,a,val10):

        self.userID = val10
        self.a = a

        # 主畫面的右邊Frame
        self.right2 = Frame(a, width= 650, height = 720, bg = 'lightgreen')
        self.right2.pack(side=RIGHT)
        # 主畫面的左邊 Frame
        self.left2 = Frame(a, width=550, height=720, bg='pink')
        self.left2.pack(side=LEFT)

        # topLeft 是 左邊 Frame 的上半部
        self.topLeft = Frame(self.left2, width= 550, height = 350, bg = 'pink')
        self.topLeft.pack(side=TOP)
        # downLeft 是 左邊 Frame 的下半部
        self.downLeft = Frame(self.left2, width= 550, height = 350, bg ='red')
        self.downLeft.pack(side=BOTTOM)

        # create font
        self.f1 = tkFont.Font(family='times', size='16', weight='bold')
        self.f2 = tkFont.Font(family='times', size='30', weight='bold')
        self.f3 = tkFont.Font(family='times', size='24', weight='bold')
        # Left heading
        self.lh2 = Label(self.left2, text="Add Appointments",font =self.f2,fg='black',bg='pink')
        self.lh2.place(x=0,y=0)
        # Right heading
        self.rh2 = Label(self.right2, text="Cancel Appointments", font=self.f2, fg='black', bg='light green')
        self.rh2.place(x=0, y=0)

        # Left labels
        self.id = Label(self.left2, text="NHS number: " + str(self.userID), font=self.f1, fg='black',bg='pink')
        self.id.place(x=0, y=50)

        re_ptloginname = c_bookapp.execute("SELECT ptName FROM ptbasic WHERE ptID = (?)", (self.userID,))
        for row in re_ptloginname:
            ptloginname = row[0]

        self.ptname = Label(self.left2, text="Patient's Name: " + ptloginname, font=self.f1, fg='black',bg='pink')
        self.ptname.place(x=0, y=100)
        self.ptloginname = ptloginname

        # Fixed Left Labels
        # Dr's name
        self.drnameup = Label(self.left2, text="Dr's Name:  ", font=self.f1, fg='black', bg='pink')
        self.drnameup.place(x=0, y=150)
        # Appointment Date
        self.dateup = Label(self.left2, text="Appointment Date:  ", font=self.f1, fg='black', bg='pink')
        self.dateup.place(x=0, y=200)
        self.drnameleftd = Label(self.left2, text="Doctors", font=self.f1, fg='black', bg='pink')
        self.drnameleftd.place(x=0, y=310)
        self.dated = Label(self.left2, text="Date", font=self.f1, fg='black', bg='pink')
        self.dated.place(x=100, y=310)

        # Entry for left labels
        self.drname_ent = Entry(self.left2, width=8)
        self.drname_ent.place(x=155, y=150)
        self.apptime_ent = Entry(self.left2, width=8)
        self.apptime_ent.place(x=155, y=200)
        # Button to add an appointment
        self.submit = Button(self.left2, text='Add appointment', width=15, height=2, bg='white',command=self.add_appointment)
        self.submit.place(x=350, y=250)

        # set scrollbar
        scrollbar = Scrollbar(self.downLeft)
        scrollbar.pack(side=RIGHT, fill=Y)
        # 醫師名字的清單，此Listbox的長和寬會和 downLeft Frame 一樣大小
        drnameList = Listbox(self.downLeft, yscrollcommand=scrollbar.set, width=550, height=350,font=self.f3)
        # Print the Dr. and their dates
        dr_namedate = c_bookapp.execute("SELECT staffName,Date1 FROM staffbasic WHERE isDr = 1 ")
        for row in dr_namedate:
            n = row[0]
            d1 = row[1]
            drnameList.insert(END, str(n) + '                ' + str(d1))

        drnameList.pack(side=LEFT, fill = BOTH)
        scrollbar.config(command=drnameList.yview)

        # right labels
        self.idright = Label(self.right2, text="NHS number: " + str(self.userID), font=self.f1, fg='black', bg='lightgreen')
        self.idright.place(x=0, y=50)
        self.ptname = Label(self.right2, text="Patient's Name: " + ptloginname, font=self.f1, fg='black', bg='lightgreen')
        self.ptname.place(x=0, y=100)
        # cancelling the appointment
        self.appnoenter = Label(self.right2, text="Enter your appointment no.  ", font=self.f1, fg='black', bg='lightgreen')
        self.appnoenter.place(x=0, y=150)
        # entry for right labels
        self.cancelbooking_ent = Entry(self.right2, width = 2)
        self.cancelbooking_ent.place(x=210, y=150)
        # Button to cancel an appointment
        self.cancel = Button(self.right2, text='Cancel appointment', width=15, height=2, bg='white',command=self.cancel_appointment)
        self.cancel.place(x=300, y=250)
        # Button to see appointment detail
        self.see = Button(self.right2, text='See appointments', width=15, height=2, bg='white',
                             command=self.see_appointment)
        self.see.place(x=300, y=350)
        self.seedt = Label(self.right2, text="The columns are the appointment number, the date, the state, and the Dr.name in order." ,font=self.f1, fg='black',
                            bg='lightgreen')
        self.seedt.place(x=0, y=400)

    # Function to see the patient's booking detail
    def see_appointment(self):

        rootsee = Tk()
        r5 = WindowtoseeAppointments(rootsee,self.userID)

        # resolution of the window
        rootsee.geometry('400x200+0+0')
        # end the loop
        rootsee.mainloop()

    # Function to call when the submit button is clicked
    def add_appointment(self):

        self.val12 = self.drname_ent.get()
        self.val13 = self.apptime_ent.get()
        self.val14 = 1
        self.val15 = datetime.datetime.now()

        dr_date_available = c_bookapp.execute("SELECT staffname,Date1 FROM staffbasic WHERE isDr = 1")
        dict2 = {}
        for row in dr_date_available:
            name = row[0]
            date = row[1]
            dict2[name] = date

        isDuplicate = c_bookapp.execute("SELECT ptID,appointmentTime,isApproved FROM appointments ")
        dict_dup ={}
        for dup in isDuplicate:
            if int(dup[2]) != 0:
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
                app_newID = int(r[0]) + 1

            sql2 = "INSERT INTO 'appointments' (ptID, ptName, appointmentTime, isApproved,DrName,DrID,systemTime,appID) VALUES(?,?,?,?,?,?,?,?)"
            c_bookapp.execute(sql2,(int(self.userID), self.ptloginname, self.val13, self.val14, self.val12, self.val16, self.val15,app_newID))
            conn_bookapp.commit()
            tkinter.messagebox.showinfo('Confirmation', 'Appointment for '+ self.ptloginname+ ' has been submitted.')
            self.see_appointment()

    # Function to call when the cancel button is clicked
    def cancel_appointment(self):
        self.val17 = self.cancelbooking_ent.get()

        cancel_available = []
        cancel_list = c_bookapp.execute("SELECT appID FROM appointments WHERE isApproved = 1 AND ptID = (?)",(self.userID,))
        for c in cancel_list:
            cancel_available.append(c[0])

        if self.val17 == '' :
            tkinter.messagebox.showinfo('Warning', 'Please fill the box for cancelling.')
        elif int(self.val17) not in cancel_available:
            tkinter.messagebox.showinfo('Warning', 'You can not cancel this appointment.')
        else:
            c_bookapp.execute("UPDATE appointments SET isApproved = 0 WHERE appID = (?)",(self.val17,))
            conn_bookapp.commit()
            tkinter.messagebox.showinfo('Confirmation', 'Cancellation for appoint no. ' +str(self.val17)+' is successful.')
            self.see_appointment()