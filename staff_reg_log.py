from tkinter import *
import tkinter.messagebox
import sqlite3
from staffhome import WindowForstaffHome

# connect to the database on register page
conn_staff_reg = sqlite3.connect('Database.db')
c_staff_reg = conn_staff_reg.cursor()

# empty the list for existing staff ID
li_exi_staffID = []

# create a window for stafflogin
class WindowForstaffLogin:
    def __init__(self,staffreg):
        self.staffreg = staffreg

        # create a frame
        self.left3 = Frame(staffreg, width=630, height = 720, bg='pink')
        self.left3.pack(side=LEFT)
        self.right3 = Frame(staffreg, width= 570, height = 720, bg = 'lavender')
        self.right3.pack(side=RIGHT)

        # headings
        self.lh3 = Label(self.left3, text="Staff register", font=('arial 40 bold'), fg='black', bg='pink')
        self.lh3.place(x=0, y=0)
        self.rh3 = Label(self.right3, text="Staff login", font=('arial 40 bold'), fg='black', bg='lavender')
        self.rh3.place(x=0, y=0)

        # LEFT labels
        # staff id
        self.staffidleft3 = Label(self.left3, text="Staff's ID (4 digit)", font=('arial 20 bold'), fg='black', bg='pink')
        self.staffidleft3.place(x=0, y=70)
        # staff's name
        self.nameleft3 = Label(self.left3, text="Staff's Name", font=('arial 20 bold'), fg='black', bg='pink')
        self.nameleft3.place(x=0, y=120)
        # password
        self.pwleft3 = Label(self.left3, text="password(only numbers)", font=('arial 20 bold'), fg='black', bg='pink')
        self.pwleft3.place(x=0, y=180)
        # age
        self.age3 = Label(self.left3, text='Age', font=('arial 20 bold'), fg='black', bg='pink')
        self.age3.place(x=0, y=240)
        # gender
        self.gender3 = Label(self.left3, text='Gender', font=('arial 20 bold'), fg='black', bg='pink')
        self.gender3.place(x=0, y=300)
        # phone
        self.phone3 = Label(self.left3, text='Phone', font=('arial 20 bold'), fg='black', bg='pink')
        self.phone3.place(x=0, y=360)
        # is a Doctor?
        self.isdr3 = Label(self.left3, text='Are you a doctor? ', font=('arial 20 bold'), fg='black', bg='pink')
        self.isdr3.place(x=0, y=410)
        self.isdrdet3 = Label(self.left3, text=' (Y:1, N:0) ', font=('arial 17 bold'), fg='black',bg='pink')
        self.isdrdet3.place(x=20, y=435)
        self.drdate3 = Label(self.left3, text='Your available date for appointments:DD/MM', font=('arial 20 bold'), fg='black', bg='pink')
        self.drdate3.place(x=0, y=470)
        self.drdatedet3 = Label(self.left3, text='(If you are not a doctor please fill 0)', font=('arial 16 bold'),fg='black', bg='pink')
        self.drdatedet3.place(x=0, y=495)

        # RIGHT labels
        # ID for login
        self.idright3 = Label(self.right3, text="staffID:", font=('arial 20 bold'), fg='black',bg='lavender')
        self.idright3.place(x=0, y=100)
        # password for login
        self.pwright3 = Label(self.right3, text="Password:", font=('arial 20 bold'), fg='black', bg='lavender')
        self.pwright3.place(x=0, y=200)

        # entry for left labels
        self.staffidleft_ent3 = Entry(self.left3, width=15)
        self.staffidleft_ent3.place(x=250, y=70)
        self.nameleft_ent3 = Entry(self.left3, width=15)
        self.nameleft_ent3.place(x=250, y=120)
        self.pwleft_ent3 = Entry(self.left3, width=15)
        self.pwleft_ent3.place(x=250, y=180)
        self.age_ent3 = Entry(self.left3, width=15)
        self.age_ent3.place(x=250, y=240)
        self.gender_ent3 = Entry(self.left3, width=15)
        self.gender_ent3.place(x=250, y=300)
        self.phone_ent3 = Entry(self.left3, width=15)
        self.phone_ent3.place(x=250, y=360)
        self.isdr_ent3 = Entry(self.left3, width=15)
        self.isdr_ent3.place(x=250, y=420)
        self.date_ent3 = Entry(self.left3, width=15)
        self.date_ent3.place(x=250, y=520)

        # entry for right labels
        self.idright_ent3 = Entry(self.right3, width=20)
        self.idright_ent3.insert(END, "1002")
        self.idright_ent3.place(x=200, y=140)
        self.pwright_ent3 = Entry(self.right3, width=20)
        self.pwright_ent3.insert(END, "2")
        self.pwright_ent3.place(x=200, y=200)


        # Button to register
        self.staffre = Button(self.left3, text='staff register', width=15, height=2, bg='white', command=self.staffregister)
        self.staffre.place(x=250, y=580)
        # Button to login
        self.stafflo = Button(self.right3, text='staff login', width=15, height=2, bg='white', command=self.stafflogin)
        self.stafflo.place(x=200, y=300)

    def staffregister(self):
        # getting the user inputs
        self.val20 = self.staffidleft_ent3.get()
        self.val21 = self.nameleft_ent3.get()
        self.val22 = self.pwleft_ent3.get()
        self.val23 = self.age_ent3.get()
        self.val24 = self.gender_ent3.get()
        self.val25 = self.phone_ent3.get()
        self.val26 = self.isdr_ent3.get()
        self.val27 = self.date_ent3.get()

        if self.val20 == '' or self.val21 == '' or self.val22 == '' or self.val23 == '' or self.val24 == '' or self.val25 == '' or self.val26 == '' or self.val27 == '':
            tkinter.messagebox.showinfo('Warning', 'Please fill up all the boxes')
        else:
            sql3 = "INSERT INTO staffbasic (staffID,staffName,password,age,gender,phone,isDr,Date1)VALUES(?,?,?,?,?,?,?,?)"
            c_staff_reg.execute(sql3,(self.val20, self.val21, self.val22, self.val23, self.val24, self.val25, self.val26, self.val27))
            conn_staff_reg.commit()
            tkinter.messagebox.showinfo('Confirmation','registration for ' + self.val21 + ' is successful.')


    def stafflogin(self):
        # getting the user inputs
        self.val28 = self.idright_ent3.get()
        self.val29 = self.pwright_ent3.get()

        re_staff_id_pw = c_staff_reg.execute("SELECT staffID,password FROM staffbasic")
        dict_staff_id_pw = {}

        for row in re_staff_id_pw:
            i = row[0]
            p = row[1]
            dict_staff_id_pw[i] = p

            if i not in li_exi_staffID:
                li_exi_staffID.append(i)

        if self.val28 == '' or self.val29 == '':
            tkinter.messagebox.showinfo('Warning', 'Please fill up all the boxes')

        elif len(self.val28) != 4:
            tkinter.messagebox.showinfo('Warning', 'Please enter your 4-digit staff ID')

        elif dict_staff_id_pw.get(int(self.val28) != int(self.val29)):
            tkinter.messagebox.showinfo('Warning', 'Invalid Password.')

        elif int(self.val28) not in li_exi_staffID:
            tkinter.messagebox.showinfo('Warning', 'Invalid staff ID.')

        else:
            tkinter.messagebox.showinfo('Confirmation', 'Login successful!')
            # create the object
            root4 = Tk()
            r4 = WindowForstaffHome(root4, self.val28)

            # resolution of the window
            root4.geometry('1200x720+0+0')

            # preventing the resize feature
            root4.resizable(False, False)

            # end the loop
            root4.mainloop()