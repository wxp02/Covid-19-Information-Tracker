from email.mime.text import MIMEText
import smtplib

def send_email(email):
    from_email="realwxp02@gmail.com"
    from_password="wenxupoh6902"
    to_email=email

    subject="Thank you for registering"
    message="Hi, thank you for registering. We will send you an email if there is a confirmed Covid-19 near our premises."
    msg=MIMEText(message, "html")
    msg["Subject"]=subject
    msg["To"]=to_email
    msg["From"]=from_email

    gmail=smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)