# Flask: Forms
**Using forms in Flask applications typically involves handling user input from HTML forms. This can be done directly with Flask's request object or, more commonly and robustly, by using the Flask-WTF extension which integrates WTForms**

### Ways to handle Forms with Flask
1. Basic Form Handling with request.form:
- HTML Form: Create an HTML form with method="POST" and action pointing to your Flask route. Include input fields with name attributes.
- Flask Route: In your Flask application, define a route that accepts both GET (for displaying the form) and POST (for handling submission) methods
- Accessing Data: Use request.form.get('field_name') to retrieve data from the submitted form. It's recommended to use .get() to avoid KeyError if a field is missing
- Learn More [here](./HTMLFORMS.md)

2. Advanced Form Handling with Flask-WTF:
**Flask-WTF simplifies form creation, validation, and rendering.**
- Installation: Install Flask-WTF and Flask:
- Form Class: Define your form fields and validators in a Python class that inherits from FlaskForm.
- Flask Route.
- HTML Template: Render the form using Jinja2.
- Validation:
form.validate_on_submit() automatically runs validators defined in your form class. If validation fails, form.errors will contain error messages.
- CSRF Protection:
Flask-WTF automatically handles CSRF protection, requiring app.config['SECRET_KEY'] and {{ form.csrf_token }} in your template.
- Learn More [here](./FlaskWTF.md)