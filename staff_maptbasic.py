import sqlite3

from tkinter import *
import tkinter.messagebox
import tkinter.font as tkFont
from admin_see_appList import WindowForAdminSeeAppList


class WindowForMan_ptbasic:
    def __init__(self, maptb, staffID):

        self.maptb = maptb
        self.staffID = staffID

        # create frame
        self.leftmaptb = Frame(self.maptb, width=550, height=720, bg='pink')
        self.leftmaptb.pack(side=LEFT)
        self.rightmaptb = Frame(self.maptb, width=650, height=720, bg='light yellow')
        self.rightmaptb.pack(side=RIGHT)

        # create font
        self.f1 = tkFont.Font(family='times', size='16')

        # heading
        self.lhmaptb = Label(self.leftmaptb, text="Manage patients' basic files", font=self.f1, fg='black', bg='pink')
        self.lhmaptb.place(x=0, y=0)

        # Left Labels
        self.ptID = Label(self.leftmaptb, text="Enter patient's NHS number:", font=self.f1, fg='black', bg='pink')
        self.ptID.place(x=0, y=80)

        # entry for left labels
        self.ptIDleft_ent = Entry(self.leftmaptb, width=15)
        self.ptIDleft_ent.insert(END, "1234567890")
        self.ptIDleft_ent.place(x=200, y=80)

        # button for submitting
        self.ptIDleftsub = Button(self.leftmaptb, text="Submit", width=8, height=2, bg='white', command=self.ptIDsubmit)
        self.ptIDleftsub.place(x=400, y=78)

    def ptIDsubmit(self):

        try:
            # getting user inputs
            self.val30 = int(self.ptIDleft_ent.get())

            # check exist ptIDs
            conn_check_ID = sqlite3.connect('Database.db')
            c_check_ID = conn_check_ID.cursor()

            re_pt_id = c_check_ID.execute("SELECT ptID FROM ptbasic")

            li_exi_ptID = []
            for r in re_pt_id:
                li_exi_ptID.append(r[0])

            if self.val30 not in li_exi_ptID:
                tkinter.messagebox.showinfo('Warning',"The database doesn't have this patient. Please re-enter a valid number")
            else:
                # Button to see the appointments

                self.bu_seeapp = Button(self.maptb, text="See all appointments of the patient", width=25, height=2,font=self.f1,
                                        fg='black', command=self.appointmentList)
                self.bu_seeapp.place(x=0, y=270)
                self.l_detail = Label(self.maptb, text="Column order: Appointment no., date, approved state,  Dr. name.",
                                      font=self.f1, fg='black',bg='pink')
                self.l_detail.place(x=0, y=320)

                self.ptbasic_view()

        except ValueError:
            tkinter.messagebox.showinfo('Warning', 'Please enter an integer.')


    def appointmentList(self):

        rootappList = Tk()
        rappList = WindowForAdminSeeAppList(rootappList,self.val30)

        # resolution of the window
        rootappList.geometry('400x210+0+0')

        # preventing the resize feature
        rootappList.resizable(True, True)

        # end the loop
        rootappList.mainloop()

    def ptbasic_view(self):

        # connect to the database
        conn_mapt = sqlite3.connect('Database.db')
        # create a cursor
        c_mapt = conn_mapt.cursor()

        re_ptbasic = c_mapt.execute(
            "SELECT ptID,ptName,password,age,gender,phone,address,allergy from ptbasic WHERE ptID = (?)", (self.val30,))
        for data in re_ptbasic:
            ptID_view = data[0]
            ptName_view = data[1]
            password_view = data[2]
            age_view = data[3]
            gender_view = data[4]
            phone_view = data[5]
            address_view = data[6]
            allergy_view = data[7]

            # labels
            # NHS number
            lptIDview = Label(self.rightmaptb, text="Patient's NHS number :" + str(ptID_view), font=self.f1, fg='black',
                              bg='light yellow')
            lptIDview.place(x=0, y=40)
            # patients' name
            lnameview = Label(self.rightmaptb, text="Patient's name", font=self.f1, fg='black', bg='light yellow')
            lnameview.place(x=0, y=110)
            # password
            lpwview = Label(self.rightmaptb, text="Password", font=self.f1, fg='black', bg='light yellow')
            lpwview.place(x=0, y=180)
            # age
            lageview = Label(self.rightmaptb, text='Age', font=self.f1, fg='black', bg='light yellow')
            lageview.place(x=0, y=250)
            # gender
            lgenderview = Label(self.rightmaptb, text='Gender', font=self.f1, fg='black', bg='light yellow')
            lgenderview.place(x=0, y=320)
            # phone
            lphoneview = Label(self.rightmaptb, text='Phone', font=self.f1, fg='black', bg='light yellow')
            lphoneview.place(x=0, y=390)
            # address
            laddressview = Label(self.rightmaptb, text='Address', font=self.f1, fg='black', bg='light yellow')
            laddressview.place(x=0, y=460)
            # allergy
            lallergyview = Label(self.rightmaptb, text='Allergy', font=self.f1, fg='black', bg='light yellow')
            lallergyview.place(x=0, y=530)

            # entry for right labels
            self.nameview_ent = Entry(self.rightmaptb, width=15)
            self.nameview_ent.insert(END, str(ptName_view))
            self.nameview_ent.place(x=200, y=110)

            self.pwright_ent = Entry(self.rightmaptb, width=15)
            self.pwright_ent.insert(END, str(password_view))
            self.pwright_ent.place(x=200, y=180)

            self.ageview_ent = Entry(self.rightmaptb, width=15)
            self.ageview_ent.insert(END, str(age_view))
            self.ageview_ent.place(x=200, y=250)

            self.genderview_ent = Entry(self.rightmaptb, width=15)
            self.genderview_ent.insert(END, str(gender_view))
            self.genderview_ent.place(x=200, y=320)

            self.phoneview_ent = Entry(self.rightmaptb, width=15)
            self.phoneview_ent.insert(END, str(phone_view))
            self.phoneview_ent.place(x=200, y=390)

            self.addressview_ent = Entry(self.rightmaptb, width=15)
            self.addressview_ent.insert(END, str(address_view))
            self.addressview_ent.place(x=200, y=460)

            self.allergyview_ent = Entry(self.rightmaptb, width=15)
            self.allergyview_ent.insert(END, str(allergy_view))
            self.allergyview_ent.place(x=200, y=530)

            conn_mapt.commit()

            # button for submitting
            self.bu_update = Button(self.rightmaptb, text="Update info.", width=12, height=2,
                                    bg='white', command=self.update_info)
            self.bu_update.place(x=140, y=600)
            self.bu_delpt = Button(self.rightmaptb, text="Delete patient.", width=12, height=2,
                                    bg='white', command=self.delete_pt)
            self.bu_delpt.place(x=260, y=600)


    def update_info(self):

        # getting the user inputs
        self.val31 = self.nameview_ent.get()
        self.val32 = self.pwright_ent.get()
        self.val33 = self.ageview_ent.get()
        self.val34 = self.genderview_ent.get()
        self.val35 = self.phoneview_ent.get()
        self.val36 = self.addressview_ent.get()
        self.val37 = self.allergyview_ent.get()

        if self.val31 == '' or self.val32 == '' or self.val33 =='' or self.val34 == '' or self.val35 == '' or self.val36 == '' :
            tkinter.messagebox.showinfo('Warning','Please fill up all the boxes')

        elif (not self.val32.isdigit()) or (not self.val33.isdigit()):
            tkinter.messagebox.showinfo('Warning','Password and age must be only integers.')

        else:
            # connect to the database on register page
            conn_submit = sqlite3.connect('Database.db')
            # create a cursor
            c_submit = conn_submit.cursor()
            c_submit.execute("DELETE FROM ptbasic WHERE ptID = (?)",(self.val30,))

            sql4 = "INSERT INTO ptbasic (ptID,ptName,password,age,gender,phone,address,allergy)VALUES(?,?,?,?,?,?,?,?)"
            c_submit.execute(sql4,(self.val30,self.val31, self.val32, self.val33, self.val34, self.val35, self.val36, self.val37))
            conn_submit.commit()
            conn_submit.close()
            tkinter.messagebox.showinfo('Confirmation', 'modification for '+ self.val31 + 'is successful.')


    def delete_pt(self):

        tkinter.messagebox.showinfo('Warning', 'This will delete the patient.')
        # Delete the pt
        conn_delpt = sqlite3.connect('Database.db')
        c_delpt = conn_delpt.cursor()

        c_delpt.execute("DELETE FROM ptbasic WHERE ptID =(?)",(self.val30,))

        conn_delpt.commit()
        conn_delpt.close()

        tkinter.messagebox.showinfo('Confirmation', 'Successful!')
        self.ptIDsubmit()