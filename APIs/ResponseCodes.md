# Response Codes
- HTTP response codes are like short notes from a server that get tacked onto a web page, indicating the status of an HTTP request
- messages from the server about the outcome of a page request
- Understanding these codes aids web professionals and users in troubleshooting and improving web experiences

# JSON response codes and their meanings
- When working with JSON responses in APIs, you'll encounter HTTP status codes that indicate the outcome of your request
- These codes fall into categories, each conveying a different type of message. 


##### HTTP response codes fall into five categories based on their first digit
- Informational responses: [100s]
- Successful responses: [200s](#successful-responses-2xx)
- Redirection messages: [300s](#redirection-messages-3xx)
- Client error responses: [400s](#client-error-responses-4xx)
- Server error responses : [500s](#server-error-responses-5xx)
- For a full lists of response codes go [here](https://www.webfx.com/web-development/glossary/http-status-codes/)
_______________________________________________________________________________________
### Informational response: We are working on it
### Successful responses: You should be getting what you asked for
- **200 OK:** Indicates the request was successful, and the response body contains the requested data.
- **201 Created:** Signifies a new resource was successfully created as a result of the request (often after a POST or PUT request).
- **202 Accepted:** Means the request has been accepted for processing, but the processing is not yet complete. This is useful for tasks that take a long time to finish.
- **204 No Content:** The request was successful, but there is no content to return in the response body. 

### Redirection messages: You cannot get what you asked for here, Go away
- **301 Moved Permanently:** Indicates the requested resource has been moved to a new, permanent location.
- **302 Found:** The resource is temporarily located at a different URL.
- **304 Not Modified:** The client's cached version of the resource is still valid, saving bandwidth by avoiding re-transmission of the full response. 
### Client error responses: You Screwed Up
- **400 Bad Request:** The server cannot understand the request due to invalid syntax or other client-side errors.
- **401 Unauthorized:** The client needs to authenticate to access the requested resource.
- **403 Forbidden:** The client is authenticated but lacks the necessary permissions to access the resource.
- **404 Not Found:** The requested resource could not be found
    - invalid endpoint
- **429 Too Many Requests:** The client has sent too many requests in a given timeframe (often used for rate limiting). 
### Server error responses: Server Screwed Up
- **500 Internal Server Error:** A generic error message indicating an unexpected condition on the server.
- **502 Bad Gateway:** The server, acting as a gateway or proxy, received an invalid response from an upstream server.
- **503 Service Unavailable:** The server is temporarily unable to handle requests, possibly due to overload or maintenance.
- **504 Gateway Timeout:** The server, acting as a gateway or proxy, did not receive a timely response from an upstream server. 
Remember, while HTTP status codes provide a general overview of the request's outcome, detailed error information should be included within the JSON response body itself for greater clarity and debug-ability.