import smtplib

from pyexpat.errors import messages

# identity of your email account: youremail
# identity of email provider: email.com
my_email = "youremail@email.com"
password = "yourapppassword"
PORT = 123456

# CREATING A CONNECTION*****************************************************************************************************************
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
# with subject and body: \n\n is used to separate subject from body
connection.sendmail(from_addr=my_email, 
                    to_addrs="sendtoemail@email.com", 
                    msg="Subject:Hello From Python\n\nThis is how python sends emails with SMTP")
# # with email body only
# connection.sendmail(from_addr=my_email, to_addrs="sendtoemail@email.com", msg="Hello from Python")



# TODO-5: Close connection
connection.close()


# CREATING A CONNECTION: with `with`(automatic closing)****************************************************************************************
#TODO-1: Create Connection
# Make sure you've got the correct smtp address for your email provider
with smtplib.SMTP("smtpaddress.com", port=PORT)as connection:
    # TODO-2: Secure Connection
    connection.starttls()

    # TODO-3: Log into email account
    connection.login(user=my_email, password=password)

    # TODO-4: Send Email
    connection.sendmail(from_addr=my_email, 
                    to_addrs="sendtoemail@email.com", 
                    msg="Subject:Hello From Python\n\nThis is how python sends emails with SMTP")
