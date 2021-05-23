from tkinter import *
from tkinter import font
import tkinter.ttk
import Show


class Main:
    window = Tk()
    Font = font.Font(window, size=15, weight='bold', family='Consolas')
    FindShow=Show.Contents()
    def __init__(self):
        self.window.title("공연 전시 정보 검색")
        self.img=PhotoImage(file="Image/BackGround00.png")
        self.bg=Canvas(self.window,width=1200,height=800)
        self.bg.create_image(0,0,image=self.img,anchor=NW)
        self.bg.place(x=0,y=0)
        self.bg.pack()
        self.logoimg = PhotoImage(file="Image/logo.png")
        logo = Label(self.window, image=self.logoimg)
        logo.pack()
        logo.place(x=0, y=0)
        global SearchListBox
        self.GmailImage=PhotoImage(file='Image/Gmail.png')
        button=Button(self.window,text='Gmail',image=self.GmailImage)
        button.pack()
        button.place(x=1200 - self.GmailImage.width(), y=100)
        self.PeriodEntry=Entry(self.window,font=self.Font,width=30,relief='ridge')
        self.PeriodEntry.pack()
        self.PeriodEntry.place(x=520,y=80)
        self.PeriodButton=Button(self.window,font=self.Font,text="검색",command=self.FindShow.SearchPeriod)
        self.PeriodButton.pack()

        self.FindShow.SetPeriodEntry(self.PeriodEntry)
        self.PeriodButton.place(x=870,y=80)
        self.AreaEntry = Entry(self.window, font=self.Font, width=30, relief='ridge')
        self.AreaEntry.pack()
        self.AreaEntry.place(x=520, y=170)
        self.AreaButton = Button(self.window, font=self.Font, text="검색", command=self.FindShow.SearchArea)
        self.AreaButton.pack()
        self.FindShow.SetAreaEntry(self.AreaEntry)
        self.AreaButton.place(x=870, y=170)

        self.ResultScrollBar=Scrollbar(self.window)
        self.ResultScrollBar.pack()
        self.ResultScrollBar.place(x=870,y=350)
        self.ResultText=Text(self.window,width=49,height=27,borderwidth=5,relief='ridge',yscrollcommand=self.ResultScrollBar.set)
        self.ResultText.pack()
        self.ResultText.place(x=520,y=350)
        self.ResultScrollBar.config(command=self.ResultText.yview)
        self.ResultText.configure(state='disabled')
        self.window.mainloop()

Main()