import csv
from tabulate import tabulate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

totalPrice='345'

me = 'svsumukh18@gmail.com'
password = 'sumukhkohli18'
server = 'smtp.gmail.com:587'
you = 'anagha_mk@yahoo.com'

text = """
Dear Customer,

Thank you for shopping with us!
Please find your E-Bill down below : 

{table}

Regards,
ABC Mart
"""

html = """
<html>

<head>
    <style> 
        table, th, td, tr {{ border: 1px solid red; border-collapse: collapse; }}
        th, td{{ border-left:1px solid red; border-right: 1px solid red;}}
    </style>
</head>

<body>
    <p>Dear Customer,</p>
    <p>Thank you for shopping with us! <br/>
       Please find your E-Bill down below : </p><br/>
    {table}
    <br/>
    <p>Total Price : Rs. %s /-</p><br/><br/>
    <p>Regards,</p><br/>
    <p>ABC Mart</p>
</body>

</html>
""" %totalPrice

data=[]

with open('input.csv') as f:
    # reader = csv.reader(input_file)
    # data = list(reader)
    data=[line.split() for line in f]
    # print(lis)

text = text.format(table=tabulate(data, headers="firstrow", tablefmt="grid"))
html = html.format(table=tabulate(data, headers="firstrow", tablefmt="html"))

message = MIMEMultipart(
    "alternative", None, [MIMEText(text), MIMEText(html,'html')])

message['Subject'] = "ABC Mart E-Bill"
message['From'] = me
message['To'] = you
server = smtplib.SMTP(server)
server.ehlo()
server.starttls()
server.login(me, password)
server.sendmail(me, you, message.as_string())
print('Email Sent')
server.quit()