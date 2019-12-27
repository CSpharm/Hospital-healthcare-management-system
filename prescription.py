from tkinter import *
import sqlite3
import tkinter.messagebox
import tkinter.font as tkFont

# connect to the database for appointments
conn_pre = sqlite3.connect('Database.db')

# create a cursor
c_pre = conn_pre.cursor()

class WindowForpres:
    def __init__(self,p,val52):

        self.ptID = val52
        self.p = p

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
        self.ldhp = Label(self.leftp, text="Prescription history", font=self.f2, fg='black', bg='red')
        self.ldhp.place(x=0, y=360)
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
        self.lphone.place(x=0, y=250)
        self.ladd = Label(self.leftp, text="Address:" + str(address), font=self.f1, fg='black', bg='pink')
        self.ladd.place(x=0, y=300)
        self.lall = Label(self.leftp, text="Allergy:" + str(allergy), font=self.f1, fg='black', bg='pink')
        self.lall.place(x=350, y=50)


        # Fixed Left Labels

        #set scrollbar
        scrollbar = Scrollbar(self.topLeftp)
        scrollbar.pack(side=RIGHT, fill=Y)
        # 醫師名字的清單，此Listbox的長和寬會和 downLeft Frame 一樣大小
        drnameList = Listbox(self.topLeftp, yscrollcommand=scrollbar.set, width=550, height=360,font=self.f3)
        # Print the Dr. and their dates
        dr_namedate = c_pre.execute("SELECT staffName,Date1 FROM staffbasic WHERE isDr = 1 ")
        for row in dr_namedate:
            n = row[0]
            d1 = row[1]
            drnameList.insert(END, str(n) + '                ' + str(d1))

        drnameList.pack(side=LEFT, fill = 'x')
        scrollbar.config(command=drnameList.yview)

        # right labels
        self.idright = Label(self.rightp, text="NHS number: " + str(self.ptID), font=self.f1, fg='black', bg='lightgreen')
        self.idright.place(x=0, y=50)
        self.ptname = Label(self.rightp, text="Patient's Name: " , font=self.f1, fg='black', bg='lightgreen')
        self.ptname.place(x=0, y=100)
        # cancelling the appointment
        self.appnoenter = Label(self.rightp, text="Enter your appointment no.  ", font=self.f1, fg='black', bg='lightgreen')
        self.appnoenter.place(x=0, y=150)
        # entry for right labels
        self.cancelbooking_ent = Entry(self.rightp, width = 2)
        self.cancelbooking_ent.place(x=210, y=150)

        # Button to see appointment detail

        self.seedt = Label(self.rightp, text="The columns are the appointment number, the date, the state, and the Dr.name in order." ,font=self.f1, fg='black',
                            bg='lightgreen')
        self.seedt.place(x=0, y=400)