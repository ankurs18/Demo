import smtplib

sender = 'ankursethi1994@gmail.com'

receivers = ['user@locahost.com', 'ankursethi1994@gmail.com']

msg=""" dsds
sasa
sasssss
"""

try:
    smtpobj=smtplib.SMTP('smtp.gmail.com', 587) #smtp.gmail.com
    smtpobj.sendmail(sender, receivers, msg)
    print('Email Sent')
    
except Exception:
    print('Error')    