




### {% include %} tag
- template tag used to insert the content of one template file directly into another
- `{% include "header.html" %}` will insert the entire content of the header.html file at the location where the {% include %} tag is placed in the current template
- can also pass variables to the included template using the `with` keyword