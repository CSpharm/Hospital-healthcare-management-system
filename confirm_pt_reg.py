from tkinter import *
import tkinter.messagebox
import sqlite3
import tkinter.font as tkFont
from see_pt_reg import WindowForseePtReg


class WindowForConfirmPtReg:
    def __init__(self,con,staffID):
        self.con = con
        self.staffID = staffID

        # create frame
        self.fcon= Frame(self.con, width=700, height = 500, bg='pink')
        self.fcon.pack(side=LEFT)

        self.topcon = Frame(self.con, width=700, height=250, bg='pink')
        self.topcon.pack(side=TOP)
        self.downcon = Frame(self.con, width=700, height=250, bg='pink')
        self.downcon.pack(side=BOTTOM)

        # create font
        self.f1 = tkFont.Font(family='times', size='16')

        # headings
        self.lcon = Label(self.fcon, text="Confirm the registration from patients",fg='black',bg='pink',font=self.f1)
        self.lcon.place(x=0,y=0)

        # Labels to describe the registration list
        self.ldetail = Label(self.fcon, text="Column order: patient's NHS ID, name and address ", font=self.f1, fg='black', bg='pink')
        self.ldetail.place(x=0, y=330)

        # Button to see the registration list
        self.bu_pt = Button(self.fcon, text='See the registration list', width=20, height=2, bg='white',
                            command=self.seeRegistration)
        self.bu_pt.place(x=350, y=330)

        # Labels to confirm one registration
        self.lconone = Label(self.fcon, text="Enter the patient NHS ID : ", font=self.f1, fg='black', bg='pink')
        self.lconone.place(x=0, y=380)

        # entry to confirm one registration
        self.conone_ent = Entry(self.fcon, width=12)
        self.conone_ent.place(x=160, y=380)

        # Button for confirming one
        self.bu_conone = Button(self.fcon, text='Confirm one registration ', width=20, height=2, bg='white',
                            command=self.confirmOne)
        self.bu_conone.place(x=350, y=380)

        # Button for confirming all
        self.bu_conall = Button(self.fcon, text='Confirm all registration ', width=20, height=2, bg='white',
                            command=self.confirmAll)
        self.bu_conall.place(x=350, y=430)

    def seeRegistration(self):

        rootseeReg = Tk()
        rseeReg = WindowForseePtReg(rootseeReg)

        # resolution of the window
        rootseeReg.geometry('500x300+0+0')

        # preventing the resize feature
        rootseeReg.resizable(True,True)

        # end the loop
        rootseeReg.mainloop()

    def confirmOne(self):


        try:
            self.val60 = int(self.conone_ent.get())

        except ValueError:
            tkinter.messagebox.showinfo('Warning', 'Please enter a valid patient NHS number.')

        else:
            # check the patient ID is valid or not
            # create a list to store the ptID which are not confirmed yet
            # connect to database
            conn_check = sqlite3.connect('Database.db')
            c_check = conn_check.cursor()

            li_not_confirmed = []
            re_not_confirmed = c_check.execute("SELECT ptID FROM ptbasic WHERE isconfirmed = 1")
            for not_confirmed in re_not_confirmed:
                li_not_confirmed.append(not_confirmed[0])

            conn_check.commit()
            conn_check.close()

            if self.val60 not in li_not_confirmed:
                tkinter.messagebox.showinfo('Warning', 'Wrong NHS ID.')
            else:
                # connect to database
                conn_con_one = sqlite3.connect('Database.db')
                c_con_one = conn_con_one_reg.cursor()

                c_con_one.execute("UPDATE ptbasic SET isconfirmed = 2 WHERE ptID = (?)",(self.val60,))
                conn_con_one.commit()
                conn_con_one.close()
                tkinter.messagebox.showinfo('Confirmation', 'Successful!')

    def confirmAll(self):

        # connect to database
        conn_con_all = sqlite3.connect('Database.db')
        c_con_all = conn_con_all.cursor()

        c_con_all.execute("UPDATE ptbasic SET isconfirmed = 2 WHERE isconfirmed = 1")
        conn_con_all.commit()
        conn_con_all.close()
        print('hey dear')
        tkinter.messagebox.showinfo('Confirmation', 'Successful!')