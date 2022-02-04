from ast import Pass
import smtplib
from email.message import EmailMessage
import xlrd
from dotenv import dotenv_values
config = dotenv_values(".env")
EMAIL_ADDRESS = config['EMAIL']
EMAIL_PASSWORD = config['PASSWORD']

wb = xlrd.open_workbook("./sheet.xlsx")
sheet = wb.sheet_by_index(0)

with open("./chetna.html", "r", encoding="utf-8") as f:
    body = f.read()

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    for i in range(sheet.nrows):
        msg = EmailMessage()
        reciever = sheet.cell_value(i, 0)
        msg['Subject'] = "Invitation to Anubhuti '22"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = reciever
        msg.set_content('This is a plain text email')
        msg.add_alternative(body, subtype='html')
        smtp.send_message(msg)
        print("Mail sent to " + reciever)
