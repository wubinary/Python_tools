from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys
 
sender = 'wubinray@gmail.com'
passwd = '0918086428'
receivers = ['wubinray@gmail.com','wubinray.eed04@g2.nctu.edu.tw','f9g8h7j654@gmail.com']
 
emails = [elem.strip().split(',') for elem in receivers]
msg = MIMEMultipart()
msg['Subject'] = "廢物"
msg['From'] = sender
msg['To'] = ','.join(receivers)
 
msg.preamble = 'Multipart massage.\n'
mail_msg="許軒偉廢物"
part = MIMEText(mail_msg)
msg.attach(part)

attachname = "smtp.txt"
part = MIMEApplication(open(str(attachname),"rb").read())
'''
if len(sys.argv) > 2:
    attachname = str(sys.argv[2])
else:
    attachname = str(sys.argv[1])
'''
 
part.add_header('Content-Disposition', 'attachment', filename=attachname)
msg.attach(part)
 
smtp = smtplib.SMTP("smtp.gmail.com:587")
smtp.ehlo()
smtp.starttls()
smtp.login(sender, passwd)
 
smtp.sendmail(msg['From'], emails , msg.as_string())
print( 'Send mails to',msg['To'])
