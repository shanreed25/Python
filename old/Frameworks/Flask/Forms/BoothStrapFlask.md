# Using Bootstrap-Flask as an Inherited Template
- has one of the most convenient methods for generating forms with WTForms
- in 1 line of code, you can create your form, replace the form with
    - `{‌{ render_form(form) }}`
    - this will generate all the labels, inputs, buttons, styling for your form just by taking the WTForm object that was passed to the template (form)


1. Install Bootstrap-Flask to your project using pip:
    - `pip install bootstrap-flask`
2. Import and initialise bootstrap-flask into server
    - `from flask_bootstrap import Bootstrap5`
    - `bootstrap = Bootstrap5(app)`
3. Add a line to import the render_form() function from bootstrap-flask
    - `{% from 'bootstrap5/form.html' import render_form %}`
4. Use the render_form() to generate your form
    - `{‌{ render_form(form) }}`

# Why Learn WTFform from scratch
- everything is dandy as long as it works
- This render_form macro is a black box. It's magic. Which is great, but what happens if your form breaks? What if it's not doing what you expect it to? How would you debug magic?
- That's why it's so important to understand how things work under the hood
- Once you understand it, you can take all the shortcuts