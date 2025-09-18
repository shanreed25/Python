# Flask [WTF](https://wtforms.readthedocs.io/en/3.0.x/)
- build forms using a Flask extension called Flask-WTF
- Flask developers will usually choose Flask-WTF to create forms in their websites
- you might also see projects that are built with HTML Forms. So it's important to understand how both of them work

### Benefits Over HTML Forms
#### Easy Form [Validation](https://wtforms.readthedocs.io/en/3.0.x/crash_course/#validators)
- Makes sure the user is entering data in the required format in all the required fields
  - like checking that the user's email entry has a "@" and a "." at the end, or make sure that passwords are minimum of 8 characters
  - Instead of us having to write our own validation code we can use all these validation rules straight out of the box from WTForms
- All without having to write your own validation code

#### Less Code 
- If you have a number of forms in your website, using WTForm can dramatically reduce the amount of code you have to write (or copy & paste).

#### Built in CSRF Protection 
- CSRF stands for Cross Site Request Forgery, it's an attack that can be made on website forms which forces your users to do unintended actions 
  - (e.g. transfer money to a stranger) or compromise your website's security if it's an admin


## Build a website that holds some secrets
- only with the right username and password can you access the page with our secrets

- [Quick Start docs](https://flask-wtf.readthedocs.io/en/1.0.x/quickstart/)
- [Basic Fields](https://wtforms.readthedocs.io/en/3.0.x/fields/#basic-fields)
- [Validation](https://wtforms.readthedocs.io/en/3.0.x/crash_course/#validators)

