from tkinter import *
import sqlite3
import tkinter.messagebox

# connect to the database for appointments
conn = sqlite3.connect('Database.db')

# create a cursor
c = conn.cursor()

# empty the list to later append the ids from the database
ids = []

class Window:
    def __init__(self,m):
        self.m = m

        # create a frame
        self.left = Frame(m, width=600, height = 720, bg='pink')
        self.left.pack(side=LEFT)

        self.right = Frame(m, width= 600, height = 720, bg = 'lightgreen')
        self.right.pack(side=RIGHT)

        # labels
        self.heading = Label(self.left, text="UCLH Appointments",font = ('arial 40 bold'),fg='black',bg='pink')
        self.heading.place(x=0,y=0)

        # NHS number
        self.id = Label(self.left, text="NHS number", font=('arial 20 bold'), fg='black', bg='pink')
        self.id.place(x=0, y=100)

        # patients' name
        self.name = Label(self.left, text="Patient's Name", font=('arial 20 bold'), fg='black', bg='pink')
        self.name.place(x=0,y=170)

        # age
        self.age = Label(self.left, text= 'Age', font=('arial 20 bold'), fg='black', bg='pink')
        self.age.place(x=0,y=240)

        # gender
        self.gender = Label(self.left, text='Gender', font=('arial 20 bold'), fg='black', bg='pink')
        self.gender.place(x=0, y=310)

        # phone
        self.phone = Label(self.left, text='Phone', font=('arial 20 bold'), fg='black', bg='pink')
        self.phone.place(x=0, y=380)

        # address
        self.address = Label(self.left, text='Address', font=('arial 20 bold'), fg='black', bg='pink')
        self.address.place(x=0, y=450)

        # Appointment Time
        self.time = Label(self.left, text='Appointment Time', font=('arial 20 bold'), fg='black', bg='pink')
        self.time.place(x=0,y=520)

        # entry for all labels
        self.id_ent = Entry(self.left, width=30)
        self.id_ent.place(x=200, y=100)

        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=200, y=170)

        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=200, y=240)

        self.gender_ent = Entry(self.left, width=30)
        self.gender_ent.place(x=200, y=310)

        self.phone_ent = Entry(self.left, width=30)
        self.phone_ent.place(x=200, y=380)

        self.address_ent = Entry(self.left, width=30)
        self.address_ent.place(x=200, y=450)

        # Button to add an appointment
        self.submit = Button(self.left, text = 'Add appointment', width=20, height=2,bg='white',command = self.add_appointment)
        self.submit.place(x=250, y=580)

    # Function to call when the button is clicked
    def add_appointment(self):
        # getting the user inputs
        self.val1 = self.id_ent.get()
        self.val2 = self.name_ent.get()
        self.val3 = self.age_ent.get()
        self.val4 = self.gender_ent.get()
        self.val5 = self.phone_ent.get()
        self.val6 = self.address_ent.get()
        self.val7 = 1

        if self.val1 == '' or self.val2 == '' or self.val3 =='' or self.val4 == '' or self.val5 == '' or self.val6 == '':
            tkinter.messagebox.showinfo('Warning','Please fill up all the boxes')
        else:
            sql = "INSERT INTO 'appointments' (Id, Name, Age, Gender, Phone, Address,Condition) VALUES(?,?,?,?,?,?,?)"
            c.execute(sql,(self.val1, self.val2, self.val3, self.val4, self.val5, self.val6, self.val7))
            conn.commit()
            tkinter.messagebox.showinfo('Confirmation', 'Appointment for'+ str(self.val2)+ 'has been submitted.')

# create the object
root = Tk()
r = Window(root)

# resolution of the window
root.geometry('1200x720+0+0')

# preventing the resize feature
root.resizable(False,False)

# end the loop
root.mainloop()