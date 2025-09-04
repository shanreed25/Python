# Include statement: {% include filePath %}
- the content of the included template is inserted directly into the current template at the point of the include statement
- template tag used to insert the content of one template file directly into another
- `{% include "header.html" %}` will insert the entire content of the header.html file at the location where the {% include %} tag is placed in the current template
- can also pass variables to the included template using the `with` keyword
- injecting a header.html and footer.html code might look something like this
    ```
    {% include "header.html" %}
    Web page content
    {% include "footer.html" %}
    ```
- primary purpose is to avoid duplicating common elements, such as headers, footers, navigation bars, or sidebars, across multiple web pages. Instead, these elements are defined once in a separate file

### blocks
- when the included template is rendered, it has its own scope, and its blocks are not exposed for overriding by the including template's inheritance chain
- blocks defined within a template that is included using the {% include %} tag cannot be directly overridden by the template that performs the inclusion, or by any template that extends the including template
Example: `base.html`
```
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{% block title %}My Title that cannot be overwritten{% endblock %}</title>
    </head>
    <body>
        {% block content %}
        <p>This Content cannot be overwritten</p>
        {% endblock %}
    </body>
    </html>
```
### Workarounds
**While direct overriding is not possible, workarounds exist to achieve similar effects**
#### Pass Variables 
- you can pass variables to the included template using the with context or by explicitly providing variables to the include tag
- the included template can then use these variables to conditionally render content within its blocks
- an included template automatically inherits the rendering context of the parent template. This means that all variables defined in the parent template are directly accessible within the included template without explicit passing
- Example: 
    - defines a variable `header` that will be passed to templateB, since the header is set in templateA it cannot be overwritten in templateB
        - this automatic inheritance simplifies variable management when using includes, as you do not need to repeatedly pass variables that are already available in the parent scope
    - the `lang_name` variable is set in tmeplateB
    
        ```
            {% set header = "My Header" %}
            <h1>{{header}}</h1>
            <h2>{{lang_name}}</h2>
        ```

    - templateB includes templateA, and sets the variable `lang_name` that is passed to templateA
    - this way the `lang_name` variable can be passed and changed along with templateA
        ```
            {% set header = "My New Header" %} #this will not work
            {% set lang_name = "CSS" %}
            {% include "templateA.html" %}
        ```
- simplifies dynamic variable management when using includes, as you can change the variable value as needed



Define Blocks in the Main Template:
.
Instead of defining blocks in the included template, define them in the main template (or a base template that the main template extends). The included template can then simply render content into these blocks using {{ super() }} or by directly outputting content, if the block is not intended to be overridden by a child of the main template.
Macros:
.
For reusable components with varying content, Jinja macros can be a more suitable alternative to includes with blocks, as they allow for passing arguments and dynamic content generation


**If you actually want to use the same design template for your entire website, but you might need to change some code in your header or footer. In these cases, it's better to use Template Inheritance instead**