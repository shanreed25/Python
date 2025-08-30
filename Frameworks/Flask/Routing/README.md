# Flask: [Routing](https://flask.palletsprojects.com/en/stable/quickstart/#routing)
- the route() decorator is used to bind a function to a URL
    - `@app.route('/')`: used to associate a URL path with a view function
    - when a user navigates to that URL, Flask executes the corresponding function

## [Variable Rules](https://flask.palletsprojects.com/en/stable/quickstart/#variable-rules)
- you can make parts of the URL dynamic and attach multiple rules to a function
    - `@app.route('/user/<username>')`: create dynamic URLs that accept user-provided values by using angle brackets

## [Unique URLs / Redirection Behavior](https://flask.palletsprojects.com/en/stable/quickstart/#unique-urls-redirection-behavior)

## [HTTP Methods](https://flask.palletsprojects.com/en/stable/quickstart/#http-methods)
- By default, a route only answers to GET requests, so GET is allowed by default on all routes
    - `@app.route("/random", methods=["GET"])` and `@app.route("/random")` is the same
You can use the methods argument of the route() decorator to handle different HTTP methods
- `@app.route('/login', methods=['GET', 'POST'])`
    - keeps all methods for the route within one function, which can be useful if each part uses some common data
- `@app.get('/login')` and `@app.post('/login')`
    - separates views for different methods into different functions

