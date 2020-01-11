import sqlite3
from tkinter import *
import tkinter.messagebox
import tkinter.font as tkFont

class WindowForaddGPadmin:

    def __init__(self,ad):
        self.ad = ad

        # create a frame
        self.leftad = Frame(ad, width=630, height = 720, bg='pink')
        self.leftad.pack(side=LEFT)

        # create font
        self.f1 = tkFont.Font(family='times', size='16')

        # headings
        self.lhad = Label(self.leftad, text="Add new GP and admin", font=self.f1, fg='black', bg='pink')
        self.lhad.place(x=0, y=0)

        # LEFT labels
        # staff id
        self.staffidleftad = Label(self.leftad, text="Staff's ID (4 digit)", font=self.f1, fg='black', bg='pink')
        self.staffidleftad.place(x=0, y=70)
        # staff's name
        self.nameleftad = Label(self.leftad, text="Staff's Name", font=self.f1, fg='black', bg='pink')
        self.nameleftad.place(x=0, y=120)
        # password
        self.pwleftad = Label(self.leftad, text="password(only numbers)", font=self.f1, fg='black', bg='pink')
        self.pwleftad.place(x=0, y=180)
        # age
        self.agead = Label(self.leftad, text='Age', font=self.f1, fg='black', bg='pink')
        self.agead.place(x=0, y=240)
        # gender
        self.genderad = Label(self.leftad, text='Gender', font=self.f1, fg='black', bg='pink')
        self.genderad.place(x=0, y=300)
        # phone
        self.phonead = Label(self.leftad, text='Phone', font=self.f1, fg='black', bg='pink')
        self.phonead.place(x=0, y=360)
        # is a Doctor?
        self.isdrad = Label(self.leftad, text='Is he or she a doctor? ', font=self.f1, fg='black', bg='pink')
        self.isdrad.place(x=0, y=410)
        self.isdrdetad = Label(self.leftad, text=' (Y:1, N:0) ', font=self.f1, fg='black',bg='pink')
        self.isdrdetad.place(x=20, y=435)


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

        # Button to add new GP
        self.bu_addGP = Button(self.leftad, text='Submit', width=15, height=2, bg='white',command=self.add_GPadmin)
        self.bu_addGP.place(x=250, y=520)

    def add_GPadmin(self):

        # getting the user inputs
        self.val44 = self.staffidleft_entad.get()
        self.val45 = self.nameleft_entad.get()
        self.val46 = self.pwleft_entad.get()
        self.val47 = self.age_entad.get()
        self.val48 = self.gender_entad.get()
        self.val49 = self.phone_entad.get()
        self.val50 = self.isdr_entad.get()

        # check the staffID is valid or not
        self.check_staID_valid()

        if self.val44 == '' or self.val45 == '' or self.val46 == '' or self.val47 == '' or self.val48 == '' \
                or self.val49 == '' or self.val50 == '':
            tkinter.messagebox.showinfo('Warning', 'Please fill up all the boxes')

        elif (not self.val44.isdigit()) or (not self.val46.isdigit()) or (not self.val47.isdigit()):
            tkinter.messagebox.showinfo('Warning', 'The staff ID ,password,and age should contain only integers.')

        elif len(self.val44) != 4:
            tkinter.messagebox.showinfo('Warning', 'Invalid staff ID. Please enter 4-digit staff ID')

        elif int(self.val44) in self.li_ex_staffID:
            tkinter.messagebox.showinfo('Warning', 'Invalid staff ID. The ID is already in the database')

        elif (int(self.val50) != 0) and (int(self.val50) != 1):
            tkinter.messagebox.showinfo('Warning','isDr should be 0 or 1.')

        else:
            # add a new GP
            conn_addGP = sqlite3.connect('Database.db')
            c_addGP = conn_addGP.cursor()

            sql6 = "INSERT INTO staffbasic (staffID,staffName,password,age,gender,phone,isDr,isactivated)" \
                   "VALUES(?,?,?,?,?,?,?,?)"
            c_addGP.execute(sql6, (self.val44, self.val45, self.val46, self.val47, self.val48, self.val49, self.val50,1))

            conn_addGP.commit()
            conn_addGP.close()
            tkinter.messagebox.showinfo('Confirmation', 'registration for ' + self.val45 + ' is successful.')

    def check_staID_valid(self):

        conn_stafID = sqlite3.connect('Database.db')
        c_stafID = conn_stafID.cursor()

        # check all the staffIDs in the database
        re_staffID = c_stafID.execute("SELECT staffID FROM staffbasic")

        # create a list to store the staffIDs
        self.li_ex_staffID = []

        for row in re_staffID:
            i = row[0]
            self.li_ex_staffID.append(i)

        conn_stafID.commit()
        conn_stafID.close()