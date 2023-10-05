# @Time : 2023/10/2 14:24
# @Author : 雷洋平
# @File : send_email_pro.py
# @Software: PyCharm
# @Function: 发送邮件
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
from util_layer.Dynamic_path import *


class SendMail:
    def __init__(self):
        self.smtp_server = "smtp.qq.com"

    def send_mail(self, smtp_server = "smtp.qq.com", smtp_server_port = 465, sender_mail ="1962560722@qq.com", receivers_mail ="582021620@qq.com"):
        smtp_server = smtp_server
        smtp_server_port = smtp_server_port
        sender_mail = sender_mail
        receivers_mail = receivers_mail
        user_nickname = "随便去个名字"
        password = "vmhxkkjmurqkbhgh"
        subject = "Allure Report"



if __name__ == '__main__':
    pass
    sm_obj = SendMail()
    sm_obj.send_mail()

