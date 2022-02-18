# Youtube video link: https://www.youtube.com/watch?v=Oz3W-LKfafE
# Using python Send email from gmail account to other emails acount 

from cgitb import html
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

# HTML code with CSS Animation Effects
html = """
<html lang="en">
<head>
	<meta charset="UTF-8">
    <title>CSS Animation Effects</title>
    <!-- <link rel="stylesheet" type="text/css" href="style.css"> -->
    <style>
        *
        {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        }
        body
        {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background: #111;
        }
        .container
        {
            position: relative;
            width: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .container .ring
        {
            position: relative;
            width: 150px;
            height: 150px;
            margin: -30px;
            border-radius: 50%;
            border: 4px solid transparent;
            border-top: 4px solid #24ecff;
            animation: animate 4s linear infinite;
        }
        @keyframes animate
        {
            0%
            {
                transform: rotate(0deg);
            }
            100%
            {
                transform: rotate(360deg);
            }
        }
        .container .ring::before
        {
            content: '';
            position: absolute;
            top: 12px;
            right: 12px;
            border-radius: 50%;
            width: 15px;
            height: 15px;
            background: #24ecff;
            box-shadow: 0 0 0 5px #24ecff33, 
            0 0 0 10px #24ecff22,
            0 0 0 20px #24ecff11,
            0 0 20px #24ecff,
            0 0 50px #24ecff;
        }

        .container .ring:nth-child(2)
        {
            animation: animate2 4s linear infinite;
            animation-delay: -1s;
            border-top: 4px solid transparent;
            border-left: 4px solid #93ff2d;
        }

        .container .ring:nth-child(2)::before
        {
            content: '';
            position: absolute;
            top: initial;
            bottom: 12px;
            left: 12px;
            border-radius: 50%;
            width: 15px;
            height: 15px;
            background: #93ff2d;
            box-shadow: 0 0 0 5px #93ff2d33, 
            0 0 0 10px #93ff2d22,
            0 0 0 20px #93ff2d11,
            0 0 20px #93ff2d,
            0 0 50px #93ff2d;
        }

        @keyframes animate2
        {
            0%
            {
                transform: rotate(360deg);
            }
            100%
            {
                transform: rotate(0deg);
            }
        }

        .container .ring:nth-child(3)
        {
            animation: animate2 4s linear infinite;
            animation-delay: -3s;
            position: absolute;
            top: -66.66px;
            border-top: 4px solid transparent;
            border-left: 4px solid #e41cf8;
        }

        .container .ring:nth-child(3)::before
        {
            content: '';
            position: absolute;
            top: initial;
            bottom: 12px;
            left: 12px;
            border-radius: 50%;
            width: 15px;
            height: 15px;
            background: #e41cf8;
            box-shadow: 0 0 0 5px #e41cf833, 
            0 0 0 10px #e41cf822,
            0 0 0 20px #e41cf811,
            0 0 20px #e41cf8,
            0 0 50px #e41cf8;
        }

        .container p
        {
            position: absolute;
            color: #fff;
            font-size: 1.5em;
            font-family: consolas;
            bottom: -80px;
            letter-spacing: 0.15em;
        }
    </style>
</head>
<body>
	<div class="container">
    	<div class="ring"></div>
        <div class="ring"></div>
        <div class="ring"></div>
        <p>Loading...</p>
    </div>
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
