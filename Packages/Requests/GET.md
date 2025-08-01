# `get()`
- makes a GET request
- call the `requests.get()` method, passing the target URL as an argument
- returns a Response object
- when calling `requests.get()` you can also include optional parameters such as
    - params for query strings
    - headers for custom HTTP headers
    - timeout for request timeouts
- See an example [here](../../CheatSheets/Packages/request.py)

### Access response data
- the response object contains various attributes and methods to access the retrieved data and request details
    - `response.status_code` : The HTTP status code (e.g., 200 for success, 404 for not found).
    - `response.text` : The content of the response as a string (useful for HTML or plain text).
    - `response.json()` : If the response contains JSON data, this method parses it into a Python dictionary or list.
    - `response.headers` : A dictionary of response headers.
    - `response.cookies` : A dictionary of cookies received in the response.