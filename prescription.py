from tkinter import *
import sqlite3
import tkinter.messagebox
import tkinter.font as tkFont

# connect to the database for appointments
conn_pre = sqlite3.connect('Database.db')

# create a cursor
c_pre = conn_pre.cursor()

class WindowForpres:
    def __init__(self,p,val52,staffID):

        self.ptID = val52
        self.p = p
        self.staffID = staffID

        # 主畫面的右邊Frame
        self.rightp = Frame(p, width= 650, height = 720, bg = 'lightgreen')
        self.rightp.pack(side=RIGHT)
        # 主畫面的左邊 Frame
        self.leftp = Frame(p, width=550, height=720, bg='pink')
        self.leftp.pack(side=LEFT)

        # topLeft 是 左邊 Frame 的上半部
        self.topLeftp = Frame(self.leftp, width= 550, height = 360, bg = 'pink')
        self.topLeftp.pack(side=TOP)
        # downLeft 是 左邊 Frame 的下半部
        self.downLeftp = Frame(self.leftp, width= 550, height = 360, bg ='red')
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
        self.ldfp = Label(self.leftp, text="No.  Date    Medicine                Day           Frequency   Admin.  Route  Dr.name",
                          font=self.f2, fg='blue', bg='pink')
        self.ldfp.place(x=0, y=335)
        # Right heading
        self.rhp = Label(self.rightp, text="Prescription", font=self.f2, fg='black', bg='light green')
        self.rhp.place(x=0, y=0)

        # Left labels
        self.id = Label(self.leftp, text="NHS number: " + str(self.ptID), font=self.f1, fg='black',bg='pink')
        self.id.place(x=0, y=50)

        re_pt = c_pre.execute("SELECT * FROM ptbasic WHERE ptID = (?)", (self.ptID,))
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
        self.lall = Label(self.leftp, text="Allergy:" + str(allergy), font=self.f1, fg='black', bg='pink')
        self.lall.place(x=300, y=150)

        #set scrollbar
        scrollbar = Scrollbar(self.downLeftp)
        scrollbar.pack(side=RIGHT, fill=Y)
        # 醫師名字的清單，此Listbox的長和寬會和 downLeft Frame 一樣大小
        pre_List = Listbox(self.downLeftp, yscrollcommand=scrollbar.set, width=550, height=360,font=self.f3)

        re_pre = c_pre.execute("SELECT * FROM prescription WHERE ptID = (?)",(self.ptID,))
        for r in re_pre:
            orderno = r[5]
            appdate = r[4]
            med1 = r[6]
            day1 = r[7]
            dos1 = r[8]
            fre1 = r[9]
            adm1 = r[10]
            rou1 = r[11]
            med2 = r[12]
            day2 = r[13]
            dos2 = r[14]
            fre2 = r[15]
            adm2 = r[16]
            rou2 = r[17]
            med3 = r[18]
            day3 = r[19]
            dos3 = r[20]
            fre3 = r[21]
            adm3 = r[22]
            rou3 = r[23]
            Drname = r[3]
            pre_List.insert(END, str(orderno)+ '    ' + str(appdate)+ '    '+str(med1) +' '+ str(dos1) + '         ' +
                            str(day1) +'              '+ str(fre1) +'         '+ str(adm1) +'         '+ str(rou1)+ '     '+ str(Drname))
            pre_List.insert(END,str(orderno) + '    ' + str(appdate) + '    ' + str(med2) + ' ' + str(dos2) + '         ' +
                            str(day2) +'              ' + str(fre2) + '         ' + str(adm2) + '          ' + str(rou2)+ '       '+ str(Drname))
            pre_List.insert(END, str(orderno) + '    ' + str(appdate) + '    ' + str(med3) + ' ' + str(dos3) + '         ' +
                            str(day3) +'              ' + str(fre3) + '         ' + str(adm3) + '          ' + str(rou3) + '     ' + str(Drname))


        pre_List.pack(side=LEFT, fill = 'x')
        scrollbar.config(command=pre_List.yview)

        # right labels
        self.lstaID = Label(self.rightp, text="Your Dr. ID: " +str(self.staffID), font=self.f1, fg='black', bg='lightgreen')
        self.lstaID.place(x=0, y=50)

        re_dr = c_pre.execute("SELECT staffName FROM staffbasic WHERE staffID = (?)", (self.staffID,))
        for r in re_dr:
            drsname = r[0]

        self.ldrname = Label(self.rightp, text="Dr's name: " +str(drsname), font=self.f1, fg='black', bg='lightgreen')
        self.ldrname.place(x=200, y=50)
        self.lapptime = Label(self.rightp, text="Appointment Date: " , font=self.f1, fg='black', bg='lightgreen')
        self.lapptime.place(x=400, y=50)

        # labels for med 1
        self.lmedicine1 = Label(self.rightp, text="Medicine 1 " , font=self.f1, fg='black', bg='lightgreen')
        self.lmedicine1.place(x=0, y=150)
        self.lmed1 = Label(self.rightp, text="Medicine's Name " , font=self.f1, fg='black', bg='lightgreen')
        self.lmed1.place(x=0, y=200)
        self.ldos1 = Label(self.rightp, text="Dosage ", font=self.f1, fg='black', bg='lightgreen')
        self.ldos1.place(x=200, y=200)
        self.lday1 = Label(self.rightp, text="Day ", font=self.f1, fg='black', bg='lightgreen')
        self.lday1.place(x=300, y=200)
        self.lfre1 = Label(self.rightp, text="Frequency ", font=self.f1, fg='black', bg='lightgreen')
        self.lfre1.place(x=360, y=200)
        self.lad1 = Label(self.rightp, text="Administration", font=self.f1, fg='black', bg='lightgreen')
        self.lad1.place(x=470, y=200)
        self.lfre1 = Label(self.rightp, text="Route ", font=self.f1, fg='black', bg='lightgreen')
        self.lfre1.place(x=580, y=200)

        # labels for med 2
        self.lmedicine2 = Label(self.rightp, text="Medicine 2 ", font=self.f1, fg='black', bg='lightgreen')
        self.lmedicine2.place(x=0, y=300)
        self.lmed2 = Label(self.rightp, text="Medicine's Name ", font=self.f1, fg='black', bg='lightgreen')
        self.lmed2.place(x=0, y=350)
        self.ldos2 = Label(self.rightp, text="Dosage ", font=self.f1, fg='black', bg='lightgreen')
        self.ldos2.place(x=200, y=350)
        self.lday2 = Label(self.rightp, text="Day ", font=self.f1, fg='black', bg='lightgreen')
        self.lday2.place(x=300, y=350)
        self.lfre2 = Label(self.rightp, text="Frequency ", font=self.f1, fg='black', bg='lightgreen')
        self.lfre2.place(x=360, y=350)
        self.lad2 = Label(self.rightp, text="Administration", font=self.f1, fg='black', bg='lightgreen')
        self.lad2.place(x=470, y=350)
        self.lfre2 = Label(self.rightp, text="Route ", font=self.f1, fg='black', bg='lightgreen')
        self.lfre2.place(x=580, y=350)

        # labels for med 3
        self.lmedicine3 = Label(self.rightp, text="Medicine 3 ", font=self.f1, fg='black', bg='lightgreen')
        self.lmedicine3.place(x=0, y=450)
        self.lmed3 = Label(self.rightp, text="Medicine's Name ", font=self.f1, fg='black', bg='lightgreen')
        self.lmed3.place(x=0, y=500)
        self.ldos3 = Label(self.rightp, text="Dosage ", font=self.f1, fg='black', bg='lightgreen')
        self.ldos3.place(x=200, y=500)
        self.lday3 = Label(self.rightp, text="Day ", font=self.f1, fg='black', bg='lightgreen')
        self.lday3.place(x=300, y=500)
        self.lfre3 = Label(self.rightp, text="Frequency ", font=self.f1, fg='black', bg='lightgreen')
        self.lfre3.place(x=360, y=500)
        self.lad3 = Label(self.rightp, text="Administration", font=self.f1, fg='black', bg='lightgreen')
        self.lad3.place(x=470, y=500)
        self.lfre3 = Label(self.rightp, text="Route ", font=self.f1, fg='black', bg='lightgreen')
        self.lfre3.place(x=580, y=500)

        # entry for right labels for med 1
        self.med1_ent = Entry(self.rightp, width=15)
        self.med1_ent.place(x=1, y=230)
        self.dos1_ent = Entry(self.rightp, width=8)
        self.dos1_ent.place(x=200, y=230)
        self.day1_ent = Entry(self.rightp, width=3)
        self.day1_ent.place(x=300, y=230)
        self.fre1_ent = Entry(self.rightp, width=5)
        self.fre1_ent.place(x=360, y=230)
        self.ad1_ent = Entry(self.rightp, width=7)
        self.ad1_ent.place(x=470, y=230)
        self.rou1_ent = Entry(self.rightp, width=3)
        self.rou1_ent.place(x=580, y=230)

        # entry for right labels for med 2
        self.med2_ent = Entry(self.rightp, width=15)
        self.med2_ent.place(x=1, y=380)
        self.dos2_ent = Entry(self.rightp, width=8)
        self.dos2_ent.place(x=200, y=380)
        self.day2_ent = Entry(self.rightp, width=3)
        self.day2_ent.place(x=300, y=380)
        self.fre2_ent = Entry(self.rightp, width=5)
        self.fre2_ent.place(x=360, y=380)
        self.ad2_ent = Entry(self.rightp, width=7)
        self.ad2_ent.place(x=470, y=380)
        self.rou2_ent = Entry(self.rightp, width=3)
        self.rou2_ent.place(x=580, y=380)

        # entry for right labels for med 3
        self.med3_ent = Entry(self.rightp, width=15)
        self.med3_ent.place(x=1, y=530)
        self.dos3_ent = Entry(self.rightp, width=8)
        self.dos3_ent.place(x=200, y=530)
        self.day3_ent = Entry(self.rightp, width=3)
        self.day3_ent.place(x=300, y=530)
        self.fre3_ent = Entry(self.rightp, width=5)
        self.fre3_ent.place(x=360, y=530)
        self.ad3_ent = Entry(self.rightp, width=7)
        self.ad3_ent.place(x=470, y=530)
        self.rou3_ent = Entry(self.rightp, width=3)
        self.rou3_ent.place(x=580, y=530)
        # Button to see appointment detail

        self.seedt = Button(self.rightp, text="Submit" ,font=self.f1, fg='black', bg='lightgreen')
        self.seedt.place(x=300, y=580)