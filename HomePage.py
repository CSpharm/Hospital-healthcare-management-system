from tkinter import *
from pt_reg_log import WindowForptLogin
from staff_log import WindowForstaffLogin


# create a window for home
class WindowForHome:
    def __init__(self, h):
        self.h = h

        # create frame
        self.lefth = Frame(h, width=630, height = 720, bg='burlywood1')
        self.lefth.pack(side=LEFT)
        self.righth = Frame(h, width= 570, height = 720, bg = 'light yellow')
        self.righth.pack(side=RIGHT)

        # heading
        self.lhh = Label(self.lefth, text="Welcome to UCLH.", font = ('arial 30 bold'), fg='black', bg='burlywood1')
        self.lhh.place(x=0,y=0)

        # identity for pt / staff
        # Button for pt
        self.bu_pt = Button(self.lefth, text='I am a patient', width=20, height=2, bg='white', command=self.pt)
        self.bu_pt.place(x=200, y=300)
        # Button for staff
        self.bu_dr = Button(self.righth, text='I am staff', width=20, height=2, bg='white', command=self.staff)
        self.bu_dr.place(x=200, y=300)

    def pt(self):

        # link to the pt_reg_log
        # create the object
        rootpt = Tk()
        WindowForptLogin(rootpt)

        # resolution of the window
        rootpt.geometry('1200x720+0+0')

        # preventing the resize feature
        rootpt.resizable(False, False)

        # end the loop
        rootpt.mainloop()

    def staff(self):
        # create the object
        rootstaff = Tk()
        WindowForstaffLogin(rootstaff)

        # resolution of the window
        rootstaff.geometry('570x720+0+0')

        # preventing the resize feature
        rootstaff.resizable(False, False)

        # end the loop
        rootstaff.mainloop()


rooth = Tk()
rh = WindowForHome(rooth)

# resolution of the window
rooth.geometry('1200x720+0+0')

# preventing the resize feature
rooth.resizable(False, False)

# end the loop
rooth.mainloop()