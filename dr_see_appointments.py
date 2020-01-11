import sqlite3
from tkinter import *
import tkinter.font as tkFont
import tkinter.messagebox
import datetime

today= datetime.date.today()
t = str(today).split('-')

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

        conn_drsee = sqlite3.connect('Database.db')
        c_drsee = conn_drsee.cursor()

        # only shows upcoming appointments that are waiting to be approved or already approved
        re_app = c_drsee.execute(
            "SELECT appID,ptID,ptName,appointmentTime,isApproved FROM appointments WHERE DrID=(?) "
            "AND (isApproved = 1 or isApproved = 2) ",(self.staffID,))

        isApproved_view = ''

        for re in re_app:

            aD2 =str(re[3]).split('-')

            if int(re[4]) == 1:
                isApproved_view = "Not approved yet"
            elif int(re[4]) == 0:
                isApproved_view = "Already cancelled"
            elif int(re[4]) == 2:
                isApproved_view = "Already approved"

            if (aD2[0] > t[0]) or (aD2[0] == t[0] and aD2[1] > t[1]) or\
                    (aD2[0] == t[0] and aD2[1] == t[1] and aD2[2] >= t[2]):
                appList.insert(END, '     ' + str(re[0]) + '             ' + str(re[1]) + '              ' +
                                    str(re[2]) + '                 ' + str(re[3]) + '            ' + isApproved_view)

        conn_drsee.commit()
        conn_drsee.close()
        appList.pack(side=BOTTOM, fill=BOTH)
        scrollbar3.config(command=appList.yview)