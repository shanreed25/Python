# Jinja
- a fast, expressive, and extensible templating engine commonly used in Python web development, particularly with frameworks like Flask
- allows for the creation of dynamic documents (like HTML pages, configuration files, or even LaTeX documents) by combining static text with dynamic content
- separates the presentation logic from the application logic, allowing developers to create clean and maintainable templates for generating various types of dynamic content

# How Jinja templates work
### Placeholders and Logic
**Jinja templates are text files that contain special placeholders and control structures. These are typically enclosed in specific delimiters**
- 
- **{{ ... }}** for expressions (variables or calculations that output a value)
    - `<h1>{{5 * 6}}</h1>` will render 30
- **{% ... %}** for control structures like conditionals (if/else) and loops (for)
- **{# ... #}** for comments


### Data Injection
- if the template is designed to be rendered with data, often provided as a dictionary or other data structure
- when the template is processed, the placeholders are replaced with the corresponding values from the provided data


- [Templates](./Templates.md)