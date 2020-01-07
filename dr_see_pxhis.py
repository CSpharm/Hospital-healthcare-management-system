from tkinter import *
import sqlite3

class WindowForPxHis:
    def __init__(self,pxhis,ptID):
        self.pxhis = pxhis
        self.ptID = ptID

        # set a list to fit the frame
        pre_List = Listbox(self.pxhis)
        # set scrollbar
        scrollbary = Scrollbar(self.pxhis)
        scrollbary.pack(side=RIGHT, fill=Y)

        pre_List.configure(yscrollcommand = scrollbary.set,width = 530, height = 360)

        # connect to the database
        conn_phis = sqlite3.connect('Database.db')
        # create a cursor
        c_phis = conn_phis.cursor()

        re_pre = c_phis.execute("SELECT * FROM prescription WHERE ptID = (?)",(self.ptID,))
        for r in re_pre:
            orderno = r[0]
            appdate = r[4]
            med1 = r[5]
            day1 = r[6]
            dos1 = r[7]
            adm1 = r[8]
            Drname = r[3]
            pre_List.insert(END, str(orderno)+ '    ' + str(appdate)+ '         '+str(med1) + '   '+ str(dos1) +'     '
                            +str(day1) +'                 '+ str(adm1) +'               '+ str(Drname))

        conn_phis.commit()
        conn_phis.close()

        pre_List.pack(side=LEFT, fill = 'x')
        scrollbary.config(command=pre_List.yview)