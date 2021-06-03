import mimetypes
import os,copy
import smtplib
from Smtp import MySMTP,EmailSender
import SearchPage
from tkinter import *
from tkinter import font
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import Show

class MailSend:
    Title=''
    FromEmail='leedongsu97@gmail.com'

    def __init__(self,window,Find):
        self.window=window
        self.FindShow = Find
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

        self.GmailImage = PhotoImage(file='Image/Gmail.png')
        button = Button(self.window, text='Gmail', image=self.GmailImage,command=self.SendMail)
        button.pack()
        button.place(x=1200 - self.GmailImage.width(), y=100)
        self.EmailEntry = Entry(self.window, font=self.Font, width=30, relief='ridge')
        self.EmailEntry.pack()
        self.EmailEntry.place(x=520, y=80)

    def SendMail(self):
        str_subject = '공연전시 정보'
        self.ToEmail=self.EmailEntry.get()
        SearchIndex = self.FindShow.GetListBox().curselection()[0]
        if self.FindShow.m_bPeriod and self.FindShow.m_bArea:
            self.Title = self.FindShow.m_Common[0 + (SearchIndex * 7)]
        elif self.FindShow.m_bPeriod:
            self.Title = self.FindShow.PeriodDataList[0 + (SearchIndex * 7)]
        elif self.FindShow.m_bArea:
            self.Title = self.FindShow.AreaDataList[0 + (SearchIndex * 7)]
        template = Template("""<html>
                                            <head></head>
                                            <body>
                                                ${Title}.<br>
                                                <img src="cid:my_image1"><br>
                                                This is a test message.
                                            </body>
                                        </html>""")
        template_params = {'Title':self.Title}
        str_image_file_name = 'test.png'
        str_cid_name = 'my_image1'
        emailHTMLImageContent = MySMTP(str_subject, str_image_file_name, str_cid_name, template,
                                       template_params)

        str_from_email_addr = self.FromEmail  # 발신자
        str_to_eamil_addrs = [self.ToEmail]  # 수신자리스트
        e=EmailSender("smtp.gmail.com","587",self.FromEmail)
        e.send_message(emailHTMLImageContent, self.FromEmail, self.ToEmail)