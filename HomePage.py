from tkinter import *
from pt_reg_log import WindowForptLogin
from staff_reg_log import WindowForstaffLogin

# create a window for home
class WindowForHome:
    def __init__(self,h):
        self.h = h

        # create a frame
        self.lefth = Frame(h, width=630, height = 720, bg='pink')
        self.lefth.pack(side=LEFT)
        self.righth = Frame(h, width= 570, height = 720, bg = 'orange')
        self.righth.pack(side=RIGHT)

        # headings
        self.lhh = Label(self.lefth, text="Welcome to UCLH.",font = ('arial 40 bold'),fg='black',bg='pink')
        self.lhh.place(x=0,y=0)

        # identity for pt / staff
        # Button for pt
        self.bu_pt = Button(self.lefth, text='I am a patient', width=20, height=2, bg='white', command=self.pt)
        self.bu_pt.place(x=200, y=300)
        # Button for staff
        self.bu_dr = Button(self.righth, text='I am a staff', width=20, height=2, bg='white', command=self.dr)
        self.bu_dr.place(x=200, y=300)

    def pt(self):
        # link to the pt_reg_log
        # create the object
        root2 = Tk()
        r2 = WindowForptLogin(root2)

        # resolution of the window
        root2.geometry('1200x720+0+0')

        # preventing the resize feature
        root2.resizable(False, False)

        # end the loop
        root2.mainloop()

    def dr(self):
        # link to the pt_reg_log
        # create the object
        root3 = Tk()
        r3 = WindowForstaffLogin(root3)

        # resolution of the window
        root3.geometry('1200x720+0+0')

        # preventing the resize feature
        root3.resizable(False, False)

        # end the loop
        root3.mainloop()


rooth = Tk()
rh = WindowForHome(rooth)

# resolution of the window
rooth.geometry('1200x720+0+0')

# preventing the resize feature
rooth.resizable(False, False)

# end the loop
rooth.mainloop()