import sqlite3
from tkinter import *
from staffhome import WindowForstaffHome
import tkinter.messagebox
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

        # labels
        # ID for login
        self.idright3 = Label(self.right3, text="staffID:", font=self.f1, fg='black',bg='lavender')
        self.idright3.place(x=0, y=100)
        # password for login
        self.pwright3 = Label(self.right3, text="Password:", font=self.f1, fg='black', bg='lavender')
        self.pwright3.place(x=0, y=200)

        # entry for labels
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

        try:
            # gett the user inputs
            self.val26 = int(self.idright_ent3.get())
            self.val27 = int(self.pwright_ent3.get())

            # check the exist staffID and password
            self.check_exi_staffIDpw()

            if self.val26 not in self.li_exi_staffID_log:
                tkinter.messagebox.showinfo('Warning', 'Invalid staff ID.')

            elif self.dict_staff_id_pw.get(self.val26 != self.val27):
                tkinter.messagebox.showinfo('Warning', 'Invalid ID-Password pairs.')

            else:
                tkinter.messagebox.showinfo('Confirmation', 'Login successful!')

                # create the object
                root_sta_home = Tk()
                WindowForstaffHome(root_sta_home, self.val26)

                # resolution of the window
                root_sta_home.geometry('1200x720+0+0')

                # preventing the resize feature
                root_sta_home.resizable(False, False)

                # end the loop
                root_sta_home.mainloop()

        except ValueError:
            tkinter.messagebox.showinfo('Warning', 'The ID and password should only contain integers.')

    def check_exi_staffIDpw(self):

        # create a dictionary to store the id and password
        self.dict_staff_id_pw = {}
        # create a list to store exist staffIDs for staff to login
        self.li_exi_staffID_log = []

        # connect to database
        conn_sta_idpw = sqlite3.connect('Database.db')
        c_sta_idpw = conn_sta_idpw.cursor()

        re_staff_id_pw = c_sta_idpw.execute("SELECT staffID,password FROM staffbasic WHERE isActivated = 1")

        # store the id and pw
        for row in re_staff_id_pw:
            self.dict_staff_id_pw[row[0]] = row[1]
            self.li_exi_staffID_log.append(int(row[0]))

        # commit and close the DB
        conn_sta_idpw.commit()
        conn_sta_idpw.close()