from tkinter import *
import sqlite3
import tkinter.messagebox

# connect to the database for appointments
conn = sqlite3.connect('Database.db')

# create a cursor
c = conn.cursor()
# empty the list for existing ID
li_ID = []

class WindowForLogin:
    def __init__(self,m):
        self.m = m

        # create a frame
        self.left = Frame(m, width=650, height = 720, bg='pink')
        self.left.pack(side=LEFT)

        self.right = Frame(m, width= 550, height = 720, bg = 'lavender')
        self.right.pack(side=RIGHT)

        # labels
        self.lh = Label(self.left, text="Register",font = ('arial 40 bold'),fg='black',bg='pink')
        self.lh.place(x=0,y=0)

        self.rh = Label(self.right, text="Login", font=('arial 40 bold'), fg='black', bg='lavender')
        self.rh.place(x=0,y=0)

        # LEFT
        # NHS number
        self.idleft = Label(self.left, text="UserID(your NHS number)", font=('arial 20 bold'), fg='black', bg='pink')
        self.idleft.place(x=0, y=70)
        # patients' name
        self.name = Label(self.left, text="Patient's Name", font=('arial 20 bold'), fg='black', bg='pink')
        self.name.place(x=0,y=140)
        # password
        self.pwleft = Label(self.left, text="password(only numbers)", font=('arial 20 bold'), fg='black', bg='pink')
        self.pwleft.place(x=0, y=210)
        # age
        self.age = Label(self.left, text= 'Age', font=('arial 20 bold'), fg='black', bg='pink')
        self.age.place(x=0,y=280)
        # gender
        self.gender = Label(self.left, text='Gender', font=('arial 20 bold'), fg='black', bg='pink')
        self.gender.place(x=0, y=350)
        # phone
        self.phone = Label(self.left, text='Phone', font=('arial 20 bold'), fg='black', bg='pink')
        self.phone.place(x=0, y=420)
        # address
        self.address = Label(self.left, text='Address', font=('arial 20 bold'), fg='black', bg='pink')
        self.address.place(x=0, y=490)
        # birthday
        self.birthday = Label(self.left, text='Birthday', font=('arial 20 bold'), fg='black', bg='pink')
        self.birthday.place(x=0, y=560)
        # RIGHT
        # ID for login
        self.idright = Label(self.right, text="UserID(your NHS number):", font=('arial 20 bold'), fg='black', bg='lavender')
        self.idright.place(x=0, y=100)

        self.pwright = Label(self.right, text="Password:",font=('arial 20 bold'), fg='black', bg='lavender')
        self.pwright.place(x=0, y=200)

        # entry for left labels
        self.idleft_ent = Entry(self.left, width=20)
        self.idleft_ent.place(x=200, y=100)

        self.name_ent = Entry(self.left, width=20)
        self.name_ent.place(x=200, y=150)

        self.pwleft_ent = Entry(self.left, width=20)
        self.pwleft_ent.place(x=200, y=240)

        self.age_ent = Entry(self.left, width=20)
        self.age_ent.place(x=200, y=300)

        self.gender_ent = Entry(self.left, width=20)
        self.gender_ent.place(x=200, y=350)

        self.phone_ent = Entry(self.left, width=20)
        self.phone_ent.place(x=200, y=420)

        self.address_ent = Entry(self.left, width=20)
        self.address_ent.place(x=200, y=490)

        self.birthday_ent = Entry(self.left, width=20)
        self.birthday_ent.place(x=200, y=560)

        # entry for right labels
        self.idright_ent = Entry(self.right, width=20)
        self.idright_ent.place(x=200, y=140)

        self.pwright_ent = Entry(self.right, width=20)
        self.pwright_ent.place(x=200, y=200)

        # Button to register
        self.reg = Button(self.left, text = 'Register', width=20, height=2,bg='white',command = self.register)
        self.reg.place(x=200, y=610)

        # Button to login
        self.lo = Button(self.right, text='Login', width=20, height=2, bg='white', command=self.login)
        self.lo.place(x=200, y=300)


    # Function to call when the button is clicked
    def register(self):
        # getting the user inputs
        self.val1 = self.idleft_ent.get()
        self.val2 = self.name_ent.get()
        self.val3 = self.pwleft_ent.get()
        self.val4 = self.age_ent.get()
        self.val5 = self.gender_ent.get()
        self.val6 = self.phone_ent.get()
        self.val7 = self.address_ent.get()
        self.val8 = self.birthday_ent.get()

        if self.val1 == '' or self.val2 == '' or self.val3 =='' or self.val4 == '' or self.val5 == '' or self.val6 == '' or self.val7 == '' or self.val8 == '':
            tkinter.messagebox.showinfo('Warning','Please fill up all the boxes')
        else:
            sql = "INSERT INTO ptbasic (Id,ptName,password,age,gender,phone,address,birthday)VALUES(?,?,?,?,?,?,?,?)"
            c.execute(sql,(self.val1, self.val2, self.val3, self.val4, self.val5, self.val6, self.val7,self.val8))
            conn.commit()
            tkinter.messagebox.showinfo('Confirmation', 'registration for'+ str(self.val2)+ 'has been submitted. Now you can login')

    def login(self):
        # getting the user inputs
        self.val10 = self.idright_ent.get()
        self.val11 = self.pwright_ent.get()

        result1 = c.execute("SELECT ID,password FROM ptbasic")
        for row in result1:
            i = row[0]
            print(i)
            p = row[1]
            print(p)
            if i not in li_ID:
                li_ID.append(int(i))
            if (int(self.val10) == i) and (self.val11 !=p):
                tkinter.messagebox.showinfo('Warning', 'Invalid Password.')

        if self.val10 == '' or self.val11 == '':
            tkinter.messagebox.showinfo('Warning','Please fill up all the boxes')

        elif len(self.val10)!= 10:
            tkinter.messagebox.showinfo('Warning', 'Please enter your 10-digit NHS number')

        elif int(self.val10) not in li_ID:
            tkinter.messagebox.showinfo('Warning', 'Invalid NHS number.')

        else:
            print('Login successful!')

# create the object
root = Tk()
r = WindowForLogin(root)

# resolution of the window
root.geometry('1200x720+0+0')

# preventing the resize feature
root.resizable(False,False)

# end the loop
root.mainloop()