from tkinter import *
import sqlite3
import datetime

today = datetime.date.today()

class WindowForViewAvail:

    def __init__(self,avail,staffID):
        self.avail = avail
        self.staffID = staffID

        # display the booking details
        # set scrollbar
        scrollbar_view_avail = Scrollbar(self.avail)
        scrollbar_view_avail.pack(side=RIGHT, fill=Y)

        avail_List = Listbox(self.avail, yscrollcommand=scrollbar_view_avail.set, width=530, height=210)

        # connect to the database
        conn_avail = sqlite3.connect('database.db')
        # create a cursor
        c_avail = conn_avail.cursor()

        re_avail = c_avail.execute("SELECT adID,week,available_date FROM appointmentDate WHERE DrID = (?)", (self.staffID,))
        t = str(today).split('-')

        for re in re_avail:
            x = str(re[2]).split('-')

            if (x[0] > t[0]) or (x[0] == t[0] and x[1] > t[1] ) or (x[0] == t[0] and x[1] == t[1] and (x[2] >t[2])):
                avail_List.insert(END, str(re[0]) + '      ' + str(re[1]) + '           ' + str(re[2]))
            else:
                pass

        conn_avail.commit()
        conn_avail.close()
        avail_List.pack(side=TOP, fill='x')
        scrollbar_view_avail.config(command=avail_List.yview)