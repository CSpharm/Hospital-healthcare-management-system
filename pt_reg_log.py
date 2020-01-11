import sqlite3

from tkinter import *
import tkinter.messagebox
import tkinter.font as tkFont
from pt_appointments import WindowForAppointments


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
        self.idright_ent.place(x=200, y=140)

        self.pwright_ent = Entry(self.right, width=20)
        self.pwright_ent.place(x=200, y=200)

        # Button to register
        self.reg = Button(self.left, text = 'Patient register', width=20, height=2,bg='white',command = self.register)
        self.reg.place(x=250, y=600)
        # Button to login
        self.lo = Button(self.right, text='Patient login', width=20, height=2, bg='white', command=self.login)
        self.lo.place(x=200, y=300)

    def register(self):

        # check exist ptID
        self.check_exi_ptID()

        # getting the user inputs
        self.val1 = self.idleft_ent.get()
        self.val2 = self.nameleft_ent.get()
        self.val3 = self.pwleft_ent.get()
        self.val4 = self.age_ent.get()
        self.val5 = self.gender_ent.get()
        self.val6 = self.phone_ent.get()
        self.val7 = self.address_ent.get()
        self.val8 = self.allergy_ent.get()

        # if the inputs are blank
        if self.val1 == '' or self.val2 == '' or self.val3 =='' or self.val4 == '' \
                or self.val5 == '' or self.val6 == '' or self.val7 == '' or self.val8 == '':
            tkinter.messagebox.showinfo('Warning','Please fill up all the boxes')

        # limit the type and length of the id input
        elif (not self.val1.isdigit()) or len(self.val1) != 10:
            tkinter.messagebox.showinfo('Warning', 'Invalid NHS number. Please enter 10-digit NHS number')

        # if the id is in the database
        elif int(self.val1) in self.li_exi_ptID_01:
            tkinter.messagebox.showinfo('Warning', 'Invalid NHS number. The number is already in the database')

        # limit the type of the password and age input
        elif (not self.val3.isdigit()) or (not self.val4.isdigit()) :
            tkinter.messagebox.showinfo('Warning', 'Invalid age. Please enter only numbers')

        else:
            # add new pt registration to the database
            # connect to the database
            conn_ptreg = sqlite3.connect('Database.db')
            c_ptreg = conn_ptreg.cursor()

            sql = "INSERT INTO ptbasic (ptID,ptName,password,age,gender,phone,address,allergy,isconfirmed)" \
                  "VALUES(?,?,?,?,?,?,?,?,?)"
            c_ptreg.execute(sql,(self.val1, self.val2, self.val3, self.val4, self.val5, self.val6, self.val7,self.val8,1))

            # commit and close the database
            conn_ptreg.commit()
            conn_ptreg.close()

            # show the successful message
            tkinter.messagebox.showinfo('Confirmation', 'registration for  '+ self.val2 + ' has been submitted.'+
                                        'Please wait. You can login once the admin confirmed your registration. ')

    def login(self):

        # check the exist ptID and password
        self.check_exi_ptIDpw()

        try:
            # getting the user inputs
            self.val10 = self.idright_ent.get()
            self.val11 = self.pwright_ent.get()

            # check the ID is in the database and its confirmed state
            if int(self.val10) not in self.li_exi_ptID_02:
                tkinter.messagebox.showinfo('Warning', 'Cannot find this ID in the database.')

            # check the ID-password pairs
            elif self.dict_pt_id_pw.get(int(self.val10)) != (self.val11):
                tkinter.messagebox.showinfo('Warning', 'Invalid ID-password pairs.')

            else:
                # show successful message
                tkinter.messagebox.showinfo('Confirmation', 'Login successful!')

                # Login page
                # create the object
                root_ptlog = Tk()
                WindowForAppointments(root_ptlog ,self.val10)

                # resolution of the window
                root_ptlog .geometry('1200x720+0+0')
                # preventing the resize feature
                root_ptlog .resizable(False,False)
                # end the loop
                root_ptlog .mainloop()

        except ValueError:
            tkinter.messagebox.showinfo('Warning', 'Please enter only integers.')


    def check_exi_ptID(self):

        # check exist ptID in the DB
        # connect to the database
        conn_existID = sqlite3.connect('Database.db')
        c_existID = conn_existID.cursor()

        # create the list for existing pt ID
        self.li_exi_ptID_01 = []

        re_pt_id = c_existID.execute("SELECT ptID FROM ptbasic")

        for row in re_pt_id:
            i = row[0]
            self.li_exi_ptID_01.append(i)

        # commit and close the DB
        conn_existID.commit()
        conn_existID.close()

    def check_exi_ptIDpw(self):

        # check exist ptID and password in the DB
        conn_idpw = sqlite3.connect('Database.db')
        c_idpw = conn_idpw.cursor()

        # create a dictionary and a list to store
        self.dict_pt_id_pw = {}
        self.li_exi_ptID_02 = []

        re_pt_id_pw = c_idpw.execute("SELECT ptID,password FROM ptbasic WHERE isconfirmed = 2")

        for row in re_pt_id_pw:
            i = row[0]
            p = row[1]
            self.dict_pt_id_pw[i] = p
            self.li_exi_ptID_02.append(i)

        # commit and close the DB
        conn_idpw.commit()
        conn_idpw.close()