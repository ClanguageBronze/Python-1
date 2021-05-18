from tkinter import *
from tkinter import font
import tkinter.ttk

class Main:
    def __init__(self):
        window=Tk()
        window.title("공연 전시 정보 검색")
        self.img=PhotoImage(file="Image/BackGround00.png")
        self.bg=Canvas(window,width=1200,height=800)
        self.bg.create_image(0,0,image=self.img,anchor=NW)
        self.bg.place(x=0,y=0)
        self.bg.pack()
        self.logoimg = PhotoImage(file="Image/logo.png")
        logo = Label(window, image=self.logoimg)
        logo.pack()
        logo.place(x=0, y=0)
        global SearchListBox
        self.GmailImage=PhotoImage(file='Image/Gmail.png')
        button=Button(window,text='Gmail',image=self.GmailImage)
        button.pack()
        button.place(x=1200 - self.GmailImage.width(), y=100)
        PeriodScrollBar=Scrollbar(window)
        PeriodScrollBar.pack()
        PeriodScrollBar.place(x=850,y=120)
        TempFont= font.Font(window,size=30,weight='bold',family='Consolas')
        SearchListBox=Listbox(window,font=TempFont,activestyle='none',
                              width=15,height=1,borderwidth=1,relief='ridge',
                              yscrollcommand=PeriodScrollBar.set)
        SearchListBox.insert(1,"기간별 공연 검색")
        SearchListBox.pack()
        SearchListBox.place(x=520,y=120)
        PeriodScrollBar.config(command=SearchListBox.yview)
        AreaScrollBar = Scrollbar(window)
        AreaScrollBar.pack()
        AreaScrollBar.place(x=850, y=50)
        TempFont = font.Font(window, size=30, weight='bold', family='Consolas')
        AreaSearchListBox = Listbox(window, font=TempFont, activestyle='none',
                                width=15, height=1, borderwidth=1, relief='ridge',
                                yscrollcommand=AreaScrollBar.set)
        AreaSearchListBox.insert(1, "지역별 공연 검색")
        AreaSearchListBox.pack()
        AreaSearchListBox.place(x=520, y=50)
        AreaScrollBar.config(command=AreaSearchListBox.yview)

        ReleamScrollBar = Scrollbar(window)
        ReleamScrollBar.pack()
        ReleamScrollBar.place(x=850, y=190)
        TempFont = font.Font(window, size=30, weight='bold', family='Consolas')
        ReleamSearchListBox = Listbox(window, font=TempFont, activestyle='none',
                                    width=15, height=1, borderwidth=1, relief='ridge',
                                    yscrollcommand=ReleamScrollBar.set)
        ReleamSearchListBox.insert(1, "분야별 공연 검색")
        ReleamSearchListBox.pack()
        ReleamSearchListBox.place(x=520, y=190)
        ReleamScrollBar.config(command=ReleamSearchListBox.yview)

        SearchResultScrb=Scrollbar(window)
        SearchResultScrb.pack()
        SearchResultScrb.place(x=850,y=260)
        TempFont=font.Font(window,size=10,family='Consolas')

        SearchText=Text(window,font=TempFont,width=47,height=5,borderwidth=1,relief='ridge',
                        yscrollcommand=SearchResultScrb.set)
        SearchText.pack()
        SearchText.place(x=520,y=260)
        SearchResultScrb.config(command=SearchText.yview)

        SearchText.configure(state='disabled')

        window.mainloop()

Main()