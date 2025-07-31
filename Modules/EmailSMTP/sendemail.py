import smtplib

from pyexpat.errors import messages

# identity of your email account: tralainereed
# identity of email provider: gmail.com
my_email = "youremail@email.com"
password = "yourapppassword"
PORT = 123456

#TODO-1: Create Connection
# Make sure you've got the correct smtp address for your email provider
connection = smtplib.SMTP("smtpaddress.com", port=PORT)# smtp address: location of email providers SMTP server

#TLS: Transport Layer Security
# way of securing the connection to email server
# if we are sending a email and someone intercepts the email
# the email will be encrypted and they wont be able to read it
# TODO-2: Secure Connection
connection.starttls()

# TODO-3: Log into email account
connection.login(user=my_email, password=password)

# TODO-4: Send Email
connection.sendmail(from_addr=my_email, to_addrs="sendtoemail@email.com", msg="Hello from Python")

# TODO-5: Close connection
connection.close()
