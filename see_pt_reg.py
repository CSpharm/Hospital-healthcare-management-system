from tkinter import *
import tkinter.messagebox
import sqlite3
import tkinter.font as tkFont


class WindowForseePtReg():

    def __init__(self, ptreg):
        self.seeptreg = ptreg

        # set scrollbar
        scrollbarcon = Scrollbar(self.seeptreg)
        scrollbarcon.pack(side=RIGHT, fill=Y)
        # set a list to fit the frame
        reg_List = Listbox(self.seeptreg, yscrollcommand=scrollbarcon.set, width=500, height=300)

        # connect to the database
        conn_see_reg = sqlite3.connect('Database.db')
        # create a cursor
        c_see_reg = conn_see_reg.cursor()
        re_see_reg = c_see_reg.execute("SELECT ptID,ptName,address FROM ptbasic WHERE isconfirmed = 1")

        for result in re_see_reg:
            reg_List.insert(END,
                            str(result[0]) + '           ' + str(result[1]) + '             ' + str(result[2]))

        conn_see_reg.commit()
        conn_see_reg.close()

        reg_List.pack(side=LEFT, fill='x')
        scrollbarcon.config(command=reg_List.yview)