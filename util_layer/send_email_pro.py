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
        pass

    def send_mail(self, smtp_server = "smtp.qq.com", smtp_server_port = 465, sender_mail ="1962560722@qq.com", receivers_mail ="582021620@qq.com"):
        smtp_server = smtp_server
        smtp_server_port = smtp_server_port
        sender_mail = sender_mail
        receivers_mail = receivers_mail
        user_nickname = "随便去个名字"
        password = "vmhxkkjmurqkbhgh"
        subject = "Allure Report"

        message = MIMEMultipart()
        message["From"] = Header(f"{user_nickname} <{sender_mail}>")
        # message["To"] = Header(",".join(receivers_mail))
        message["To"] = Header(receivers_mail,"utf-8")
        message["Subject"] = Header(subject,"utf-8")

        with open(REPORT_PATH+ r"/allure_report/index.html", "rb") as file:
            html_part = MIMEApplication(file.read(), "html")
            html_part["Content-Disposition"] = 'attachment; filename="allure_report.html"'
            message.attach(html_part)

        server = smtplib.SMTP(smtp_server, smtp_server_port)
        server.login(sender_mail, password)
        server.sendmail(sender_mail, receivers_mail, message)
        print("发送成功")


if __name__ == '__main__':
    pass
    # with open(CONFIG_PATH + r"/email_config.yaml", mode="r") as f:
    #     datas = yaml.load(f, Loader=yaml.FullLoader)  # Loader=yaml.FullLoader 去除警告
    #     print(datas)
    sm_obj = SendMail()
    sm_obj.send_mail()

