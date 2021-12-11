import smtplib
import pandas
import datetime as dt
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

Username = ''
Password = 'olcygsskagjmwzev'

from_email = 'abc@xyz.com'

data = pandas.read_csv('client_info.csv')
emails = data['Email ID'].tolist()

# with open('body.txt') as body:
#     message = body.read()

msg = MIMEMultipart('alternative')
msg['From'] = formataddr(('EPCORN ', from_email))
msg['To'] = 'exteam.epcorn@gmail.com'
msg['Subject'] = 'EPCORN Newsletter'
# msg.attach(MIMEText(message))


    
with smtplib.SMTP('smtp.mail.yahoo.com', 587) as connection:
    connection.starttls()
    connection.login(user=Username, password=Password)
    for(index, row) in data.iterrows():

        with open('body.txt') as body:
            message = body.read()
            new_message = message.replace('[name]', row['Name'])
        
        msg.attach(MIMEText(new_message))
        
        connection.sendmail(from_email, row['Email ID'],  msg.as_string())
    print('emails sent successfully')


# now = dt.datetime.now()
# current_month = now.month
# current_day = now.day







