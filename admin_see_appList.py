from tkinter import *
import sqlite3
import tkinter.messagebox

class WindowForAdminSeeAppList():
    def __init__(self, adminsee,val30):
        self.adminsee = adminsee
        self.ptID = val30

        # set a scrollbar
        scrollbarAdminSee = Scrollbar(self.adminsee)
        scrollbarAdminSee.pack(side=RIGHT, fill=Y)

        # set a list to fit the frame
        appList = Listbox(self.adminsee, yscrollcommand=scrollbarAdminSee.set, width=400, height=210)

        conn_admin_see = sqlite3.connect('Database.db')
        c_admin_see = conn_admin_see.cursor()
        re_app = c_admin_see.execute("SELECT appID,appointmentTime,isApproved,DrName FROM appointments WHERE ptID = (?)",(self.ptID,))
        isApp = ''

        for re in re_app:
            if int(re[2]) == 1:
                isApp = "Not approved yet"
            elif int(re[2]) == 0:
                isApp = "Already cancelled"
            elif int(re[2]) == 2:
                isApp = "Already approved"
            appList.insert(END,
                           str(re[0]) + '         ' + str(re[1]) + '           ' + isApp + '        ' + str(re[3]))

        conn_admin_see.commit()
        conn_admin_see.close()

        appList.pack(side=TOP, fill='x')
        scrollbarAdminSee.config(command=appList.yview)