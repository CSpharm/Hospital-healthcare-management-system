from tkinter import *
import tkinter.messagebox
import sqlite3

# connect to the database on register page
conn_addGP = sqlite3.connect('Database.db')
c_addGP = conn_addGP.cursor()
li_ex_staffID = []

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

        # Button to add new GP
        self.bu_addGP = Button(self.leftad, text='Submit', width=15, height=2, bg='white',command=self.add_GP)
        self.bu_addGP.place(x=250, y=560)

    def add_GP(self):

        re_staffID = c_addGP.execute("SELECT staffID FROM staffbasic")

        for row in re_staffID:
            i = row[0]

            if i not in li_ex_staffID:
                li_ex_staffID.append(i)

        # getting the user inputs
        self.val44 = self.staffidleft_entad.get()
        self.val45 = self.nameleft_entad.get()
        self.val46 = self.pwleft_entad.get()
        self.val47 = self.age_entad.get()
        self.val48 = self.gender_entad.get()
        self.val49 = self.phone_entad.get()
        self.val50 = self.isdr_entad.get()
        self.val51 = self.date_entad.get()

        if self.val44 == '' or self.val45 == '' or self.val46 == '' or self.val47 == '' or self.val48 == '' or self.val49 == '' or self.val50 == '' or self.val51 == '':
            tkinter.messagebox.showinfo('Warning', 'Please fill up all the boxes')

        elif len(self.val44) != 4:
            tkinter.messagebox.showinfo('Warning', 'Invalid staff ID. Please enter 4-digit staff ID')

        elif int(self.val44) in li_ex_staffID:
            tkinter.messagebox.showinfo('Warning', 'Invalid staff ID. The ID is already in the database')

        else:
            sql6 = "INSERT INTO staffbasic (staffID,staffName,password,age,gender,phone,isDr,Date1)VALUES(?,?,?,?,?,?,?,?)"
            c_addGP.execute(sql6, (self.val44, self.val45, self.val46, self.val47, self.val48, self.val49, self.val50, self.val51))
            conn_addGP.commit()
            tkinter.messagebox.showinfo('Confirmation', 'registration for ' + self.val45 + ' is successful.')
