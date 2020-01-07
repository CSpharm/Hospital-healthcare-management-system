import sqlite3
from tkinter import *
import tkinter.font as tkFont


class WindowFordrseeappointments:

    def __init__(self,drseeapp,staffID):

        self.drseeapp = drseeapp
        self.staffID = staffID

        # create font
        self.f1 = tkFont.Font(family='times', size='16')

        self.appointmentList()

    def appointmentList(self):
        # set scrollbar
        scrollbar3 = Scrollbar(self.drseeapp)
        scrollbar3.pack(side=RIGHT, fill=Y)

        appList = Listbox(self.drseeapp, yscrollcommand=scrollbar3.set, width=650, height=150,font = self.f1)

        # connect to the database for appointments
        conn_drsee = sqlite3.connect('Database.db')
        # create a cursor
        c_drsee = conn_drsee.cursor()

        re_app = c_drsee.execute(
            "SELECT appID,ptID,ptName,appointmentTime,isApproved FROM appointments WHERE DrID=(?) "
            "AND (isApproved = 1 or isApproved = 2) ",(self.staffID,))

        for re in re_app:
            if int(re[4]) == 1:
                isApproved_view = "Not approved yet"
            elif int(re[4]) == 0:
                isApproved_view = "Already cancelled"
            elif int(re[4]) == 2:
                isApproved_view = "Already approved"

            appList.insert(END, '     ' + str(re[0]) + '             ' + str(re[1]) + '              ' +
                                str(re[2]) + '                 ' + str(re[3]) + '              ' + isApproved_view)

        conn_drsee.commit()
        conn_drsee.close()
        appList.pack(side=BOTTOM, fill=BOTH)
        scrollbar3.config(command=appList.yview)