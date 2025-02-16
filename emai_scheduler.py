_author_ = 'Katyayani'
_credits_ = 'Katyayani'
_email_ = 'bpyadav0510@gmail.com'

import smtplib
import datetime as dt
import time
import getpass
import warnings
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Suppress warnings
warnings.filterwarnings("ignore")

# Input email credentials and message details
sender_email = input("Enter sender's email address: ")
receiver_email = input("Enter receiver's email address: ")
password = getpass.getpass("Enter your email app password: ")  # Use App Password here
port = 587
smtp_server = "smtp.gmail.com"

# Compose the email
subject = input("Enter the subject: ")
body = input("Enter the message body: ")
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Input the scheduled time
schedule_time = input('Enter the scheduled time (YYYY-MM-DD HH:MM:SS): ')
send_time = dt.datetime.strptime(schedule_time, '%Y-%m-%d %H:%M:%S')

# Wait until the scheduled time
current_time = dt.datetime.now()
time_to_wait = (send_time - current_time).total_seconds()

if time_to_wait > 0:
    print(f"Waiting for {time_to_wait} seconds to send the email...")
    time.sleep(time_to_wait)
else:
    print("Scheduled time is in the past. Please enter a future time.")
    exit()

# Send the email
try:
    with smtplib.SMTP(smtp_server, port) as email:
        email.starttls()
        email.login(sender_email, password)
        email.sendmail(sender_email, receiver_email, msg.as_string())
        print('Email sent successfully!')
except smtplib.SMTPAuthenticationError:
    print("Authentication failed. Please check your email address and App Password.")
except Exception as e:
    print(f"An error occurred: {e}")
