import smtplib 
from email.message import EmailMessage

def sendEmail(From, to, subject, message, mailservice, password):
    email = EmailMessage() 
    email['from'] = From
    email['to'] = to 
    email['subject'] = subject
    email.set_content(message) 
    mail = 'smtp.' + mailservice
    with smtplib.SMTP(host=mail, port=587) as smtp: #host could be any email service and port = 587 is the standard for the smtp protocol
        smtp.ehlo() #this is part of the smpt standard, says hi to server essentially
        smtp.starttls() #ttls is the encrytion part, encrypts message
        smtp.login(From, password)#login of your email
        smtp.send_message(email) #email is the object we used created
        print('email sent!')

def main():
    print("Hello! Please follow the instructions to send an email using Python!\n")
    From = input("Please enter your email address: ")
    to = input("Please enter the email of the person who will receive the email: ")
    subject = input("Please enter subject of the email: ")
    message = input("Please enter the main message: ")
    mailservice = input("Please enter which email service you are using \n(ex: if you are using gmail use: gmail.com)\n ")
    password = input("Please enter the password of your email: ")

    sendEmail(From, to, subject, message, mailservice, password)
  

if __name__ == "__main__":
    main()
