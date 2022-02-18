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
<!DOCTYPE html>
<html>
<head>
    <title>Calculator</title>
    <style>
        *
{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: consolas;
}
body
{
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background: #333;
}
.container
{
    position: relative;
    min-width: 300px;
    min-height: 400px;
    background: #333;
    padding: 40px 30px 30px;
    border-radius: 20px;
    box-shadow: 25px 25px 75px rgba(0,0,0,0.25),
    10px 10px 70px rgba(0,0,0,0.25),
    inset -5px -5px 15px rgba(0,0,0,0.5),
    inset 5px 5px 15px rgba(0,0,0,0.5);
}
.calculator
{
    position: relative;
    display: grid;
}

.calculator .value
{
    position: relative;
    grid-column: span 4;
    height: 100px;
    left: 10px;
    width: calc(100% - 20px);
    border: none;
    outline: none;
    background: #a7af7c;
    margin-bottom: 10px;
    border-radius: 10px;
    box-shadow: 0 0 0 2px rgba(0,0,0,0.75);
    text-align: right;
    padding: 10px;
    font-size: 2em;

}




.calculator span
{
    position: relative;
    display: grid;
    place-items: center;
    width: 80px;
    height: 80px;
    margin: 8px;
    background: linear-gradient(180deg, #2f2f2f, #3f3f3f);
    box-shadow: inset -8px 0 8px rgba(0,0,0,0.15),
    inset 0 -8px 8px rgba(0,0,0,0.25),
    0 0 0 2px rgba(0,0,0,0.75),
    10px 20px 25px rgba(0,0,0,0.4);
    color: #fff;
    user-select: none;
    cursor: pointer;
    font-weight: 400;
    border-radius: 10px;
}
.calculator span::before
{
    content: '';
    position: absolute;
    top: 3px;
    left: 4px;
    bottom: 14px;
    right: 12px;
    background: linear-gradient(90deg, #2d2d2d, #4d4d4d);
    border-radius: 10px;
    box-shadow: -5px -5px 15px rgba(0,0,0,0.1),
    10px 5px 10px rgba(0,0,0,0.15);
    border-left: 1px solid #0004;
    border-bottom: 1px solid #0004;
    border-top: 1px solid #0009;
}

.calculator span:active
{
    filter: brightness(1.5);
}

.calculator span i
{
    position: relative;
    font-style: normal;
    font-size: 1.5em;
    text-transform: uppercase;
}
.calculator .clear
{
    grid-column: span 2;
    width: 180px;
    background: #f00;
}
.calculator .clear::before
{
    background: linear-gradient(90deg, #d20000, #ffffff5c);
    border-left: 1px solid #fff4;
    border-bottom: 1px solid #fff4;
    border-top: 1px solid #fff4;
}
.calculator .plus
{
    grid-row: span 2;
    height: 180px;
}
.calculator .equal
{
    background: #2196f3;
}
.calculator .equal::before
{
    background: linear-gradient(90deg, #1479c9, #ffffff5c);
    border-left: 1px solid #fff4;
    border-bottom: 1px solid #fff4;
    border-top: 1px solid #fff4;
}
    </style>
    
</head>
<body>
	<div class="container">
    	<form class="calculator" name="calc">
            <input type="text" class="value" readonly name="txt">
            <span class="num clear" onclick="calc.txt.value=
            ''"><i>C</i></span>
            <span class="num" onclick="calc.txt.value+=
            '/'"><i>/</i></span>
            <span class="num" onclick="calc.txt.value+=
            '*'"><i>*</i></span>
            <span class="num" onclick="calc.txt.value+=
            '7'"><i>7</i></span>
            <span class="num" onclick="calc.txt.value+=
            '8'"><i>8</i></span>
            <span class="num" onclick="calc.txt.value+=
            '9'"><i>9</i></span>
            <span class="num" onclick="calc.txt.value+=
            '-'"><i>-</i></span>
            <span class="num" onclick="calc.txt.value+=
            '4'"><i>4</i></span>
            <span class="num" onclick="calc.txt.value+=
            '5'"><i>5</i></span>
            <span class="num" onclick="calc.txt.value+=
            '6'"><i>6</i></span>
            <span class="num plus" onclick="calc.txt.value+=
            '+'"><i>+</i></span>
            <span class="num" onclick="calc.txt.value+=
            '1'"><i>1</i></span>
            <span class="num" onclick="calc.txt.value+=
            '2'"><i>2</i></span>
            <span class="num" onclick="calc.txt.value+=
            '3'"><i>3</i></span>
            <span class="num" onclick="calc.txt.value+=
            '0'"><i>0</i></span>     
            <span class="num" onclick="calc.txt.value+=
            '00'"><i>00</i></span>
            <span class="num" onclick="calc.txt.value+=
            '.'"><i>.</i></span>
            <span class="num equal" onclick="document.calc.txt.
            value=eval(calc.txt.value)"><i>=</i></span>
        </form>   
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
