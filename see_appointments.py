from tkinter import *
import sqlite3
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

        # connect to the database
        conn_see = sqlite3.connect('Database.db')
        # create a cursor
        c_see = conn_see.cursor()

        re_app = c_see.execute("SELECT appID,appointmentTime,isApproved,DrName FROM appointments WHERE ptID = (?)",(self.userID,))
        isAP = ''

        for re in re_app:

            aD = str(re[1]).split('-')

            if int(re[2]) == 1:
                isAP = "Not approved"
            elif int(re[2]) == 0:
                isAP = "Already cancelled"
            elif int(re[2]) == 2:
                isAP = "Already approved"

            # print the future appointments
            if (aD[0] > t[0]) or (aD[0] == t[0] and aD[1] > t[1]) or (aD[0] == t[0] and aD[1] == t[1] and (aD[2] > t[2])):
                appList.insert(END, str(b[0]) + '         ' + str(b[1]) + '           ' + isAP + '        ' + str(b[3]))

        conn_see.commit()
        conn_see.close()

        appList.pack(side=TOP, fill='x')
        scrollbar2.config(command=bookingList.yview)