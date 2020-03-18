from pyzbar import pyzbar
import argparse
import cv2
import os
import re
import glob
import tkinter
from tkinter import *
import smtplib
from prettytable import PrettyTable
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import csv
from tabulate import tabulate

path='barcodes/'
files=[]
for filename in glob.glob(os.path.join(path, '*.jpg')):  
    files.append(filename)
# print(files)

barCodes=[]
splStr='\\'
for f in files:
    res=f.partition(splStr)[2]
    # print(res)
    barCodes.append(res)
# print(barCodes)

items=[]

for barCode in barCodes:

    a=str('barcodes/'+barCode)

    image=cv2.imread(a)

    bars=pyzbar.decode(image)

    for bar in bars:
        (x,y,w,h)=bar.rect
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
        barcodeData=bar.data.decode("utf-8")
        barcodeType=bar.type

        text="{}({})".format(barcodeData,barcodeType)
        # print(text)
        splStr='('
        res=text.partition(splStr)[0]
        items.append(res)
        cv2.putText(image,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    
    cv2.waitKey(100)

fruitsAndVegetables=['Apple','Mango','Drumstick','Eggplant','Banana']
fluids=['Pepsi','Harpic']

itemScanned=[]
quantity=[]
price=[]
for i in items:
    temp=i.split('-',2)
    itemScanned.append(temp[0])
    quantity.append(temp[1])
    price.append(temp[2])

print(itemScanned)
print(quantity)
print(price)

# mainWindow=tkinter.Tk()

# mainWindow.geometry("500x500+300-100")

# mainWindow.title('ABC Mart')

# title=Label(mainWindow,text="BILL DETAILS", font=('comicsana',18)).place(x=170,y=10)

# slNo=1
# slNox=10
# slNoy=50
# itemNamex=70
# itemNamey=50
# quantityx=250
# quantityy=50
# pricex=350
# pricey=50
# discountx=420
# discounty=50

# title=Label(mainWindow,text="SL NO").place(x=slNox,y=slNoy)
# title=Label(mainWindow,text="ITEM").place(x=itemNamex,y=itemNamey)
# title=Label(mainWindow,text="QUANTITY").place(x=quantityx,y=quantityy)
# title=Label(mainWindow,text="PRICE").place(x=pricex,y=pricey)
# title=Label(mainWindow,text="DISCOUNT").place(x=discountx,y=discounty)

# slNoy += 20
# itemNamey += 20
# quantityy += 20
# pricey += 20
# discounty += 20

# finalBillItems=[]

# ptr=0

# totalPrice=0

# for i in itemScanned:
#     var=IntVar()
#     mainWindow.after(15, var.set, 1)
#     print("Scanned")
#     mainWindow.wait_variable(var)
#     title=Label(mainWindow,text=slNo).place(x=slNox,y=slNoy)
#     title=Label(mainWindow,text=i).place(x=itemNamex,y=itemNamey)
#     quant=quantity[ptr]
#     if(i in fruitsAndVegetables):
#         name=' Kgs'
#     elif(i in fluids):
#         name=' Lts'
#     else:
#         name=' Pkt'
#     title=Label(mainWindow,text=quantity[ptr]+name).place(x=quantityx,y=quantityy)
#     title=Label(mainWindow,text=price[ptr]+'/-').place(x=pricex,y=pricey)
#     title=Label(mainWindow,text="None").place(x=discountx,y=discounty)
#     totalPrice += int(price[ptr])
#     temp=[]
#     temp.append(slNo)
#     temp.append(i)
#     temp.append(quantity[ptr]+name)
#     temp.append(price[ptr]+'/-')
#     finalBillItems.append(temp)
#     ptr += 1
#     slNo += 1
#     slNoy += 20
#     itemNamey += 20
#     quantityy += 20
#     pricey += 20
#     discounty += 20

# var=IntVar()
# mainWindow.after(1500, var.set, 1)
# mainWindow.wait_variable(var)

# totalPriceLabel=Label(mainWindow,text="TOTAL PRICE : "+str(totalPrice)).place(x=itemNamex,y=discounty+20)

# billPrint = PrettyTable()
# billPrint.field_names = ["SL NO", "ITEM", "QUANTITY", "PRICE"]
# for bill in finalBillItems:
#     billPrint.add_row(bill)
# f=open("bill.pdf","w")
# f.write(str(billPrint))

# def buttonClick():
#     # s=smtplib.SMTP('smtp.gmail.com',587)
#     # s.starttls()
#     # s.login("svsumukh18@gmail.com", "sumukhkohli18")
#     # message="Dear Customer, Please find your bill attached with this email! Thank you for shopping!"
#     #########################################################
#     mail_content = '''Dear Customer,
#     Thanks for shopping in ABC Mart!
#     Please find your e-bill attached with this email.
#     Thank you!
#     '''
#     #The mail addresses and password
#     sender_address = 'svsumukh18@gmail.com'
#     sender_pass = 'sumukhkohli18'
#     receiver_address = 'sumukhmys1999@gmail.com'
#     #Setup the MIME
#     message = MIMEMultipart()
#     message['From'] = sender_address
#     message['To'] = receiver_address
#     message['Subject'] = 'ABC Mart E-Bill'
#     #The subject line
#     #The body and the attachments for the mail
#     message.attach(MIMEText(mail_content+'Total Price : Rs. '+str(totalPrice)+'/-', 'plain'))
#     attach_file_name = 'bill.pdf'
#     attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
#     payload = MIMEBase('application', 'octet-stream')
#     payload.set_payload((attach_file).read())
#     encoders.encode_base64(payload) #encode the attachment
#     #add payload header with filename
#     payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
#     message.attach(payload)
#     #Create SMTP session for sending the mail
#     session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
#     session.starttls() #enable security
#     session.login(sender_address, sender_pass) #login with mail_id and password
#     text = message.as_string()
#     session.sendmail(sender_address, receiver_address, text)
#     session.quit()
#     print('Mail Sent')
#     #########################################################
#     # s.sendmail("svsumukh18@gail.com", "sumukhmys1999@gmail.com", message)
#     # # s.sendmail("svsumukh18@gail.com", "anagha_mk@yahoo.com", message)
#     # print("Email Sent")
#     # s.quit() 
#     var=IntVar()
#     mainWindow.after(1500, var.set, 1)
#     mainWindow.wait_variable(var)
#     mainWindow.destroy()

# # button=tkinter.Button(mainWindow,text='PAY Rs. 500/-',width=30, command=mainWindow.destroy).place(x=135,y=450)
# button=tkinter.Button(mainWindow,text='PAY Rs. '+str(totalPrice),width=30, command=buttonClick).place(x=135,y=450)

# mainWindow.mainloop()


