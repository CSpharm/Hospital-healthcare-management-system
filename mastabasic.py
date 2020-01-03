from tkinter import *
import sqlite3
import tkinter.messagebox

class WindowForMan_stabasic:
    def __init__(self, mastab, staffID):
        self.staffID = staffID
        self.mastab = mastab

        # create a frame
        self.leftmastab = Frame(mastab, width=550, height=720, bg='pink')
        self.leftmastab.pack(side=LEFT)
        self.rightmastab = Frame(mastab, width=650, height=720, bg='light yellow')
        self.rightmastab.pack(side=RIGHT)

        # heading
        self.lhmastab = Label(self.leftmastab, text="Manage staff's basic file", font=('arial 40 bold'), fg='black', bg='pink')
        self.lhmastab.place(x=0, y=0)

        # connect to the database
        conn_mastabasic = sqlite3.connect('Database.db')
        # create a cursor
        c_mastabasic = conn_mastabasic.cursor()
        re_stabasic = c_mastabasic.execute("SELECT * from staffbasic WHERE staffID = (?)",(self.staffID,))

        for sta in re_stabasic:
            staID_view = sta[0]
            staname_view = sta[1]
            stapassword_view = sta[2]
            staage_view = sta[3]
            stagender_view = sta[4]
            staphone_view = sta[5]
            stadate_view = sta[6]

            if sta[7] == 0:
                sta_isDr_view = 'not'
            elif sta[7] == 1:
                sta_isDr_view = 'is'
            else:
                sta_isDr_view = 'Unsure'


            # labels
            # ID
            self.staID = Label(self.rightmastab, text="Your staff ID: "+ str(staID_view), font=('arial 20 bold'), fg='black', bg='light yellow')
            self.staID.place(x=0, y=40)
            # staff's name
            self.nameview = Label(self.rightmastab, text="Your name", font=('arial 20 bold'), fg='black', bg='light yellow')
            self.nameview.place(x=0, y=110)
            # password
            self.pwview = Label(self.rightmastab, text="Password", font=('arial 20 bold'), fg='black',bg='light yellow')
            self.pwview.place(x=0, y=180)
            # age
            self.ageview = Label(self.rightmastab, text='Age', font=('arial 20 bold'), fg='black', bg='light yellow')
            self.ageview.place(x=0, y=250)
            # gender
            self.genderview = Label(self.rightmastab, text='Gender', font=('arial 20 bold'), fg='black', bg='light yellow')
            self.genderview.place(x=0, y=320)
            # phone
            self.phoneview = Label(self.rightmastab, text='Phone', font=('arial 20 bold'), fg='black', bg='light yellow')
            self.phoneview.place(x=0, y=390)
            # available date
            self.dateview = Label(self.rightmastab, text='Available Date: DD/MM', font=('arial 18 bold'), fg='black', bg='light yellow')
            self.dateview.place(x=0, y=460)
            self.dateviewde = Label(self.rightmastab, text="(If you aren't a doctor please fill 0)" , font=('arial 16 bold'),fg='black',bg='light yellow')
            self.dateviewde.place(x=0, y=485)

            # isDr
            self.isDrview = Label(self.rightmastab, text='Is a Doctor: '+str(sta_isDr_view) , font=('arial 20 bold'), fg='black',bg='light yellow')
            self.isDrview.place(x=0, y=540)

            # entry for right labels
            self.nameview_ent = Entry(self.rightmastab, width=15)
            self.nameview_ent.insert(END, str(staname_view))
            self.nameview_ent.place(x=200, y=110)

            self.pwview_ent = Entry(self.rightmastab, width=15)
            self.pwview_ent.insert(END, str(stapassword_view))
            self.pwview_ent.place(x=200, y=180)

            self.ageview_ent = Entry(self.rightmastab, width=15)
            self.ageview_ent.insert(END, str(staage_view))
            self.ageview_ent.place(x=200, y=250)

            self.genderview_ent = Entry(self.rightmastab, width=15)
            self.genderview_ent.insert(END, str(stagender_view))
            self.genderview_ent.place(x=200, y=320)

            self.phoneview_ent = Entry(self.rightmastab, width=15)
            self.phoneview_ent.insert(END, str(staphone_view))
            self.phoneview_ent.place(x=200, y=390)

            self.dateview_ent = Entry(self.rightmastab, width=15)
            self.dateview_ent.insert(END, str(stadate_view))
            self.dateview_ent.place(x=200, y=460)

            conn_mastabasic.commit()

            # button for submitting
            self.modifysub = Button(self.rightmastab, text="Submit", width=15, height=2,bg='white', command=self.modify_sta_submit)
            self.modifysub.place(x=200, y=560)

    def modify_sta_submit(self):

        # getting the user inputs
        self.val38 = self.nameview_ent.get()
        self.val39 = self.pwview_ent.get()
        self.val40 = self.ageview_ent.get()
        self.val41 = self.genderview_ent.get()
        self.val42 = self.phoneview_ent.get()
        self.val43 = self.dateview_ent.get()

        if self.val38 == '' or self.val39 == '' or self.val40 =='' or self.val41 == '' or self.val42 == '' or self.val43 == '' :
            tkinter.messagebox.showinfo('Warning','Please fill up all the boxes')

        elif not (self.val39.isdigit()) or (not self.val40.isdigit()):
            tkinter.messagebox.showinfo('Warning','Password and Age should be only integer.')

        else:
            # connect to the database
            conn_substabasic = sqlite3.connect('Database.db')
            # create a cursor
            c_substabasic = conn_substabasic.cursor()

            sql5 = "UPDATE staffbasic SET staffName=(?),password=(?),age=(?),gender=(?),phone=(?),Date1=(?) WHERE staffID = (?)"
            c_substabasic.execute(sql5,(self.val38, self.val39, self.val40, self.val41, self.val42, self.val43,self.staffID))
            conn_substabasic.commit()
            conn_substabasic.close()
            tkinter.messagebox.showinfo('Confirmation', 'modification for  ' + self.val38 + ' is successful.')