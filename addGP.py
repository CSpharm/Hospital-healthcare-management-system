from tkinter import *
import tkinter.messagebox
import sqlite3

# connect to the database on register page
conn_addGP = sqlite3.connect('Database.db')
c_addGP = conn_addGP.cursor()

class WindowForaddGP:
    def __init__(self,ad):
        self.ad = ad

        # create a frame
        self.leftad = Frame(ad, width=630, height = 720, bg='pink')
        self.leftad.pack(side=LEFT)
        self.rightad = Frame(ad, width= 570, height = 720, bg = 'plum3')
        self.rightad.pack(side=RIGHT)

        # headings
        self.lhad = Label(self.leftad, text="Add new GP", font=('arial 40 bold'), fg='black', bg='pink')
        self.lhad.place(x=0, y=0)

        # LEFT labels
        # staff id
        self.staffidleftad = Label(self.leftad, text="Staff's ID (4 digit)", font=('arial 20 bold'), fg='black', bg='pink')
        self.staffidleftad.place(x=0, y=70)
        # staff's name
        self.nameleftad = Label(self.leftad, text="Staff's Name", font=('arial 20 bold'), fg='black', bg='pink')
        self.nameleftad.place(x=0, y=120)
        # password
        self.pwleftad = Label(self.leftad, text="password(only numbers)", font=('arial 20 bold'), fg='black', bg='pink')
        self.pwleftad.place(x=0, y=180)
        # age
        self.agead = Label(self.leftad, text='Age', font=('arial 20 bold'), fg='black', bg='pink')
        self.agead.place(x=0, y=240)
        # gender
        self.genderad = Label(self.leftad, text='Gender', font=('arial 20 bold'), fg='black', bg='pink')
        self.genderad.place(x=0, y=300)
        # phone
        self.phonead = Label(self.leftad, text='Phone', font=('arial 20 bold'), fg='black', bg='pink')
        self.phonead.place(x=0, y=360)
        # is a Doctor?
        self.isdrad = Label(self.leftad, text='Is he or she a doctor? ', font=('arial 20 bold'), fg='black', bg='pink')
        self.isdrad.place(x=0, y=410)
        self.isdrdetad = Label(self.leftad, text=' (Y:1, N:0) ', font=('arial 17 bold'), fg='black',bg='pink')
        self.isdrdetad.place(x=20, y=435)
        self.drdatead = Label(self.leftad, text='His/Her available date for appointments:DD/MM', font=('arial 20 bold'), fg='black', bg='pink')
        self.drdatead.place(x=0, y=470)
        self.drdatedetad = Label(self.leftad, text='(If he or she is not a doctor please fill 0)', font=('arial 16 bold'),fg='black', bg='pink')
        self.drdatedetad.place(x=0, y=495)

        # entry for left labels
        self.staffidleft_entad = Entry(self.leftad, width=15)
        self.staffidleft_entad.place(x=250, y=70)
        self.nameleft_entad = Entry(self.leftad, width=15)
        self.nameleft_entad.place(x=250, y=120)
        self.pwleft_entad = Entry(self.leftad, width=15)
        self.pwleft_entad.place(x=250, y=180)
        self.age_entad = Entry(self.leftad, width=15)
        self.age_entad.place(x=250, y=240)
        self.gender_entad = Entry(self.leftad, width=15)
        self.gender_entad.place(x=250, y=300)
        self.phone_entad = Entry(self.leftad, width=15)
        self.phone_entad.place(x=250, y=360)
        self.isdr_entad = Entry(self.leftad, width=15)
        self.isdr_entad.place(x=250, y=420)
        self.date_entad = Entry(self.leftad, width=15)
        self.date_entad.place(x=250, y=520)

        

