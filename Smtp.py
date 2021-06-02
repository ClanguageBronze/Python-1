import os,copy
import smtplib

from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.base64mime import body_encode as encode_base64


class MySMTP(smtplib.SMTP):
    def __init__(self, str_subject, str_image_file_name, str_cid_name, template, template_params):
        """이미지파일(str_image_file_name), 컨텐츠ID(str_cid_name)사용된 string template과 딕셔너리형 template_params받아 MIME 메시지를 만든다"""
        assert isinstance(template, Template)
        assert isinstance(template_params, dict)
        self.msg = MIMEMultipart()

        # e메일 제목을 설정한다
        self.msg['Subject'] = str_subject  # e메일 제목을 설정한다

        # e메일 본문을 설정한다
        str_msg = template.safe_substitute(**template_params)  # ${변수} 치환하며 문자열 만든다
        mime_msg = MIMEText(str_msg, 'html')  # MIME HTML 문자열을 만든다
        self.msg.attach(mime_msg)

        # e메일 본문에 이미지를 임베딩한다
        assert template.template.find("cid:" + str_cid_name) >= 0, 'template must have cid for embedded image.'
        assert os.path.isfile(str_image_file_name), 'image file does not exist.'
        with open(str_image_file_name, 'rb') as img_file:
            mime_img = MIMEImage(img_file.read())
            mime_img.add_header('Content-ID', '<' + str_cid_name + '>')
        self.msg.attach(mime_img)

    def get_message(self, str_from_email_addr, str_to_eamil_addrs):
        """발신자, 수신자리스트를 이용하여 보낼메시지를 만든다 """
        mm = copy.deepcopy(self.msg)
        mm['From'] = str_from_email_addr  # 발신자
        mm['To'] = ",".join(str_to_eamil_addrs)  # 수신자리스트
        return mm



    def login(self, user, password):


        def encode_cram_md5(challenge, user, password):
            challenge = base64.decodestring(challenge)
            response = user + " " + hmac.HMAC(password, challenge).hexdigest()
            return encode_base64(response)

        def encode_plain(user, password):
            s = "\0%s\0%s" % (user, password)
            return encode_base64(s.encode('ascii'), eol='')

        AUTH_PLAIN = "PLAIN"
        AUTH_CRAM_MD5 = "CRAM-MD5"
        AUTH_LOGIN = "LOGIN"

        self.ehlo_or_helo_if_needed()

        if not self.has_extn("auth"):
            raise SMTPException("SMTP AUTH extension not supported by server.")

        authlist = self.esmtp_features["auth"].split()
        preferred_auths = [AUTH_CRAM_MD5, AUTH_PLAIN, AUTH_LOGIN]

        authmethod = None
        for method in preferred_auths:
            if method in authlist:
                authmethod = method
                break

        if authmethod == AUTH_LOGIN:
            (code, resp) = self.docmd("AUTH",
                                      "%s %s" % (AUTH_LOGIN, encode_base64(user)))
            if code != 334:
                raise SMTPAuthenticationError(code, resp)
            (code, resp) = self.docmd(encode_base64(password))
        elif authmethod == AUTH_PLAIN:
            temp_encode_plain = str(encode_plain(user, password))
            temp_encode_plain = temp_encode_plain.replace("\n", "")
            (code, resp) = self.docmd("AUTH",
                                      AUTH_PLAIN + " " + temp_encode_plain)
        elif authmethod == AUTH_CRAM_MD5:
            (code, resp) = self.docmd("AUTH", AUTH_CRAM_MD5)
            if code == 503:
                return (code, resp)
            (code, resp) = self.docmd(encode_cram_md5(resp, user, password))
        elif authmethod is None:
            raise SMTPException("No suitable authentication method found.")
        if code not in (235, 503):
            raise SMTPAuthenticationError(code, resp)
        return (code, resp)

class EmailSender:
    """e메일 발송자"""

    def __init__(self, str_host, num_port=25):
        """호스트와 포트번호로 SMTP로 연결한다 """
        self.str_host = str_host
        self.num_port = num_port
        self.ss = smtplib.SMTP(host=str_host, port=num_port)
        # SMTP인증이 필요하면 아래 주석을 해제하세요.
        # self.ss.starttls() # TLS(Transport Layer Security) 시작
        # self.ss.login('계정명', '비밀번호') # 메일서버에 연결한 계정과 비밀번호

    def send_message(self, emailContent, str_from_email_addr, str_to_eamil_addrs):
        """e메일을 발송한다 """
        cc = emailContent.get_message(str_from_email_addr, str_to_eamil_addrs)
        self.ss.send_message(cc, from_addr=str_from_email_addr, to_addrs=str_to_eamil_addrs)
        del cc