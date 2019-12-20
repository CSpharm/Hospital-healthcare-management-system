from tkinter import *
import sqlite3
import tkinter.messagebox

# connect to the database for appointments
conn1 = sqlite3.connect('Database.db')

# create a cursor
c1 = conn1.cursor()

class WindowForAppointments:
    def __init__(self,a):
        self.a = a

        # create a frame
        self.left2 = Frame(a, width=600, height = 720, bg='pink')
        self.left2.pack(side=LEFT)

        self.right2 = Frame(a, width= 600, height = 720, bg = 'lightgreen')
        self.right2.pack(side=RIGHT)

        # heading
        self.lh2 = Label(self.left2, text="Appointments",font = ('arial 40 bold'),fg='black',bg='pink')
        self.lh2.place(x=0,y=0)

        # Fixed Labels
        self.drnameleft = Label(self.left2, text="Doctors", font=('arial 20 bold'), fg='black', bg='pink')
        self.drnameleft.place(x=0, y=80)

        self.date1 = Label(self.left2, text="Date1", font=('arial 20 bold'), fg='black', bg='pink')
        self.date1.place(x=250, y=80)
        self.date2 = Label(self.left2, text="Date2", font=('arial 20 bold'), fg='black', bg='pink')
        self.date2.place(x=450, y=80)


        dr_namedate = c1.execute("SELECT DrName,Date1,Date2 FROM Drbasic")
        count = 0
        rb =IntVar()
        for row in dr_namedate:

            n = row[0]
            d1 = row[1]
            d2 = row[2]
            count += 1
            self.drname = Label(self.left2, text=n, font=('arial 20 bold'), fg='black', bg='pink')
            self.drname.place(x=0, y=50 + 70 * count)
            self.d1 = Radiobutton(self.left2, text=d1, font=('arial 20 bold'),fg='black',bg='pink', variable = count,value=count,command = lambda:self.booking(count))
            self.d1.place(x=250, y=50 + 70 * count)
            self.d2 = Radiobutton(self.left2, text=d2, font=('arial 20 bold'), fg='black',bg='pink',variable = count, value=count,command = lambda:self.booking(count))
            self.d2.place(x=450, y=50 + 70 * count)

        # NHS number
        self.id = Label(self.right2, text="NHS number:   ", font=('arial 17 bold'), fg='black', bg='lightgreen')
        self.id.place(x=0, y=50)

        # patients' name
        self.ptname = Label(self.right2, text="Patient's Name:   ", font=('arial 17 bold'), fg='black', bg='lightgreen')
        self.ptname.place(x=0,y=100)

        # Button to add an appointment
        self.submit = Button(self.right2, text = 'Add appointment', width=20, height=2,bg='white',command = self.add_appointment)
        self.submit.place(x=200, y=300)

    # book the appointment once the patient click one of the button
    def booking(self,count):
        li_dr_name_date = []
        dr_namedate2 = c1.execute("SELECT DrName,Date1,Date2 FROM Drbasic")
        count2 = 0
        for row in dr_namedate2:
            li_dr_name_date.append(row[0])
            count2 +=1
            print(count)

            if int(count) == int(count2):
                # exact Dr.name
                self.drnameright = Label(self.right2, text="Dr's Name:  "+ str(row[0]), font=('arial 17 bold'), fg='black',bg='lightgreen')
                self.drnameright.place(x=0, y=150)
                # exact Appointment Date
                self.time = Label(self.right2, text='Appointment Date: '+ str(row[1]), font=('arial 17 bold'), fg='black',bg='lightgreen')
                self.time.place(x=0, y=200)


    # Function to call when the button is clicked
    def add_appointment(self):

        #self.val1 = self.id_ent.get()
        #self.val2 = self.name_ent.get()
        self.val3 = 1

        #if self.val1 == '' or self.val2 == '' or self.val3 =='' or self.val4 == '' or self.val5 == '' or self.val6 == '':
            #tkinter.messagebox.showinfo('Warning','Please fill up all the boxes')
        #else:
            #sql = "INSERT INTO 'appointments' (Id, Name, Age, Gender, Phone, Address,Condition) VALUES(?,?,?,?,?,?,?)"
            #c.execute(sql,(self.val1, self.val2, self.val3, self.val4, self.val5, self.val6, self.val7))
            #conn.commit()
            #tkinter.messagebox.showinfo('Confirmation', 'Appointment for'+ str(self.val2)+ 'has been submitted.')