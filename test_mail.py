import smtplib
import ssl

port = 587
server = "smtp.gmail.com"
senders_mail = "darsh.sharm0811@gmail.com"
senders_pass = "reoiyvhwtsawtsxi"
reciver_mail = [{"name": "Rahul", "email": "rahul.brudite@gmail.com"}, {"name": "Mantu", "email": "mantu.r.brudite@gmail.com"}, {"name": "Prakhar", "email":"prakhar.k.brudite@gmail.com"}]

message = "Hello Folks"

# context = ssl.create_default_context()

for reciver in reciver_mail:
    message = f"Hello {reciver.get("name")}"

    with smtplib.SMTP("smtp.gmail.com", 587) as smtpMail:
        smtpMail.starttls()
        smtpMail.login(senders_mail, senders_pass)
        smtpMail.sendmail(senders_mail, reciver.get("email"), message)
        print(f"message send to {reciver.get("name")}")

print("Hello")