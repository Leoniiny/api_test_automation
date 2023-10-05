# @Time : 2023/10/5 16:30
# @Author : 雷洋平
# @File : drafts.py
# @Software: PyCharm
# @Function: 脚本草稿
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
from util_layer.Dynamic_path import *


"""
1、初始化SMTP信息
2、设置邮箱的正文内容格式
3、运用os 命令压缩文件
4、将压缩文件添加到附件
5、与服务器建立链接
6、发送带有附件的邮件
"""
# 1、初始化SMTP信息
smtp_server = "smtp.qq.com"
smtp_server_port = 465
sender_mail = "1962560722@qq.com"
receivers_mail = "582021620@qq.com"
user_nickname = ""
password = "vmhxkkjmurqkbhgh"
subject = "Allure Report"
report_url = "http://localhost:63342/api_test_automation/reporter_layer/allure_report/index.html"

# 2、设置邮箱的正文内容格式
message = MIMEMultipart(_subtype='mixed')
message["From"] = Header(f"{user_nickname} <{sender_mail}>")
message["To"] = Header(receivers_mail, "utf-8")
message["Subject"] = Header(subject, "utf-8")

# 构造邮件数据
# 构造邮件正文数据
# content = "带附件的邮件"
content = f"""
            <p>Hello all,</p>
            <p>View the test report please <a href="{report_url}">click here</a></p>
            <p></p>
            <p>Thanks</p>"""

content_obj = MIMEText(content, 'html', 'utf-8')
message.attach(content_obj)

# 3、运用os 命令压缩文件
os.system(rf"rar a  {REPORT_PATH}\allure_report.rar {REPORT_PATH}\allure_report")

# 构造邮件附件数据
attachment = MIMEApplication(open(rf"{REPORT_PATH}\allure_report.rar", 'rb').read())
attachment.add_header('Content-Disposition', 'attachment', filename='report.rar')
message.attach(attachment)

# 连接SMTP 服务器
smtp_Obj = smtplib.SMTP_SSL(smtp_server,smtp_server_port)
smtp_Obj.login(user=sender_mail,password=password)
smtp_Obj.sendmail(sender_mail, receivers_mail, str(message))
smtp_Obj.quit()
print("邮件发送成功")








