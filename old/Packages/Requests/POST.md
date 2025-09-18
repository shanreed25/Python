# `requests.post()
- makes a POST request, which allow use to give the external system some piece of data
    - used to send HTTP POST requests to a specified URL
- typically used to send data to a server to create or update a resource
- call the `requests.post()` method

# How to send data
- Basic Usage: to send a simple POST request with form-encoded data, pass a dictionary to the data argument

### Sending JSON Data
- to send JSON data in the request body, pass a dictionary to the json argument
- the requests library will automatically set the Content-Type header to application/json


# Response


#### Important Parameters
- **headers**: A dictionary of HTTP headers to send with the request.
- **files**: A dictionary of files to send (e.g., for file uploads).
- **auth**: A tuple for HTTP authentication (e.g., ('username', 'password')).
- **timeout**: An integer or tuple specifying how many seconds to wait for the server to respond.
- **cookies**: A dictionary of cookies to send.
- **verify**: A boolean or string to verify the server's TLS certificate. 


#### Handling the Response
- the requests.post() method returns a requests.Response object, which contains information about the server's response, including
    - **response.status_code**: The HTTP status code (e.g., 200 for success).
    - **response.text**: The response content as a string.
    - **response.json()**: If the response is JSON, this method converts it to a Python dictionary.
    - **response.headers**: A dictionary of response headers.
- the response we are interested in from a post request is weather or not it was sucessful