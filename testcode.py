from tkinter import *

root =Tk()
canvas=Canvas(root,width=200,height=180,scrollregion=(0,0,520,520)) #创建canvas
canvas.place(x = 75, y = 265) #放置canvas的位置
frame=Frame(canvas) #把frame放在canvas里
frame.place(width=180, height=180) #frame的长宽，和canvas差不多的


vbar=Scrollbar(canvas,orient=VERTICAL) #竖直滚动条
vbar.place(x = 180,width=20,height=180)
vbar.configure(command=canvas.yview)

canvas.config(yscrollcommand=vbar.set) #设置
canvas.create_window((90,240), window=frame)  #create_window
root.mainloop()

---

# display the booking details
        # set scrollbar
        scrollbar2 = Scrollbar(self.downright)
        scrollbar2.pack(side=RIGHT, fill=Y)

        # booking的清單，此Listbox的長和寬會和 downright Frame 一樣大小
        bookingList = Listbox(a, yscrollcommand = scrollbar2.set, width=650,height=350,font=self.f3)

        # Print booking detail
        booking = c_bookapp.execute("SELECT appID,appointmentTime,isApproved,DrName FROM appointments WHERE ptID = (?)",(self.userID,))
        li_appID = []
        can_available = []
        for b in booking:
            appID_view = b[0]
            li_appID.append(appID_view)

            if int(b[2]) == 1:
                isAP = "Not approved"
                can_available.append(appID_view)
            elif int(b[2]) == 0:
                isAP = "Already cancelled"
            elif int(b[2]) == 3:
                isAP = "Already approved"

            bookingList.insert(END,str(b[0]) + '                                ' +str(b[1])+'                          '+ isAP +'                          '+ str(b[3]))

        bookingList.pack(side=TOP,fill='x')
        scrollbar2.config(command=bookingList.yview)
        self.li_appID = li_appID
        self.can_available = can_available