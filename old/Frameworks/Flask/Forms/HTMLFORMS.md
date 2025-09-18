# HTML Forms in Flask: 
## action attribute
- action attribute of the form can be set to the path
    - `<form action="/sendemail" method="post">`
- or action attribute of the form can be dynamically generated with `url_for`
    - `<form action="{{ url_for('receive_data') }}" method="post">`
- Depending on where your server is hosted, the `"/sendemail"` path may change
- So it's usually a better idea to use `url_for` to dynamically generate the url for a particular function in your Flask server


## The [Request Object](https://flask.palletsprojects.com/en/stable/quickstart/#the-request-object)
#### request method
- Flask has a method called request (don't confuse this with the requests module) which allows us to tap into the parameters of the request that was made to our server
    - `from flask import request`
- current request method(GET, POST etc...>) is available by using the method attribute
    - `request.method`
- to access form data (data transmitted in a POST or PUT request) you can use the form attribute and the input name as the key
    - `request.form` gives us the data from the form as a dictionary where the `name` attribute is the key and the value is the value entered in the form
    - `request.form['user_name']`
    - if the key does not exist in the form attribute, a special KeyError is raised and you can catch it like a standard KeyError but if you don’t do that, a HTTP 400 Bad Request error page is shown instead
- to access parameters submitted in the URL (?key=value) you can use the args attribute
    - `searchword = request.args.get('key', '')`
    - it is recommended to access URL parameters with get or by catching the KeyError because users might change the URL and presenting them a 400 bad request page in that case is not user friendly
- [Requests Docs](https://flask.palletsprojects.com/en/stable/api/#flask.Request)


- `enctype="multipart/form-data"`: When the form contains file inputs, it must have this encoding set, otherwise the files will not be uploaded and Flask won't see them


- see how to Make POST Requests with Flask and HTML Forms [here](https://github.com/shanreed25/Python-Cheatsheet/blob/main/FlaskApplication/docs/flaskApp/server.py#L48)


