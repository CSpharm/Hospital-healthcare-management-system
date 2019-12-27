import sqlite3
from tkinter import *
import tkinter.messagebox
import tkinter.font as tkFont

# connect to the database on register page
conn_app = sqlite3.connect('Database.db')
c_app = conn_app.cursor()
li_dr_appID = []

class WindowForappapp:
    def __init__(self,appapp,staffID):
        self.appapp = appapp
        self.staffID = staffID

        # 主畫面的左邊 Frame
        self.leftap = Frame(appapp, width=580, height=720, bg='pink')
        self.leftap.pack(side=LEFT)

        # topLeft 是 左邊 Frame 的上半部
        self.topLeftap = Frame(self.leftap, width=580, height=360, bg='pink')
        self.topLeftap.pack(side=TOP)
        # downLeft 是 左邊 Frame 的下半部
        self.downLeftap = Frame(self.leftap, width=580, height=360, bg='pink')
        self.downLeftap.pack(side=BOTTOM)

        # create font
        self.f1 = tkFont.Font(family='times', size='16', weight='bold')
        self.f2 = tkFont.Font(family='times', size='30', weight='bold')
        self.f3 = tkFont.Font(family='times', size='24', weight='bold')
        # Left heading
        self.lhap = Label(self.leftap, text="Approve or cancel appointments", font=self.f2, fg='black', bg='pink')
        self.lhap.place(x=0, y=0)

        # Left labels
        self.id = Label(self.leftap, text="staffID:  " + str(self.staffID), font=self.f1, fg='black', bg='pink')
        self.id.place(x=0, y=50)
        self.labde = Label(self.leftap, text="Please enter one appointment number in each box one time" , font=self.f1, fg='black', bg='pink')
        self.labde.place(x=0, y=100)
        self.labap = Label(self.leftap, text="You'd like to approve: " , font=self.f1, fg='black', bg='pink')
        self.labap.place(x=0, y=130)
        self.labdap = Label(self.leftap, text="You'd like to disapprove: ", font=self.f1, fg='black', bg='pink')
        self.labdap.place(x=0, y=180)
        # Left entry
        self.labap_ent = Entry(self.leftap, width=8)
        self.labap_ent.place(x=170, y=130)
        self.labdap_ent = Entry(self.leftap, width=8)
        self.labdap_ent.place(x=170, y=180)

        # Button to submit the decision an appointment
        self.submit = Button(self.leftap, text='Submit', width=15, height=2, bg='white',
                             command=self.submit)
        self.submit.place(x=350, y=250)

        # Fixed Left Labels
        # Title for the bookings made
        self.viewappno = Label(self.topLeftap, text="App. No.", font=self.f1, fg='black', bg='pink')
        self.viewappno.place(x=0, y=310)
        self.viewptid = Label(self.topLeftap, text="Patient's ID", font=self.f1, fg='black', bg='pink')
        self.viewptid.place(x=100, y=310)
        self.viewptname = Label(self.topLeftap, text="Patient's name", font=self.f1, fg='black', bg='pink')
        self.viewptname.place(x=200, y=310)
        self.viewdate = Label(self.topLeftap, text="Date", font=self.f1, fg='black', bg='pink')
        self.viewdate.place(x=300, y=310)
        self.viewstate = Label(self.topLeftap, text="State", font=self.f1, fg='black', bg='pink')
        self.viewstate.place(x=400, y=310)
