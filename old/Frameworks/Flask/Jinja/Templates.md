
### [Include statement: {% include fileName %} tag](./Include.md)
- template tag used to insert the content of one template file directly into another



## Template Inheritance
- a powerful feature that promotes code reusability and maintainability in web development
- allows developers to create a base "skeleton" template that contains common elements of a website, such as headers, footers, navigation bars, and overall page structure
- templates then extend this base template and override or add content to specific sections
- Benefits of Template Inheritance include, Code Reusability, Maintainability, Organization and Flexibility

### Base Template
- defines the common layout and structure of your web pages
- includes `{% block %}` tags, which act as placeholders for content that child templates can fill in
### Child Templates
- inherit from a base template using the `{% extends %}` tag at the beginning of the file
- then they define their specific content within `{% block %}` tags that correspond to the blocks defined in the base template

### {% block %} Tag
- defines a named section in a template that can be overridden by a child template
### {% extends %} Tag
- specifies which base template a child template should inherit from

Example: `base.html`
```
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{% block title %}{% endblock %}</title>
    </head>
    <body>
        {% block content %}{% endblock %}
    </body>
    </html>
```
- has predefined areas (or blocks) where new content can be inserted by a child webpage inheriting from this template

Example: `success.html`
```
{% extends "base.html" %} 
{% block title %}Success{% endblock %}
{% block content %}
   <div class="container">
      <h1>Top Secret </h1>
      <iframe src="https://giphy.com/embed/Ju7l5y9osyymQ" width="480" height="360" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
      <p><a href="https://giphy.com/gifs/rick-astley-Ju7l5y9osyymQ">via GIPHY</a></p>
   </div>
{% endblock %}
```
- `{% extends "base.html" %}`: tells the templating engine (Jinja) to use "base.html" as the template for this page
- `{% block title %}Success{% endblock %}`: inserts a custom title into the header of the template
    - title is the name of the block but you can name it what you want
- `{% block content %}.....{% endblock %}`: provides the content of the website. The part that is going to vary between webpages
**When we are inheriting templates. Sometimes, there's some part of the template that we want to keep, but we also want to add to it. So we can use super blocks in this case**

## Super Blocks
- when we inherit from Python classes, you often see super.init()
- the super keyword refers to the parent that the child is inheriting from. e.g If Simba inherits from Mufasa, then Mufasa is the super
- add a super block using `{‌{ super() }}`
Example: Parent Page
```
    <style>
        {% block styling %}
        body{
            background: purple;
        }
        {% endblock %}
    </style>
```
Example: Child Page
```
{% block styling %}
   {{ super() }}
   h1 {
      color:red;
   }
{% endblock %}
```
- will inject all the code in the styling block to this child page
- afterwards before the `{% endblock %}`, we can add some more styling to change the colour of the 