from tkinter import *
from staffhome import WindowForstaffHome
import tkinter.messagebox
import sqlite3
import tkinter.font as tkFont


# create a window for stafflogin
class WindowForstaffLogin:
    def __init__(self,staffreg):
        self.staffreg = staffreg

        # create a frame
        self.right3 = Frame(staffreg, width= 570, height = 720, bg = 'lavender')
        self.right3.pack(side=LEFT)

        # create font
        self.f1 = tkFont.Font(family='times', size='16')

        # headings
        self.rh3 = Label(self.right3, text="Staff login", font=self.f1, fg='black', bg='lavender')
        self.rh3.place(x=0, y=0)

        # RIGHT labels
        # ID for login
        self.idright3 = Label(self.right3, text="staffID:", font=self.f1, fg='black',bg='lavender')
        self.idright3.place(x=0, y=100)
        # password for login
        self.pwright3 = Label(self.right3, text="Password:", font=self.f1, fg='black', bg='lavender')
        self.pwright3.place(x=0, y=200)

        # entry for right labels
        self.idright_ent3 = Entry(self.right3, width=20)
        self.idright_ent3.insert(END, "1015")
        self.idright_ent3.place(x=200, y=140)
        self.pwright_ent3 = Entry(self.right3, width=20)
        self.pwright_ent3.insert(END, "15")
        self.pwright_ent3.place(x=200, y=200)

        # Button to login
        self.stafflo = Button(self.right3, text='staff login', width=15, height=2, bg='white', command=self.stafflogin)
        self.stafflo.place(x=200, y=300)

    def stafflogin(self):

        # getting the user inputs
        self.val26 = self.idright_ent3.get()
        self.val27 = self.pwright_ent3.get()

        # connect to database
        conn_sta_idpw = sqlite3.connect('Database.db')
        c_sta_idpw = conn_sta_idpw.cursor()

        re_staff_id_pw = c_sta_idpw.execute("SELECT staffID,password FROM staffbasic")

        # create a dictionary to store the id and password
        dict_staff_id_pw = {}
        # create a list to store exist staffIDs for staff to login
        li_exi_staffID_log = []

        for row in re_staff_id_pw:
            i = row[0]
            p = row[1]
            dict_staff_id_pw[i] = p
            li_exi_staffID_log.append(i)

        conn_sta_idpw.commit()
        conn_sta_idpw.close()

        if self.val26 == '' or self.val27 == '':
            tkinter.messagebox.showinfo('Warning', 'Please fill up all the boxes')

        elif  (not self.val26.isdigit()) or (not self.val27.isdigit()):
            tkinter.messagebox.showinfo('Warning', 'The ID and password should only contain integers.')

        elif len(self.val26) != 4:
            tkinter.messagebox.showinfo('Warning', 'Please enter your 4-digit staff ID')

        elif dict_staff_id_pw.get(int(self.val26) != int(self.val27)):
            tkinter.messagebox.showinfo('Warning', 'Invalid Password.')

        elif int(self.val26) not in li_exi_staffID_log:
            tkinter.messagebox.showinfo('Warning', 'Invalid staff ID.')

        else:
            tkinter.messagebox.showinfo('Confirmation', 'Login successful!')
            # create the object
            root4 = Tk()
            r4 = WindowForstaffHome(root4, self.val26)

            # resolution of the window
            root4.geometry('1200x720+0+0')

            # preventing the resize feature
            root4.resizable(False, False)

            # end the loop
            root4.mainloop()