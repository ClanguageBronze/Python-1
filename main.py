from tkinter import *
from tkinter import font
import tkinter.ttk

class Main:
    def __init__(self):
        window=Tk()
        window.title("공연 전시 정보 검색")
        global SearchListBox
        frame=Frame(window,width=1200,height=800)
        frame.pack()
        self.GmailImage=PhotoImage(file='Image/Gmail.png')
        button=Button(frame,text='Gmail',image=self.GmailImage)
        button.pack()
        button.place(x=1200 - self.GmailImage.width(), y=100)
        PeriodScrollBar=Scrollbar(window)
        PeriodScrollBar.pack()
        PeriodScrollBar.place(x=850,y=120)
        TempFont= font.Font(window,size=15,weight='bold',family='Consolas')
        SearchListBox=Listbox(window,font=TempFont,activestyle='none',
                              width=30,height=2,borderwidth=1,relief='ridge',
                              yscrollcommand=PeriodScrollBar.set)
        SearchListBox.pack()
        SearchListBox.place(x=520,y=120)
        PeriodScrollBar.config(command=SearchListBox.yview)
        AreaScrollBar = Scrollbar(window)
        AreaScrollBar.pack()
        AreaScrollBar.place(x=850, y=50)
        TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
        AreaSearchListBox = Listbox(window, font=TempFont, activestyle='none',
                                width=30, height=2, borderwidth=1, relief='ridge',
                                yscrollcommand=AreaScrollBar.set)
        AreaSearchListBox.pack()
        AreaSearchListBox.place(x=520, y=50)
        AreaScrollBar.config(command=AreaSearchListBox.yview)

        ReleamScrollBar = Scrollbar(window)
        ReleamScrollBar.pack()
        ReleamScrollBar.place(x=850, y=190)
        TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
        ReleamSearchListBox = Listbox(window, font=TempFont, activestyle='none',
                                    width=30, height=2, borderwidth=1, relief='ridge',
                                    yscrollcommand=ReleamScrollBar.set)
        ReleamSearchListBox.pack()
        ReleamSearchListBox.place(x=520, y=190)
        ReleamScrollBar.config(command=ReleamSearchListBox.yview)

        SearchResultScrb=Scrollbar(window)
        SearchResultScrb.pack()
        SearchResultScrb.place(x=850,y=260)
        TempFont=font.Font(window,size=10,family='Consolas')

        SearchText=Text(window,width=47,height=5,borderwidth=1,relief='ridge',
                        yscrollcommand=SearchResultScrb.set)
        SearchText.pack()
        SearchText.place(x=520,y=260)
        SearchResultScrb.config(command=SearchText.yview)

        SearchText.configure(state='disabled')

        window.mainloop()

Main()