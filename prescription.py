from tkinter import *
import sqlite3
import tkinter.messagebox
import tkinter.font as tkFont
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
        self.f1 = tkFont.Font(family='times', size='16', weight='bold')
        self.f2 = tkFont.Font(family='times', size='30', weight='bold')
        self.f3 = tkFont.Font(family='times', size='24', weight='bold')

        # Left heading
        self.lhp = Label(self.leftp, text="Patient's basic file",font =self.f2,fg='black',bg='pink')
        self.lhp.place(x=0,y=0)
        self.ldhp = Label(self.leftp, text="Prescription history", font=self.f2, fg='blue', bg='pink')
        self.ldhp.place(x=0, y=300)
        self.ldfp = Label(self.leftp, text="No.     Date              Medicine                       Day     "
                                           + "           Administration             Dr.name",
                          font=self.f2, fg='blue', bg='pink')
        self.ldfp.place(x=0, y=335)
        # Right heading
        self.rhp = Label(self.rightp, text="Prescription", font=self.f2, fg='black', bg='light green')
        self.rhp.place(x=0, y=0)

        # Left labels
        self.id = Label(self.leftp, text="NHS number: " + str(self.ptID), font=self.f1, fg='black',bg='pink')
        self.id.place(x=0, y=50)

        # connect to the database
        conn_ptb = sqlite3.connect('Database.db')
        # create a cursor
        c_ptb = conn_ptb.cursor()

        re_pt = c_ptb.execute("SELECT * FROM ptbasic WHERE ptID = (?)", (self.ptID,))
        for row in re_pt:
            ptname = row[1]
            age = row[3]
            gender = row[4]
            phone = row[5]
            address = row[6]
            allergy = row[7]

        self.lptname = Label(self.leftp, text="Patient's Name: " + str(ptname), font=self.f1, fg='black',bg='pink')
        self.lptname.place(x=0, y=100)
        self.lage = Label(self.leftp, text="Age:" + str(age), font=self.f1, fg='black', bg='pink')
        self.lage.place(x=0, y=150)
        self.lgender = Label(self.leftp, text="Gender:" +str(gender), font=self.f1, fg='black', bg='pink')
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

        # Button to see the px
        self.bseepx = Button(self.leftp, text="See the prescription history", font=self.f1, fg='black', bg='pink', command=self.seepx)
        self.bseepx.place(x=0, y=270)
        # connect to the database
        conn_drname = sqlite3.connect('Database.db')
        # create a cursor
        c_drname = conn_drname.cursor()

        re_dr = c_drname.execute("SELECT staffName FROM staffbasic WHERE staffID = (?)", (self.staffID,))
        for r in re_dr:
            drsname = r[0]

        conn_drname.commit()
        conn_drname.close()
        self.drsname = drsname

        # connect to the database
        conn_date = sqlite3.connect('Database.db')
        # create a cursor
        c_date = conn_date.cursor()

        re_date = c_date.execute("SELECT appointmentTime,appID FROM 'appointments' WHERE (ptID = (?) AND DrID= (?)) "
                                 "AND (isApproved = 2 or isApproved = 3)", (self.ptID,self.staffID))

        for re in re_date:
            appDate = re[0]
            todayappID = re[1]
            aD1 = appDate.split('-')
            li_appDate = []

            if (aD1[0] < t[0]) or (aD1[0] == t[0] and aD1[1] < t[1] ) or (aD1[0] == t[0] and aD1[1] == t[1] and (aD1[2] <t[2])):
                pass
            elif (aD1[0] == t[0] and aD1[1] == t[1]) and (aD1[2] == t[2]):
                self.todayappID = todayappID
                li_appDate.append(appDate)

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
                self.lappdate = Label(self.rightp, text="Appointment Date:   " + str(li_appDate), font=self.f1,fg='black', bg='lightgreen')
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
                self.ldp = Label(self.rightp, text="Delete today's prescription", font=self.f2, fg='black', bg='lightgreen')
                self.ldp.place(x=0, y=380)
                self.le = Label(self.rightp, text="Enter the prescription no.", font=self.f1, fg='black', bg='lightgreen')
                self.le.place(x=0, y=430)
                # entry to delete a presciption
                self.pno_ent = Entry(self.rightp, width=3)
                self.pno_ent.place(x=200, y=430)
                # Button to submit
                self.subd = Button(self.rightp, text="Submit", font=self.f1, fg='black', bg='lightgreen',
                                   command=self.delpx)
                self.subd.place(x=280, y=480)

            else:
                li_appDate.append(appDate)

        conn_date.commit()
        conn_date.close()



    def seepx(self):

        # set scrollbar
        scrollbar = Scrollbar(self.downLeftp)
        scrollbar.pack(side=RIGHT, fill=Y)
        # set a list to fit the frame
        pre_List = Listbox(self.downLeftp, yscrollcommand=scrollbar.set, width=550, height=360,font=self.f3)

        # connect to the database
        conn_phis = sqlite3.connect('Database.db')
        # create a cursor
        c_phis = conn_phis.cursor()

        re_pre = c_phis.execute("SELECT * FROM prescription WHERE ptID = (?)",(self.ptID,))
        for r in re_pre:
            orderno = r[4]
            appdate = r[3]
            med1 = r[5]
            day1 = r[6]
            dos1 = r[7]
            adm1 = r[8]
            Drname = r[2]
            pre_List.insert(END, str(orderno)+ '    ' + str(appdate)+ '         '+str(med1) + '   '+ str(dos1) +'     '
                            +str(day1) +'                 '+ str(adm1) +'               '+ str(Drname))

        conn_phis.commit()
        conn_phis.close()

        pre_List.pack(side=LEFT, fill = 'x')
        scrollbar.config(command=pre_List.yview)
        scrollbar.config(command=pre_List.yview)

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
            # connect to the database
            conn_addp = sqlite3.connect('Database.db')
            # create a cursor
            c_addp = conn_addp.cursor()

            sql7 = "INSERT INTO 'prescription' (ptID, DrID, DrName, appointmentTime,medname1,day1,dosage1,adm1,appID) VALUES(?,?,?,?,?,?,?,?,?)"
            c_addp.execute(sql7, (self.ptID,self.staffID, self.drsname, today,self.val54,self.val56,self.val55,self.val57,self.todayappID))
            conn_addp.commit()
            c_addp.execute("UPDATE appointments SET isApproved = 3 WHERE appID = (?)", (self.todayappID,))
            conn_addp.commit()
            conn_addp.close()

            tkinter.messagebox.showinfo('Confirmation', ' Successful!')

    def delpx(self):

        self.val58 = self.pno_ent.get()

        t = str(today).split('-')

        # connect to the database
        conn_date = sqlite3.connect('Database.db')
        # create a cursor
        c_date = conn_date.cursor()

        re_predate = c_date.execute(" SELECT appointmentTime FROM 'prescription' WHERE orderNo = (?)",(self.val58,))
        for result in re_predate:
            appDate = result[0]
            aD2 = appDate.split('-')

            if not self.val58.isdigit():
                tkinter.messagebox.showinfo('Warning', 'The number should be an integer.')

            elif (aD2[0] == t[0] and aD2[1] == t[1]) and aD2[2] == t[2]:
                c_date.execute("DELETE FROM 'prescription' WHERE orderNo = (?)", (self.val58))
                tkinter.messagebox.showinfo('Confirmation', 'Successful!')
            else:
                tkinter.messagebox.showinfo('Warning', "This appointment date is not today")

        conn_date.commit()
        conn_date.close()

