# Flask
- a micro web framework written in Python, designed for building web applications
-  classified as a "microframework" because it provides the core functionalities for web development without imposing strict dependencies or including a large number of built-in features like database abstraction layers or form validation
- emphasizes flexibility and allows developers to choose and integrate external libraries and tools based on their specific project requirements
- offers a lightweight and flexible foundation for building web applications in Python, suitable for projects ranging from small-scale APIs to more complex web applications where customizability and control over component selection are desired

#  __name__ variable
***Flask uses the __name__ variable when creating a Flask application instance, as in app = Flask(__name__)***
### Why
**`Flask(__name__)` tells Flask where to find the necessary components of your application by providing it with the name of the module or package it's running within**
- **Resource Location:** Flask uses the value passed to its constructor (often __name__) to determine the root path of your application
    - this is crucial for Flask to correctly locate resources such as templates, static files (CSS, JavaScript, images), and other application-specific files.
- **Dynamic Adaptation:** By using __name__, Flask can dynamically adapt to whether your application is being run directly as a script or imported as a module within a larger project. 
    - This ensures that Flask can correctly find its resources regardless of how the application is launched.
- Learn more about the `__name__` variable [here](../../SpecialAttributes.md#__name__)