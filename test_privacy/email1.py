import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = "312296537@qq.com"
reciver = "312296537@qq.com"
port = 465
password = "qplgmmsisuxkcabc"
smtpserver = "smtp.qq.com"


subject = "主题"
body = "内容"

body1 = """
<p>这是内容</p>
<a href="https://www.baidu.com/">按钮</a>

"""

msg = MIMEText(body1, 'html', 'utf-8')
msg['from'] = "python"
msg['to'] = 'reciver'
msg['subject'] = subject

smtp = smtplib.SMTP_SSL(smtpserver,port)
smtp.login(sender,password)
for i in range(3):
    smtp.sendmail(sender,reciver,msg.as_string())
smtp.quit()