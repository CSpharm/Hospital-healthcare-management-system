import sqlite3
from tkinter import *
import tkinter.messagebox
import tkinter.font as tkFont

from dr_see_pxhis import WindowForPxHis
import datetime

today = datetime.date.today()
t = str(today).split('-')


class WindowForpres:
    def __init__(self,p,val52,staffID):

        self.ptID = val52
        self.p = p
        self.staffID = staffID

        self.rightp = Frame(p, width= 650, height = 720, bg = 'lightgreen')
        self.rightp.pack(side=RIGHT)
        self.leftp = Frame(p, width=550, height=720, bg='pink')
        self.leftp.pack(side=LEFT)

        self.topLeftp = Frame(self.leftp, width= 550, height = 360, bg = 'pink')
        self.topLeftp.pack(side=TOP)
        self.downLeftp = Frame(self.leftp, width= 550, height = 360, bg ='pink')
        self.downLeftp.pack(side=BOTTOM)

        # create font
        self.f1 = tkFont.Font(family='times', size='16')

        # Left heading
        self.lhp = Label(self.leftp, text="Patient's basic file",font =self.f1,fg='black',bg='pink')
        self.lhp.place(x=0,y=0)
        self.ldhp = Label(self.leftp, text="Prescription history", font=self.f1, fg='blue', bg='pink')
        self.ldhp.place(x=0, y=300)
        self.ldetail1 = Label(self.leftp, text="Column order:",font=self.f1, fg='blue', bg='pink')
        self.ldetail1.place(x=0, y=335)
        self.ldetail2 = Label(self.leftp, text=" Prescription no., Date, Medicine name, Dosage, Day, "
                              "How to use, Dr's name.",font=self.f1, fg='blue', bg='pink')
        self.ldetail2.place(x=0, y=360)

        # Right heading
        self.rhp = Label(self.rightp, text="Prescription", font=self.f1, fg='black', bg='light green')
        self.rhp.place(x=0, y=0)

        # Left labels
        self.id = Label(self.leftp, text="NHS number: " + str(self.ptID), font=self.f1, fg='black',bg='pink')
        self.id.place(x=0, y=50)

        # pt details
        self.ptdetails()

        # Button to see the px
        self.bseepx = Button(self.leftp, text="See the prescription history", font=self.f1, fg='black', bg='pink', command=self.pxhistory)
        self.bseepx.place(x=0, y=270)

        # if the appointment date is today, show the prescription page;
        # if not, dr can only see the previous prescription history but cannot add any prescription
        # since the prescription must be under the situation that patient has a confirmed appointment
        # this can also prevent drs modifying past and future prescriptions
        # to protect patients and drs at the same time
        self.prescribe_today()

    def ptdetails(self):

        conn_ptb = sqlite3.connect('Database.db')
        c_ptb = conn_ptb.cursor()

        re_pt = c_ptb.execute("SELECT * FROM ptbasic WHERE ptID = (?)", (self.ptID,))
        for row in re_pt:
            ptname = row[1]
            age = row[3]
            gender = row[4]
            phone = row[5]
            address = row[6]
            allergy = row[7]

        self.lptname = Label(self.leftp, text="Patient's Name: " + str(ptname), font=self.f1, fg='black', bg='pink')
        self.lptname.place(x=0, y=100)
        self.lage = Label(self.leftp, text="Age:" + str(age), font=self.f1, fg='black', bg='pink')
        self.lage.place(x=0, y=150)
        self.lgender = Label(self.leftp, text="Gender:" + str(gender), font=self.f1, fg='black', bg='pink')
        self.lgender.place(x=0, y=200)
        self.lphone = Label(self.leftp, text="Phone:" + str(phone), font=self.f1, fg='black', bg='pink')
        self.lphone.place(x=300, y=50)
        self.ladd = Label(self.leftp, text="Address:" + str(address), font=self.f1, fg='black', bg='pink')
        self.ladd.place(x=300, y=100)
        self.ladd.place(x=300, y=100)
        self.lall = Label(self.leftp, text="Allergy:" + str(allergy), font=self.f1, fg='black', bg='pink')
        self.lall.place(x=300, y=150)

        conn_ptb.commit()
        conn_ptb.close()

    def prescribe_today(self):

        conn_date = sqlite3.connect('Database.db')
        c_date = conn_date.cursor()

        # find drsname
        conn_drname = sqlite3.connect('Database.db')
        c_drname = conn_drname.cursor()

        re_dr = c_drname.execute("SELECT staffName FROM staffbasic WHERE staffID = (?)", (self.staffID,))
        for r in re_dr:
            self.drsname = r[0]

        conn_drname.commit()
        conn_drname.close()

        # find the available and confirmed appointment dates
        # isApproved = 3 means prescribed, but one appointment usually needs several medicines
        # so the state includes isApproved=2 and isApproved=3
        re_date = c_date.execute("SELECT appointmentTime,appID FROM 'appointments' WHERE (ptID = (?) AND DrID= (?)) "
                                 "AND (isApproved = 2 or isApproved = 3)", (self.ptID, self.staffID))

        for re in re_date:
            appDate = re[0]
            todayappID = re[1]
            aD1 = appDate.split('-')
            self.li_appDate = []

            # if the date is today, the labels,entries, and buttons will show, then dr can prescribe.
            # if not, the page won't show anything.
            if (aD1[0] < t[0]) or (aD1[0] == t[0] and aD1[1] < t[1]) or (
                    aD1[0] == t[0] and aD1[1] == t[1] and (aD1[2] < t[2])):
                pass

            elif (aD1[0] == t[0] and aD1[1] == t[1]) and (aD1[2] == t[2]):
                self.todayappID = todayappID
                self.li_appDate.append(appDate)

                # right labels
                self.lstaID = Label(self.rightp, text="Your Dr. ID: " + str(self.staffID), font=self.f1, fg='black',
                                    bg='lightgreen')
                self.lstaID.place(x=0, y=50)
                self.ldrname = Label(self.rightp, text="Your name: " + str(self.drsname), font=self.f1, fg='black',
                                     bg='lightgreen')
                self.ldrname.place(x=200, y=50)

                self.ltoday = Label(self.rightp, text="Today: " + str(today), font=self.f1, fg='black', bg='lightgreen')
                self.ltoday.place(x=400, y=50)
                # label for the appointment date
                self.lappdate = Label(self.rightp, text="Appointment Date:   " + str(li_appDate), font=self.f1,
                                      fg='black', bg='lightgreen')
                self.lappdate.place(x=0, y=100)

                # labels for med
                self.lmed1 = Label(self.rightp, text="Medicine's Name ", font=self.f1, fg='black', bg='lightgreen')
                self.lmed1.place(x=0, y=200)
                self.ldos1 = Label(self.rightp, text="Dosage ", font=self.f1, fg='black', bg='lightgreen')
                self.ldos1.place(x=200, y=200)
                self.lday1 = Label(self.rightp, text="Day ", font=self.f1, fg='black', bg='lightgreen')
                self.lday1.place(x=300, y=200)
                self.lad1 = Label(self.rightp, text="Administration", font=self.f1, fg='black', bg='lightgreen')
                self.lad1.place(x=470, y=200)

                # entry for right labels for med 1
                self.med1_ent = Entry(self.rightp, width=15)
                self.med1_ent.place(x=1, y=230)
                self.dos1_ent = Entry(self.rightp, width=8)
                self.dos1_ent.place(x=200, y=230)
                self.day1_ent = Entry(self.rightp, width=3)
                self.day1_ent.place(x=300, y=230)
                self.ad1_ent = Entry(self.rightp, width=7)
                self.ad1_ent.place(x=470, y=230)

                # Button to add px
                self.sub = Button(self.rightp, text="Submit", font=self.f1, fg='black', bg='lightgreen',
                                  command=self.addpx)
                self.sub.place(x=280, y=280)

                # Label to delete a prescription
                self.ldp = Label(self.rightp, text="Delete today's prescription", font=self.f1, fg='black',
                                 bg='lightgreen')
                self.ldp.place(x=0, y=380)
                self.le = Label(self.rightp, text="Enter the prescription no.", font=self.f1, fg='black',
                                bg='lightgreen')
                self.le.place(x=0, y=430)

                # entry to delete a presciption
                self.pno_ent = Entry(self.rightp, width=3)
                self.pno_ent.place(x=200, y=430)
                # Button to submit
                self.subd = Button(self.rightp, text="Submit", font=self.f1, fg='black', bg='lightgreen',
                                   command=self.delpx)
                self.subd.place(x=280, y=480)

            else:
                self.li_appDate.append(appDate)

        conn_date.commit()
        conn_date.close()

    def pxhistory(self):

        root_drPxHis = Tk()
        WindowForPxHis(root_drPxHis,self.ptID)

        # resolution of the window
        root_drPxHis.geometry('530x360+0+0')
        # end the loop
        root_drPxHis.mainloop()


    def addpx(self):

        self.val54 = self.med1_ent.get()
        self.val55 = self.dos1_ent.get()
        self.val56 = self.day1_ent.get()
        self.val57 = self.ad1_ent.get()

        if self.val54 == '' or self.val55 == '' or self.val56 == '' or self.val57 == '':
            tkinter.messagebox.showinfo('Warning', 'Please fill the boxes.')

        elif not self.val56.isdigit():
            tkinter.messagebox.showinfo('Warning', 'The day must be an integer.')

        else:
            conn_addp = sqlite3.connect('Database.db')
            c_addp = conn_addp.cursor()

            # add presription
            sql7 = "INSERT INTO 'prescription' (ptID, DrID, DrName, appointmentTime,medname1,day1,dosage1,adm1,appID)" \
                   " VALUES(?,?,?,?,?,?,?,?,?)"
            c_addp.execute(sql7, (self.ptID,self.staffID, self.drsname, today,self.val54,self.val56,self.val55,
                                  self.val57,self.todayappID))
            conn_addp.commit()

            # update the appointments to be prescribed (isApproved = 3)
            c_addp.execute("UPDATE appointments SET isApproved = 3 WHERE appID = (?)", (self.todayappID,))
            conn_addp.commit()
            conn_addp.close()

            tkinter.messagebox.showinfo('Confirmation', ' Successful!')

    def delpx(self):

        try:
            self.val58 = int(self.pno_ent.get())

        except ValueError:
            tkinter.messagebox.showinfo('Warning', 'The number should be an integer.')

        else:
            conn_date = sqlite3.connect('Database.db')
            c_date = conn_date.cursor()

            re_predate = c_date.execute(" SELECT appointmentTime FROM 'prescription' WHERE orderNo = (?)",(self.val58,))

            for result in re_predate:
                appDate = result[0]
                aD2 = appDate.split('-')

                # check the date is today or not
                if (aD2[0] == t[0] and aD2[1] == t[1]) and aD2[2] == t[2]:
                    c_date.execute("DELETE FROM 'prescription' WHERE orderNo = (?)", (self.val58,))
                    tkinter.messagebox.showinfo('Confirmation', 'Successful!')
                else:
                    tkinter.messagebox.showinfo('Warning', "This appointment date is not today")

            conn_date.commit()
            conn_date.close()
