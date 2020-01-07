import sqlite3
from tkinter import *
import tkinter.messagebox
import tkinter.font as tkFont
from dr_view_avail_date import WindowForViewAvail

import calendar as cd
from datetime import timedelta, date
import datetime


# get time
today = datetime.date.today()
t = str(today).split('-')

class WindowForappDate:

    def __init__(self, appD,staffID):
        self.appD = appD
        self.staffID = staffID

        # create a frame
        self.leftappD = Frame(appD, width=630, height=720, bg='pink')
        self.leftappD.pack(side=LEFT)

        # create font
        self.f1 = tkFont.Font(family='times', size='16')

        # headings
        self.lhad = Label(self.appD, text="Manage dates", font=self.f1, fg='black', bg='pink')
        self.lhad.place(x=0, y=0)

        #labels
        self.lm = Label(self.appD, text="Enter the month of this year, eg.1 ", font=self.f1, fg='black',bg='pink')
        self.lm.place(x=0, y=160)
        self.lm = Label(self.appD, text="Column order: appointment Date ID, Week, Date. ", font=self.f1, fg='black', bg='pink')
        self.lm.place(x=0, y=250)
        self.lw = Label(self.appD, text="Enter the week of this year, eg.4 ", font=self.f1, fg='black', bg='pink')
        self.lw.place(x=0, y=440)
        self.ld = Label(self.appD, text="Enter the date in the next 7-30 days using 2020-XX-XX ", font=self.f1, fg='black', bg='pink')
        self.ld.place(x=0, y=480)

        self.ldel = Label(self.appD, text="Enter the adID no. you want to delete: ", font=self.f1, fg='black', bg='pink')
        self.ldel.place(x=0, y=580)

        # Entry
        self.lm_ent = Entry(self.appD, width=3)
        self.lm_ent.place(x=220, y=160)
        self.lw_ent = Entry(self.appD, width=3)
        self.lw_ent.place(x=220, y=442)
        self.ld_ent = Entry(self.appD, width=9)
        self.ld_ent.place(x=360, y=480)
        self.delad_ent = Entry(self.appD, width=3)
        self.delad_ent.place(x=300, y=580)

        # Button to see the calender
        self.bu_seecal = Button(self.appD, text='See the calendar', width=13, height=2, bg='white', command=self.seecal)
        self.bu_seecal.place(x=400, y=158)
        self.bu_seeappD = Button(self.appD, text='See my coming dates', width=16, height=2, bg='white',
                                 command=self.drViewAvailableDate)
        self.bu_seeappD.place(x=400, y=248)
        self.bu_submit = Button(self.appD, text='Add week and date', width=15, height=2, bg='white', command=self.adddate)
        self.bu_submit.place(x=470, y=478)
        self.bu_delaD = Button(self.appD, text='Delete your dates', width=15, height=2, bg='white',
                                command=self.delaD)
        self.bu_delaD.place(x=400, y=580)

        # see available future weeks and startdates (from Monday)
        self.see_ava_week()

    def see_ava_week(self):

        count = datetime.date(2020, 1, 6).isocalendar()
        week = count[1]
        self.w1 = week + 1
        start_w1 = today + timedelta(7)

        self.w2 = week + 2
        start_w2 = date(2020, 1, 6) + timedelta(7 * (self.w2 - 2))

        self.w3 = week + 3
        start_w3 = date(2020, 1, 6) + timedelta(7 * (self.w3 - 2))

        # labels for future weeks
        self.lw1 = Label(self.appD, text="Week " + str(self.w1) + "     Start date: " + str(start_w1) +
                                         "   * You cannot add those dates within 7 days. ", font=self.f1, fg='black',
                         bg='pink')
        self.lw1.place(x=0, y=330)
        self.lw2 = Label(self.appD, text="Week " + str(self.w2) + "     Start date: " + str(start_w2), font=self.f1,
                         fg='black', bg='pink')
        self.lw2.place(x=0, y=360)
        self.lw3 = Label(self.appD, text="Week " + str(self.w3) + "     Start date: " + str(start_w3), font=self.f1,
                         fg='black', bg='pink')
        self.lw3.place(x=0, y=390)

    def seecal(self):

        y = 2020

        try :
            # transfer user inputs
            m = int(self.lm_ent.get())

        except ValueError:
            tkinter.messagebox.showinfo('Warning', 'Please enter an integer between 1-12.')

        else:
            if m not in range(1,13) :
                tkinter.messagebox.showinfo('Warning', 'Please enter an integer between 1-12.')
            else:
                # assign the month's calendar to a multiline string
                str1 = cd.month(y, m)

                # create the window
                root_calen = Tk()
                root_calen.title("Monthly Calendar")

                # pick a fixed font like courier so spaces behave right
                output = Label(root_calen, text=str1, font=('courier',14),justify=LEFT, bg='lightgreen')
                output.pack(padx=3, pady=5)

                # preventing the resize feature
                root_calen.resizable(False, False)
                # end the loop
                root_calen.mainloop()


    def adddate(self):

        try:
            #transfer the input
            w = int(self.lw_ent.get())

        except ValueError:
            tkinter.messagebox.showinfo('Warning', 'Please check the box.')

        else:
            d = self.ld_ent.get().split('-')

            # calculate the date interval
            d_date = datetime.date(int(d[0]), int(d[1]), int(d[2]))
            interval_01 = (d_date - today).days

            # calculate the corresponding week of the date input
            interval_02 = (d_date - datetime.date(2019, 12, 30)).days
            w_number = (interval_02) // 7 + 1

            # check duplicate appointment dates
            self.check_dup()

            if w not in range(self.w1, self.w3 + 1):
                tkinter.messagebox.showinfo('Warning', 'Please enter a valid week number.')
            elif interval_01 < 7 or interval_01 > 28:
                tkinter.messagebox.showinfo('Warning', 'Invalid date.')
            elif w != w_number:
                tkinter.messagebox.showinfo('Warning', 'Invalid week and date pair.')
            elif self.ld_ent.get() in self.li_dup_date:
                tkinter.messagebox.showinfo('Warning', 'Duplicate available date.')
            else:
                self.findDrName()

                # add a new appointment Date
                conn_addDate = sqlite3.connect('Database.db')
                c_addDate = conn_addDate.cursor()

                c_addDate.execute("INSERT INTO appointmentDate (week,DrID,DrName,available_date) "
                                  "VALUES (?,?,?,?)", (w, self.staffID, self.val_drName, d_date))
                conn_addDate.commit()
                conn_addDate.close()
                tkinter.messagebox.showinfo('Confirmation', 'Successful!')

    def check_dup(self):

        # find duplicate dates
        conn_dup = sqlite3.connect('Database.db')
        c_dup = conn_dup.cursor()

        self.li_dup_date = []
        re_dup = c_dup.execute("SELECT available_date FROM appointmentDate WHERE DrID = (?) ",(self.staffID,))
        for re in re_dup:
            self.li_dup_date.append(re[0])

        conn_dup.commit()
        conn_dup.close()

    def findDrName(self):

        conn_drName = sqlite3.connect('Database.db')
        c_drName = conn_drName.cursor()

        re_drName = c_drName.execute("SELECT staffName FROM staffbasic WHERE staffID=(?)",(self.staffID,))
        for result in re_drName:
            self.val_drName = result[0]

        conn_drName.commit()
        conn_drName.close()

    def drViewAvailableDate(self):

        rootviewAvail = Tk()
        WindowForViewAvail(rootviewAvail, self.staffID)

        # resolution of the window
        rootviewAvail.geometry('530x210+0+0')

        rootviewAvail.resizable(True,True)
        # end the loop
        rootviewAvail.mainloop()

    def delaD(self):

        try:
            aD_get = int(self.delad_ent.get())

        except ValueError:
            tkinter.messagebox.showinfo('Warning', 'Please enter an integer.')

        else:
            # calculate the aDno. after today
            self.check_after_today()

            if aD_get not in self.li_after_today:
                tkinter.messagebox.showinfo('Warning', 'Invalid.')

            else:
                conn_delaD = sqlite3.connect('database.db')
                c_delaD = conn_delaD.cursor()

                c_delaD.execute("DELETE FROM appointmentDate WHERE adID = (?)",(aD_get,))
                conn_delaD.commit()
                conn_delaD.close()

                tkinter.messagebox.showinfo('Confirmation', 'Successful.')
                self.drViewAvailableDate()


    def check_after_today(self):

        conn_cal = sqlite3.connect('Database.db')
        c_cal = conn_cal.cursor()

        # find the all available dates
        re_cal = c_cal.execute("SELECT adID,available_date FROM appointmentDate WHERE DrID = (?)",
                                   (self.staffID,))
        self.li_after_today= []

        # store adIDs that are after today
        for re in re_cal:
            x = str(re[1]).split('-')

            if (x[0] < t[0]) or (x[0] == t[0] and x[1] < t[1]) or (x[0] == t[0] and x[1] == t[1] and (x[2] < t[2])):
                pass
            else:
                self.li_after_today.append(re[0])

        conn_cal.commit()
        conn_cal.close()