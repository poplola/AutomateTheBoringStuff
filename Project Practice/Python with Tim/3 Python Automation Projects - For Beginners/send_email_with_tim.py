# Youtube video link: https://www.youtube.com/watch?v=Oz3W-LKfafE
# Using python Send email from gmail account to other email accounts 

# from cgitb import html
import smtplib
import ssl
from email.message import EmailMessage

subject = "Test Email From Lisa"
body = "From Lisa - This is a test email from Python!"
sender_email = "seletestpy@gmail.com"
# receiver_email = 'seletestpy@gmail.com,flaviolj@comcast.net,flfmsqa@gmail.com'
receiver_email = ['seletestpy@gmail.com', 'flaviolj@comcast.net', 'flfmsqa@gmail.com']
# password = input("enter a password: ")
password = "fdsaqwer"

message = EmailMessage()

message["From"] = sender_email
# message["To"] = receiver_email
message["To"] = ','.join(receiver_email)

print(type(','.join(receiver_email)))
print(type('seletestpy@gmail.com,flaviolj@comcast.net,flfmsqa@gmail.com'))

message["Subject"] = subject
# message.set_content(body)
print(message)
html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p
    </body>
</html>
"""

message.add_alternative(html, subtype="html")

context = ssl.create_default_context()

print("Sending Email ...")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email sent!")
