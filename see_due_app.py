from tkinter import *
import sqlite3
import datetime

today = datetime.date.today()

class WindowForseedueapp:

    def __init__(self,due,staffID):
        self.due = due
        self.staffID = staffID

        # display the booking details
        # set scrollbar
        scrollbar4 = Scrollbar(self.due)
        scrollbar4.pack(side=RIGHT, fill=Y)

        dueappList = Listbox(self.due, yscrollcommand=scrollbar4.set, width=530, height=210)


        t = str(today).split('-')

        # connect to the database
        conn_due = sqlite3.connect('database.db')
        # create a cursor
        c_due = conn_due.cursor()

        due_app = c_due.execute("SELECT appID,ptID,ptName,appointmentTime,isApproved FROM appointments WHERE (DrID = (?) AND isApproved != 3)",
                                    (self.staffID,))
        for d in due_app:
            if int(d[4]) == 0:
                isAP = "Cancelled"
            elif int(d[4]) == 1:
                isAP = "Waiting to be approved"
            elif int(d[4]) == 2:
                isAP = "Approved"

            x = str(d[3]).split('-')

            if (x[0] < t[0]) or (x[0] == t[0] and x[1] < t[1] ) or (x[0] == t[0] and x[1] == t[1] and (x[2] <t[2])):
                dueappList.insert(END, str(d[0]) + '      ' + str(d[1]) + '           ' + str(d[2]) + '           ' +
                                  str(d[3]) + '           ' +isAP + '        ')
            else:
                pass

        conn_due.commit()
        conn_due.close()
        dueappList.pack(side=TOP, fill='x')
        scrollbar4.config(command=dueappList.yview)