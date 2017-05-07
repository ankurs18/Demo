import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
 
fromaddr = "ankursethi1994@gmail.com"
toaddr = "ankursethi1994@g.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Sent By Python"
 
body = "YOUR MESSAGE HERE"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "wuwjuomsxtiybvbe")
text = msg.as_string()

result=server.sendmail(fromaddr, toaddr, text)

if len(result) == 0:
    print('Success')
else:
    print(result)  
      
server.quit()