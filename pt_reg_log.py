from tkinter import *
import tkinter.messagebox
import tkinter.font as tkFont
from appointments import WindowForAppointments
import sqlite3


class WindowForptLogin:

    def __init__(self,ptreg):
        self.ptreg = ptreg

        # create a frame
        self.left = Frame(ptreg, width=650, height = 720, bg='pink')
        self.left.pack(side=LEFT)
        self.right = Frame(ptreg, width= 550, height = 720, bg = 'lavender')
        self.right.pack(side=RIGHT)

        # create font
        self.f1 = tkFont.Font(family='times', size='16')
        # headings
        self.lh = Label(self.left, text="Patient register",font = self.f1,fg='black',bg='pink')
        self.lh.place(x=0,y=0)
        self.rh = Label(self.right, text="Patient login", font= self.f1, fg='black', bg='lavender')
        self.rh.place(x=0,y=0)

        # LEFT labels
        # NHS number
        self.idleft = Label(self.left, text="UserID(your NHS number)", font=self.f1, fg='black', bg='pink')
        self.idleft.place(x=0, y=70)
        # patients' name
        self.nameleft = Label(self.left, text="Patient's Name", font=self.f1, fg='black', bg='pink')
        self.nameleft.place(x=0,y=140)
        # password
        self.pwleft = Label(self.left, text="password(only numbers)", font=self.f1, fg='black', bg='pink')
        self.pwleft.place(x=0, y=210)
        # age
        self.age = Label(self.left, text= 'Age', font=self.f1, fg='black', bg='pink')
        self.age.place(x=0,y=280)
        # gender
        self.gender = Label(self.left, text='Gender', font=self.f1, fg='black', bg='pink')
        self.gender.place(x=0, y=350)
        # phone
        self.phone = Label(self.left, text='Phone', font=self.f1, fg='black', bg='pink')
        self.phone.place(x=0, y=420)
        # address
        self.address = Label(self.left, text='Address', font=self.f1, fg='black', bg='pink')
        self.address.place(x=0, y=490)
        # allergy
        self.allergy = Label(self.left, text='Allergy', font=self.f1, fg='black', bg='pink')
        self.allergy.place(x=0, y=540)
        # allergy detail
        self.allergy = Label(self.left, text='(including food and medicine)', font=self.f1, fg='black', bg='pink')
        self.allergy.place(x=0, y=570)
        # RIGHT labels
        # ID for login
        self.idright = Label(self.right, text="UserID(your NHS number):", font=self.f1, fg='black', bg='lavender')
        self.idright.place(x=0, y=100)
        # password for login
        self.pwright = Label(self.right, text="Password:",font=self.f1, fg='black', bg='lavender')
        self.pwright.place(x=0, y=200)

        # entry for left labels
        self.idleft_ent = Entry(self.left, width=15)
        self.idleft_ent.place(x=250, y=80)
        self.nameleft_ent = Entry(self.left, width=15)
        self.nameleft_ent.place(x=250, y=150)
        self.pwleft_ent = Entry(self.left, width=15)
        self.pwleft_ent.place(x=250, y=230)
        self.age_ent = Entry(self.left, width=15)
        self.age_ent.place(x=250, y=290)
        self.gender_ent = Entry(self.left, width=15)
        self.gender_ent.place(x=250, y=350)
        self.phone_ent = Entry(self.left, width=15)
        self.phone_ent.place(x=250, y=420)
        self.address_ent = Entry(self.left, width=15)
        self.address_ent.place(x=250, y=480)
        self.allergy_ent = Entry(self.left, width=15)
        self.allergy_ent.place(x=250, y=550)

        # entry for right labels
        self.idright_ent = Entry(self.right, width=20)
        self.idright_ent.insert(END, "1234567890")
        self.idright_ent.place(x=200, y=140)

        self.pwright_ent = Entry(self.right, width=20)
        self.pwright_ent.insert(0, "1")
        self.pwright_ent.place(x=200, y=200)

        # Button to register
        self.reg = Button(self.left, text = 'Patient register', width=20, height=2,bg='white',command = self.register)
        self.reg.place(x=250, y=600)
        # Button to login
        self.lo = Button(self.right, text='Patient login', width=20, height=2, bg='white', command=self.login)
        self.lo.place(x=200, y=300)

    # Function for pt to register
    def register(self):

        # connect to the database
        conn_existID = sqlite3.connect('Database.db')
        c_existID = conn_existID.cursor()

        # empty the list for existing pt ID
        li_exi_ptID = []

        re_pt_id = c_existID.execute("SELECT ptID FROM ptbasic")

        for row in re_pt_id:
            i = row[0]
            li_exi_ptID.append(i)

        conn_existID.commit()
        conn_existID.close()

        # getting the user inputs
        self.val1 = self.idleft_ent.get()
        self.val2 = self.nameleft_ent.get()
        self.val3 = self.pwleft_ent.get()
        self.val4 = self.age_ent.get()
        self.val5 = self.gender_ent.get()
        self.val6 = self.phone_ent.get()
        self.val7 = self.address_ent.get()
        self.val8 = self.allergy_ent.get()

        if self.val1 == '' or self.val2 == '' or self.val3 =='' or self.val4 == '' or self.val5 == '' or self.val6 == '' or self.val7 == '' or self.val8 == '':
            tkinter.messagebox.showinfo('Warning','Please fill up all the boxes')

        elif len(self.val1) != 10 or (not self.val1.isdigit()):
            tkinter.messagebox.showinfo('Warning', 'Invalid NHS number. Please enter 10-digit NHS number')

        elif int(self.val1) in li_exi_ptID:
            tkinter.messagebox.showinfo('Warning', 'Invalid NHS number. The number is already in the database')

        elif not self.val4.isdigit() :
            tkinter.messagebox.showinfo('Warning', 'Invalid age. Please enter only numbers')

        else:
            # connect to the database
            conn_ptreg = sqlite3.connect('Database.db')
            c_ptreg = conn_ptreg.cursor()

            sql = "INSERT INTO ptbasic (ptID,ptName,password,age,gender,phone,address,allergy,isconfirmed)VALUES(?,?,?,?,?,?,?,?,?)"
            c_ptreg.execute(sql,(self.val1, self.val2, self.val3, self.val4, self.val5, self.val6, self.val7,self.val8,1))
            conn_ptreg.commit()
            conn_ptreg.close()
            tkinter.messagebox.showinfo('Confirmation', 'registration for  '+ self.val2 + ' has been submitted.'+
                                        'Please wait. You can login once the admin confirmed your registration. ')

    def login(self):
        # getting the user inputs
        self.val10 = self.idright_ent.get()
        self.val11 = self.pwright_ent.get()

        # connect to the database on register page
        conn_idpw = sqlite3.connect('Database.db')
        c_idpw = conn_idpw.cursor()

        re_pt_id_pw = c_idpw.execute("SELECT ptID,password FROM ptbasic WHERE isconfirmed = 2")
        dict_pt_id_pw = {}
        li_exi_ptID = []

        for row in re_pt_id_pw:
            i = row[0]
            p = row[1]
            dict_pt_id_pw[i]=p
            li_exi_ptID.append(i)

        conn_idpw.commit()
        conn_idpw.close()

        if self.val10 == '' or self.val11 == '':
            tkinter.messagebox.showinfo('Warning','Please fill up all the boxes')

        elif len(self.val10)!= 10:
            tkinter.messagebox.showinfo('Warning', 'Please enter your 10-digit NHS number')

        elif int(self.val10) not in li_exi_ptID:
            tkinter.messagebox.showinfo('Warning', 'Invalid NHS number.')

        elif dict_pt_id_pw.get(int(self.val10)) != (self.val11):
            tkinter.messagebox.showinfo('Warning', 'Invalid Password.')

        else:
            tkinter.messagebox.showinfo('Confirmation','Login successful!')
            # create the object
            root1 = Tk()
            r1 = WindowForAppointments(root1,self.val10)

            # resolution of the window
            root1.geometry('1200x720+0+0')

            # preventing the resize feature
            root1.resizable(False,False)

            # end the loop
            root1.mainloop()