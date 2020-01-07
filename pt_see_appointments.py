import sqlite3
from tkinter import *
import datetime

today= datetime.datetime.today()
t = str(today).split('-')

class WindowtoseeAppointments:

    def __init__(self,see,userID):
        self.see = see
        self.userID = userID

        # set a scrollbar
        scrollbar2 = Scrollbar(self.see)
        scrollbar2.pack(side=RIGHT, fill=Y)

        # set a list to fit the frame
        appList = Listbox(self.see, yscrollcommand=scrollbar2.set, width=280, height=210)

        # find the coming appointments
        conn_see = sqlite3.connect('Database.db')
        c_see = conn_see.cursor()
        re_app = c_see.execute("SELECT appID,appointmentTime,isApproved,DrName FROM appointments WHERE ptID = (?)",(self.userID,))

        # set a blank string for isAp
        isAP = ''

        for re in re_app:

            # set the state to show on the window
            if int(re[2]) == 1:
                isAP = "Not approved"
            elif int(re[2]) == 0:
                isAP = "Already cancelled"
            elif int(re[2]) == 2:
                isAP = "Already approved"
            elif int(re[2]) == 3:
                isAP = "Already prescribed"

            aD = str(re[1]).split('-')

            # print the future appointments
            if (aD[0] > t[0]) or (aD[0] == t[0] and aD[1] > t[1]) or (aD[0] == t[0] and aD[1] == t[1] and (aD[2] > t[2])):
                appList.insert(END, str(re[0]) + '         ' + str(re[1]) + '           ' + isAP + '        ' + str(re[3]))

        # commit and close the db
        conn_see.commit()
        conn_see.close()

        appList.pack(side=TOP, fill='x')
        scrollbar2.config(command=appList.yview)