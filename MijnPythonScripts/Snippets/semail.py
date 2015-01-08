import smtplib
from email.mime.text import MIMEText
def send_email(message,subject,toaddrs):
    fromaddr = 'enter your email address'
    username = 'enter your username'
    password = 'enter your password'
    msg = MIMEText(message, 'html')
    msg['Subject']  = subject
    msg['From']=fromaddr
    msg['Reply-to'] = 'no-reply'
    msg['To'] = toaddrs
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, [toaddrs], msg.as_string())
    server.quit()
subject = input("Enter your subject?\n")
message = input("Enter your mesage?\n")
toaddrs = input("Enter receiver email address?\n")
send_email(str(message),str(subject),str(toaddrs))
