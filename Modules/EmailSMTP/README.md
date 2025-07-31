# Email SMTP: `smtplib`
- module that come pre bundled with Python, that helps us send emails using python code
- SMTP: Simple Mail Transfer Protocol
- allows you to connect to an SMTP server, authenticate if necessary, and send email messages
- Import smtplib and email.message
- Create an EmailMessage object: This object helps construct the email with headers (From, To, Subject) and content
- Establish an SMTP connection
- secure the connection (if using TLS)
- Log in to the SMTP server (if required)
- Send the email.


### Important Considerations:
- **SMTP Server Details:**
    - You need the correct SMTP server address, port, and authentication credentials (username and password) provided by your email service provider.
- **Security:**
    - Always use starttls() or connect to port 465 for SSL/TLS to encrypt your connection and protect your credentials.
- **Error Handling:**
    - Implement try-except blocks to handle potential smtplib.SMTPException errors during the process.
- **Debugging:**
    - The smtplib module can be set to a debug level to see the communication with the SMTP server for troubleshooting.

# Port
 - By default smtplib.SMTP uses port 25
    - used to be the standard SMTP port, but because of abuse in the past most servers nowadays have blocked this port to external traffic
    - there are still some that do allow it; Hotmail, Live, etc. 
- Port 25 is still used for traffic between servers, but many providers have switched to using port 587 for external traffic
- If in doubt, search the internet for "smtp server settings" for your provider
- if `smtplib.SMTP("smtp.gmail.com", port=587)` is not working
    - Add a port number by changing your code to this: `smtplib.SMTP("smtp.gmail.com", port=587)`




# error Connection unexpectedly closed
- might be due to a number of things
1. Make sure you've got the correct smtp address for your email provider:
    - **Gmail:** smtp.gmail.com
    - **Hotmail:** smtp.live.com
    - **Outlook:** outlook.office365.com
    - **Yahoo:** smtp.mail.yahoo.com
    - If you use another email provider, just Google for your email provider e.g. "Gmail SMTP address"

# How does Emails  work
### SMTP: Simple Mail Transfer Protocol
- contains all the rules that determine how an email is received by mail servers passed on the the next mail server and how it can be sent by the internet
- SMTP is the mailman for emails

