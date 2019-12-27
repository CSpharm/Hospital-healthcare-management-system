from tkinter import *
import sqlite3

# connect to the database for appointments
conn_see = sqlite3.connect('Database.db')

# create a cursor
c_see = conn_see.cursor()


class WindowtoseeAppointments:

    def __init__(self,see,userID):
        self.see = see
        self.userID = userID

        # display the booking details
        # set scrollbar
        scrollbar2 = Scrollbar(self.see)
        scrollbar2.pack(side=RIGHT, fill=Y)

        # booking的清單，此Listbox的長和寬會和 downright Frame 一樣大小
        bookingList = Listbox(self.see, yscrollcommand=scrollbar2.set, width=280, height=210)

        # Print booking detail
        booking = c_see.execute("SELECT appID,appointmentTime,isApproved,DrName FROM appointments WHERE ptID = (?)",
                                    (self.userID,))
        li_appID = []
        for b in booking:
            appID_view = b[0]
            li_appID.append(appID_view)

            if int(b[2]) == 1:
                isAP = "Not approved"
            elif int(b[2]) == 0:
                isAP = "Already cancelled"
            elif int(b[2]) == 2:
                isAP = "Already approved"

            bookingList.insert(END, str(b[0]) + '         ' + str(b[1]) + '           ' + isAP + '        ' + str(b[3]))

        bookingList.pack(side=TOP, fill='x')
        scrollbar2.config(command=bookingList.yview)