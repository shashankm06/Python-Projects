
import smtplib
import ssl
from email.message import EmailMessage

EMAIL = "shashankmish96@gmail.com"
APP_PASSWORD = "XXXXXXXXXXX"
RECIEVER = "24tec2aids175@vgu.ac.in"

msg = EmailMessage()

msg["From"] = EMAIL
msg["To"] = RECIEVER
msg["Subject"] = "Hello From Python..."

msg.set_content("This email was sent through python")

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465, context=context)as server:
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)