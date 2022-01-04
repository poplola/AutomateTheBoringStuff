#!/usr/bin/env python3

import smtplib
import os
import config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

raport_file = open('test.html','rb')
alert_msg = MIMEText(raport_file.read(),"html", "utf-8")

# me == my email address
# you == recipient's email address
me = "seletestpy@gmail.com"
you = "flavilj@comcast.net"
subject = 'html email Test'

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = subject
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
html = """\

"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(config.EMAIL_ADDRESS, config.PASSWORD)

server.sendmail(me,you,alert_msg.as_string())
server.quit()
