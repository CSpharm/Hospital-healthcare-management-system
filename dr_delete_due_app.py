import sqlite3
from tkinter import *
import tkinter.messagebox
import tkinter.font as tkFont
import datetime
from dr_see_due_app import WindowForseedueapp

today = datetime.date.today()
t = str(today).split('-')


class WindowFordeletedueapp:

    def __init__(self,deldue,staffID):
        self.deldue = deldue
        self.staffID = staffID

        # create a frame
        self.leftdel = Frame(deldue, width=500, height = 500, bg='pink')
        self.leftdel.pack(side=LEFT)

        # create font
        self.F1 = tkFont.Font(family='arial', size='20', weight='bold')
        self.F2 = tkFont.Font(family='arial', size='30', weight='bold')

        # Button to see the due appointments
        self.bseedue = Button(self.leftdel, text='See your due appointments', width=20, height=2, bg='white',command=self.see_due)
        self.bseedue.place(x=285, y=50)

        # label for delete app
        self.delappno = Label(self.leftdel, text="Enter the appointment no.", font=self.F2, fg='black', bg='pink')
        self.delappno.place(x=0, y=270)

        # entry for delete app
        self.delappno_ent = Entry(self.leftdel, width = 3)
        self.delappno_ent.place(x=180, y=268)

        # Buttons to delete app
        self.delone = Button(self.leftdel, text='Delete a due appointment', width=22, height=2, bg='white',command=self.delone)
        self.delone.place(x=285, y=265)
        self.delall = Button(self.leftdel, text='Delete all due appointments', width=22, height=2, bg='white', command=self.delall)
        self.delall.place(x=285, y=400)

        # can only delete appointments that haven't been prescribed (isApproved !=3)
        # since the prescriptions are so important that can't be afffected!

        conn_d = sqlite3.connect('database.db')
        c_d = conn_d.cursor()

        # store the due app ID into the list
        self.li_appdel_ID = []

        # Choose appointments earlier than today and unprescribed (isApproved !=3)
        result_one = c_d.execute(
            "SELECT appID,appointmentTime FROM appointments WHERE (DrID = (?) AND isApproved != 3)", (self.staffID,))

        for r in result_one:
            x = str(r[1]).split('-')

            if (x[0] < t[0]) or (x[0] == t[0] and x[1] < t[1]) or (x[0] == t[0] and x[1] == t[1] and (x[2] < t[2])):
                self.li_appdel_ID.append(r[0])
            else:
                pass

        conn_d.commit()
        conn_d.close()

    def see_due(self):

        rootdue = Tk()
        WindowForseedueapp(rootdue,self.staffID)

        # resolution of the window
        rootdue.geometry('530x210+0+0')
        # end the loop
        rootdue.mainloop()

    def delone(self):

        try:
            self.val59 = int(self.delappno_ent.get())

        except ValueError:
            tkinter.messagebox.showinfo('Warning','Please enter an valid appointment number.')

        else:
            if self.val59 not in self.li_appdel_ID:
                tkinter.messagebox.showinfo('Warning', 'You can not delete this appointment.')

            else:
                # delete the appointment
                conn_delone = sqlite3.connect('database.db')
                c_delone = conn_delone.cursor()

                # delete the selected appointment
                c_delone.execute("DELETE FROM appointments WHERE appID = (?)", (self.val59,))
                conn_delone.commit()
                conn_delone.close()

                tkinter.messagebox.showinfo('Confirmation', 'Deletion for' + str(self.val59) + ' is successful.')

    def delall(self):

        # if the list isn't empty, delete all the due and unprescribed appointments
        if self.li_appdel_ID:

            tkinter.messagebox.showinfo('Warning', 'This will delete all your due appointments.')
            tu_appdel_ID = tuple(self.li_appdel_ID)

            conn_delall = sqlite3.connect('database.db')
            c_delall = conn_delall.cursor()

            c_delall.execute("DELETE FROM appointments WHERE appID = (?)", tu_appdel_ID)
            conn_delall.commit()
            conn_delall.close()

            tkinter.messagebox.showinfo('Confirmation', 'Successful!')

        # if the list is empty, show the message
        else:
            tkinter.messagebox.showinfo('Warning', "There isn't any due appointment.")



