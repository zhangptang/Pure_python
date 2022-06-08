# -*-coding:utf-8-*-
from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP


def main():
    sender = 'zptang_study@163.com'
    receivers = ['1004676372@qq.com']
    message = MIMEText('用python发送邮件实例', 'plain', 'utf8')
    message['From'] = Header('zptang', 'utf8')
    message['to'] = Header('大佬', 'utf8')
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    smpter = SMTP('smtp.163.com')
    smpter.login(sender, '***')
    smpter.sendmail(sender, receivers, message.as_string())
    print('send email end!')


if __name__ == '__main__':
    main()
