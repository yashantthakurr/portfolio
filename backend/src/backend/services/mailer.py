
from backend.constants.config import secrets
from email.message import EmailMessage
import smtplib

sender_email = "yashant.thakur2007@gmail.com"

def send_emails(receiver_email: str, receiver_subject: str, receiver_content: str, admin_subject: str, admin_content: str) -> None:

    msg1 = EmailMessage()
    msg1["From"] = sender_email
    msg1["To"] = sender_email
    msg1["Subject"] = admin_subject
    msg1.set_content(admin_content)

    msg2 = EmailMessage()
    msg2["From"] = sender_email
    msg2["To"] = receiver_email
    msg2["Subject"] = receiver_subject
    msg2.set_content(receiver_content)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, secrets.EMAIL_SENDER_PASSWORD)
        server.send_message(msg1)
        server.send_message(msg2)

    print(f"Mails sent successfully to both {sender_email} and {receiver_email}")
