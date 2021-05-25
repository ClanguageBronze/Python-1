import mimetypes

from email.mime.base import MIMEBase
from email.mime.text import MIMEText

host="smtp.gmail.com"
port="587"
htmlFileName="test.png"
senderAddr="leedongsu97@gmail.com"
recipientAddr="leedongsu97@naver.com"

msg=MIMEBase("multiport","alternative")
msg['Subject']="Test email in Python 3.5"
msg['From']=senderAddr
msg['To']=recipientAddr

htmlFD=open(htmlFileName,'rb')
HtmlPart=MIMEText(htmlFD.read(),'html',_charset='UTF-8')
htmlFD.close()
msg.attach(HtmlPart)
