# `requests.put()`
- used to send an HTTP PUT request to a specified URL
- primarily used to update or replace an existing resource on a server. 


#### Parameters
- **url**: The URL of the resource to be updated or created.
- **data**: (Optional) A dictionary, list of tuples, bytes, or file-like object to send in the body of the request. This is useful for sending form-encoded data. 
- **json**: (Optional) A JSON serializable Python object to send in the body of the request. Requests will automatically set the Content-Type header to application/json when using this parameter. 
- **headers**: (Optional) A dictionary of HTTP headers to send with the request.
- **auth**: (Optional) A tuple for basic authentication (e.g., (username, password)) or a custom authentication object.
- **files**: (Optional) A dictionary of files to upload.


#### Important Considerations
- **Idempotence**
    - PUT requests are idempotent, meaning that making the same request multiple times will have the same effect as making it once. This distinguishes it from POST, which can create multiple resources with repeated requests.
- **Response Object**
    - the requests.put() method returns a Response object, which contains information about the server's response, including the status code, headers, and body content.
- **Error Handling**
    - it is crucial to check the response.status_code to determine if the request was successful and handle any errors appropriately. Common success codes for PUT are 200 (OK) and 201 (Created).