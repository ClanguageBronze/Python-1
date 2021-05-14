from tkinter import *
from tkinter import font
import tkinter.ttk

class Main:
    def __init__(self):
        window=Tk()
        window.title("공연 전시 정보 검색")
        frame=Frame(window,width=1200,height=800)
        frame.pack()
        self.GmailImage=PhotoImage(file='Image/Gmail.png')
        button=Button(frame,text='Gmail',image=self.GmailImage)
        button.pack()
        button.place(x=1200 - self.GmailImage.width(), y=0)
        window.mainloop()

Main()