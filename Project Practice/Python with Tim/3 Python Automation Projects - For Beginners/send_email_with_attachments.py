import smtplib, ssl, email, os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "seletestpy@gmail.com"
receiver_email = ['seletestpy@gmail.com', 'flaviolj@comcast.net', 'flfmsqa@gmail.com']
# receiver_email = 'flaviolj@comcast.net'
password = "fdsaqwer"

#Create MIMEMultipart object
msg = MIMEMultipart("alternative")
msg["Subject"] = "multipart test"
msg["From"] = sender_email
msg["To"] = ','.join(receiver_email)
filename = "document.pdf"

#HTML Message Part
html = """
<html>
    <body>
        <h1>From: {sender_email}</h1>
        <p>To: {receiver_email}</p
    </body>
</html>
"""

part = MIMEText(html, "html")
msg.attach(part)

print(os.getcwd())
newDir = "/Users/flaviolago/Documents/Education/Liping/Python/Projects/Project Practice/Python with Tim/3 Python Automation Projects - For Beginners/"
os.chdir(newDir)
print(os.getcwd())

# Add Attachment
with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
   
encoders.encode_base64(part)

# Set mail headers
part.add_header(
    "Content-Disposition",
    "attachment", filename= filename
)
msg.attach(part)

# Create secure SMTP connection and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, msg.as_string()
    )

print("Email sent!")