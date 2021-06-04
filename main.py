from tkinter import *
from tkinter import font
import tkinter.ttk
import tkinter.ttk
import Show
import requests
import shutil
import os
import time
from PIL import Image
import urllib.request
import Smtp
# MIMEMultipart의 MIME을 생성합니다.
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import SearchPage
import Gmail
import Telegramteller

class Main:
    def __init__(self):
        self.FindShow = Show.Contents()
        self.window = Tk()
        self.window.title("공연 전시 정보 검색")
        notebook=tkinter.ttk.Notebook(self.window,width=1200,height=800)
        notebook.pack()
        SearchPage1=Frame(self.window)
        notebook.add(SearchPage1,text='검색')
        _page1=SearchPage.Page1(SearchPage1,self.FindShow)
        GMAIL=Frame(self.window)
        notebook.add(GMAIL,text='메일')
        _page2=Gmail.MailSend(GMAIL,self.FindShow)


    def Running(self):
        Telegramteller.Running()
        self.window.mainloop()

main=Main()
main.Running()