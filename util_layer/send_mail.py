# @Time : 2023/9/29 21:58
# @Author : 雷洋平
# @File : send_mail.py
# @Software: PyCharm
# @Function:发送邮件
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


class SendEmail:
    def __init__(self):
        pass

    def send_mail(self):
        # 第三方SMTP 服务
        host = "smtp.qq.com"
        user = "1962560722@qq.com"
        pwd = "vmhxkkjmurqkbhgh"
        # 发送方
        sender = "lyp1962560722@163.com"
        # 接收方
        receivers = ["1962560722@qq.com"]

        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        message = MIMEText("pytest 发送allure报告", "plain", "utf-8")
        message["From"] = Header("测试报告")  # 发送者
        message["To"] = Header("接收报告者测试", "utf-8")  # 发送者

        subject = "Python SMTP 测试"
        message[subject] = Header("utf-8")

        try:
            smtp_obj = smtplib.SMTP(host=host)
            # smtp_obj = smtplib.SMTP_SSL(host=host)
            # smtp_obj.connect(host=host, port=465)
            smtp_obj.login(user=user, password=pwd)
            smtp_obj.sendmail(sender, receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error：无法发送邮件")


if __name__ == '__main__':
    obj = SendEmail()
    obj.send_mail()
