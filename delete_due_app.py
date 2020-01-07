import datetime
from tkinter import *
import tkinter.messagebox
import sqlite3
import tkinter.font as tkFont
from see_due_app import WindowForseedueapp

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

        # label for the entry
        self.delappno = Label(self.leftdel, text="Enter the appointment no.", font=self.F2, fg='black', bg='pink')
        self.delappno.place(x=0, y=270)

        # entry for delete appNo
        self.delappno_ent = Entry(self.leftdel, width = 3)
        self.delappno_ent.place(x=180, y=268)

        # Button
        self.delone = Button(self.leftdel, text='Delete a due appointment', width=22, height=2, bg='white',command=self.delone)
        self.delone.place(x=285, y=265)
        self.delall = Button(self.leftdel, text='Delete all due appointments', width=22, height=2, bg='white', command=self.delall)
        self.delall.place(x=285, y=400)

        # connect to the database
        conn_d = sqlite3.connect('database.db')
        # create a cursor
        c_d = conn_d.cursor()
        # store the due app ID into the list
        li_appdel_ID = []

        # Choose appointments earlier than today and unprescribed
        result_one = c_d.execute(
            "SELECT appID,appointmentTime FROM appointments WHERE (DrID = (?) AND isApproved != 3)", (self.staffID,))

        for r in result_one:
            x = str(r[1]).split('-')

            if (x[0] < t[0]) or (x[0] == t[0] and x[1] < t[1]) or (x[0] == t[0] and x[1] == t[1] and (x[2] < t[2])):
                li_appdel_ID.append(r[0])
            else:
                pass

        # let the function delone can use this list
        self.li_appdel_ID = li_appdel_ID
        conn_d.commit()
        conn_d.close()

    def see_due(self):

        rootdue = Tk()
        r11 = WindowForseedueapp(rootdue,self.staffID)

        # resolution of the window
        rootdue.geometry('530x210+0+0')
        # end the loop
        rootdue.mainloop()

    def delone(self):

        self.val59 = self.delappno_ent.get()

        if self.val59 == '':
            tkinter.messagebox.showinfo('Warning', 'Please fill the box if you only want to delete one due appointment.')

        elif not self.val59.isdigit():
            tkinter.messagebox.showinfo('Warning','Please enter an valid appointment number.')

        elif int(self.val59) not in self.li_appdel_ID:
            tkinter.messagebox.showinfo('Warning', 'You can not delete this appointment.')

        else:
            # connect to the database
            conn_delone = sqlite3.connect('database.db')
            # create a cursor
            c_delone = conn_delone.cursor()
            # delete the selected appointment
            c_delone.execute("DELETE FROM appointments WHERE appID = (?)", (self.val59,))
            conn_delone.commit()
            conn_delone.close()
            tkinter.messagebox.showinfo('Confirmation', 'Deletion for' + str(self.val59) + ' is successful.')

    def delall(self):

        if self.li_appdel_ID:
            tkinter.messagebox.showinfo('Warning', 'This will delete all your due appointments.')
            tu_appdel_ID = tuple(self.li_appdel_ID)

            # connect to the database
            conn_delall = sqlite3.connect('database.db')
            # create a cursor
            c_delall = conn_delall.cursor()
            # delete all the due appointments
            c_delall.execute("DELETE FROM appointments WHERE appID = (?)", tu_appdel_ID)
            conn_delall.commit()
            conn_delall.close()

            tkinter.messagebox.showinfo('Confirmation', 'Successful!')

        else:
            tkinter.messagebox.showinfo('Warning', "There isn't any due appointment.")



