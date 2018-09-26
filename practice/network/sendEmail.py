import smtplib
from email.mime.text import MIMEText
from email.header import Header

from boto import exception


def send_text():
    #第三方SMTP服务，即使用别人的服务器将文件发送出去
    mail_host = 'smtp.163.com'
    mail_user = '*******' #邮箱
    mail_pass = '授权码'

    sender = '******' #发送人
    receiver = '******' #接收人邮箱

    message = MIMEText('使用python发送邮件。。。', 'plain', 'utf-8') #邮件内容
    message['From'] = '************'#发送人的邮箱
    message['To'] = '************'#收件人的邮箱

    subject = 'python邮件测试' #邮件标题
    message['Subject'] = Header(subject, 'utf-8')

    try:
        # smtObj = smtplib.SMTP_SSL(mail_host, 465) #创建服务对象
        smtObj = smtplib.SMTP()
        smtObj.connect(mail_host, 25) #链接
        smtObj.login(mail_user, mail_pass) #登陆
        smtObj.sendmail(sender, receiver, message.as_string())
        print('send succeed')
    except smtplib.SMTPException as e:
        print('send fail', str(e))

send_text()