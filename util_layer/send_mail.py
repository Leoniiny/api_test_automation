# @Time : 2023/9/30 9:15
# @Author : 雷洋平
# @File : send_mail.py
# @Software: PyCharm
# @Function: 发送邮件
import base64
import smtplib
# 导入构造邮件头部信息的库【必需】
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication


def send_mail():
    nick_name = ""
    username = "1962560722@qq.com"
    pwd = "vmhxkkjmurqkbhgh"
    receivers = "582021620@qq.com"

    # 1、构造纯文本邮件
    # 定义邮件内容
    text_info = "这是一个纯文本的测试邮件"
    # 定义邮件主题
    subject = "Python测试纯文本邮件主题"
    # 构造邮件对象
    msg = MIMEText(text_info,"plain","utf-8")
    # 汉字转base64
    fromname64 = base64.b64encode(bytes(nick_name,"utf-8"))
    # b'xxxx'转为'xxxx'
    fromname64_str = str(fromname64,"utf-8")
    # 尖括号拼接用双引号
    from_namestr = '"=?utf-8?B?' + fromname64_str + '=?=" <' + username + ">"
    # 构造头部信息
    # msg['From'] = Header(from_namestr)
    msg['From'] = Header(f"{nick_name} <{username}>")
    msg["To"] = Header("582021620@qq.com","utf-8")
    msg["Subject"] = Header(subject,"utf-8")

    try:
        smtp_obj = smtplib.SMTP_SSL("smtp.qq.com",465)
        smtp_obj.login(username,pwd)
        smtp_obj.sendmail(username,receivers,msg.as_string())
        print("邮件发送成功")
        smtp_obj.quit()
    except Exception as e:
        print("邮件发送失败" + str(e) )


if __name__ == '__main__':
    send_mail()
