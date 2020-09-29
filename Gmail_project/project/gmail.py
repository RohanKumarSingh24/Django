import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
import os



fromaddr='rohan24malhotra@gmail.com'
toaddr='singh.rohan72@gmail.com'
msg=MIMEMultipart()

msg['From']=fromaddr

msg['To']=toaddr

msg['Subject']='Urgent_Work'

body="body of the email"

msg.attach(MIMEText(body,'plain'))

filename='t.pdf'


#file_path = Path("C:/Users/Rohan Singh/Desktop/")

attachment=open('/mnt/c/users/rohan singh/desktop/t.pdf','rb')

p=MIMEBase('application','octet-stream')

p.set_payload((attachment).read())

encoders.encode_base64(p)

p.add_header('Content-Disposition',"attachment; filename=%s" % filename)

msg.attach(p)

s=smtplib.SMTP('smtp.gmail.com',587)

s.starttls()
s.login(fromaddr,'XXXX')
text=msg.as_string()
s.sendmail(fromaddr,toaddr,text)
s.quit()