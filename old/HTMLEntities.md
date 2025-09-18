# Unescape HTML Entities
**To unescape HTML entities in Python, the recommended method is to use the html.unescape() function from the built-in html module**
- converts named and numeric character references (e.g., &lt;, &#62;, &#x3e;) in a string to their corresponding Unicode characters
- `import html`
- `html.unescape(escaped_string)` takes the string containing HTML entities as an argument and returns a new string with the entities replaced by their original characters

```

import html

# String with HTML entities
escaped_string = "In &quot;Resident Evil&quot;, only Chris has access to the grenade launcher"

# Unescape the HTML entities
unescaped_string = html.unescape(escaped_string)

print(unescaped_string)


```