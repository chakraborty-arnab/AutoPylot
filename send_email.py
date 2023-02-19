import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up the email details
sender_email = 'your_email@example.com'
# Prerequisite: Setup an app password
sender_password = 'your_email_app_password'
recipient_email = 'recipient@example.com'
subject = 'Checkout my GitHub'
body = "I've just made some new commits in my github repos. Here's the link: https://github.com/chakraborty-arnab!"

# Create a MIME message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

# Connect to the SMTP server and send the email
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, message.as_string())

print('Email sent successfully!')