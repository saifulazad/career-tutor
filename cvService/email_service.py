import email.utils
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SENDER = "admin@fractalslab.com"
SENDERNAME = "Saiful Azad"

USERNAME_SMTP = "AKIA5V5WGNMDD2ONQEJU"

PASSWORD_SMTP = "BKSSZPNJfms6cpJFOHrrWiBzuTSVJyYWxJIli30fRBL3"

HOST = "email-smtp.ap-southeast-1.amazonaws.com"
PORT = 587


def send_email(user_mail):
    RECIPIENT = user_mail
    SUBJECT = "Thanks for contact us."

    BODY_HTML = """
        <h3>Hi, Thanks for your comment. We will respond as soon as possible.</h3>
    """

    msg = MIMEMultipart("alternative")
    msg["Subject"] = SUBJECT
    msg["From"] = email.utils.formataddr((SENDERNAME, SENDER))
    msg["To"] = RECIPIENT

    part2 = MIMEText(BODY_HTML, "html")
    msg.attach(part2)
    try:
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(USERNAME_SMTP, PASSWORD_SMTP)
        server.sendmail(SENDER, RECIPIENT, msg.as_string())
        server.close()
    except Exception as e:
        print("Error: ", e)
    else:
        print("Email sent!")
