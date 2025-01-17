from tkinter import *
from tkinter import font

import Show
import requests
import shutil
import os
import time
from PIL import Image
import urllib.request
import FindMap

class Page1():
    def __init__(self,window,Find):
        self.window=window
        self.FindShow = Find

        self.BackGround = []
        self.Font = font.Font(self.window, size=15, weight='bold', family='Consolas')
        self.img = PhotoImage(file="Image/BackGround00.png")
        self.bg = Canvas(self.window, width=1200, height=800)
        self.bg.create_image(0, 0, image=self.img, anchor=NW)
        self.bg.place(x=0, y=0)
        self.bg.pack()
        self.logoimg = PhotoImage(file="Image/logo.png")
        logo = Label(self.window, image=self.logoimg)
        logo.pack()
        logo.place(x=0, y=0)



        self.PeriodEntry = Entry(self.window, font=self.Font, width=30, relief='ridge')
        self.PeriodEntry.pack()
        self.PeriodEntry.place(x=520, y=80)
        self.PeriodButton = Button(self.window, font=self.Font, text="기간 검색", command=self.FindShow.SearchPeriod)
        self.PeriodButton.pack()

        self.FindShow.SetPeriodEntry(self.PeriodEntry)
        self.PeriodButton.place(x=870, y=80)
        self.AreaEntry = Entry(self.window, font=self.Font, width=30, relief='ridge')
        self.AreaEntry.pack()
        self.AreaEntry.place(x=520, y=170)
        self.AreaButton = Button(self.window, font=self.Font, text="지역 검색", command=self.FindShow.SearchArea)
        self.AreaButton.pack()
        self.FindShow.SetAreaEntry(self.AreaEntry)
        self.AreaButton.place(x=870, y=170)

        self.ResultScrollBar = Scrollbar(self.window)
        self.ResultScrollBar.pack()
        self.ResultScrollBar.place(x=1020, y=350)
        TempFont = font.Font(self.window, size=10, weight='bold', family='Consloas')
        self.ResultText = Listbox(self.window, font=TempFont, width=130, height=10, borderwidth=5, relief='ridge',
                                  yscrollcommand=self.ResultScrollBar.set)
        self.FindShow.SetListBox(self.ResultText)
        self.ResultText.pack()

        self.ResultText.place(x=100, y=350)
        self.ResultScrollBar.config(command=self.ResultText.yview)

        self.Imagebut = Button(self.window, text='Image', command=self.FindImage)
        self.Imagebut.pack()
        self.Imagebut.place(x=1050, y=450)
        irmg = PhotoImage(file="Back.png")
        self.PerformanceImage = Label(self.window, image=irmg)

        self.PerformanceImage.pack()
        self.PerformanceImage.place(x=200, y=40)

    def FindImage(self):
        SearchIndex = self.ResultText.curselection()[0]
        if self.FindShow.m_bPeriod and self.FindShow.m_bArea:
            self.urlImage = self.FindShow.m_Common[6 + (SearchIndex * 9)]
            FindMap.ReturnMap(self.FindShow.m_Common[8], self.FindShow.m_Common[7])
        elif self.FindShow.m_bPeriod:
            self.urlImage = self.FindShow.PeriodDataList[6 + (SearchIndex * 9)]
            FindMap.ReturnMap(self.FindShow.PeriodDataList[8], self.FindShow.PeriodDataList[7])
        elif self.FindShow.m_bArea:
            self.urlImage = self.FindShow.AreaDataList[6 + (SearchIndex * 9)]
            FindMap.ReturnMap(self.FindShow.AreaDataList[8], self.FindShow.AreaDataList[7])
        urllib.request.urlretrieve(self.urlImage, "test.png")
        self.rimg = Image.open("test.png")
        Img = self.rimg.resize((300, 300))
        Img.save("test.png")
        my_img = PhotoImage(file="test.png")
        self.PerformanceImage.config(image=my_img)
        my_img.image = my_img



    def GetUrlImage(self):
        return self.urlImage
    def GetFindShow(self):
        return self.FindShow

