# Environment Management
- Accessing and modifying system environment variables

## OS Module: Environment Variables
- enables applications to be configured externally through environment variables, making them more adaptable to different deployment environments (development, staging, production, etc.)
- Accessing, setting, and deleting environment variables using functions like `os.getenv()`, `os.putenv()`, and `os.unsetenv()`

#### Accessing Environment Variables
- **`os.environ`** a dictionary-like object that contains all current environment variables as key-value pairs
    - you can access individual variables like dictionary entries
    - `my_api_key = os.environ['API_KEY']`: If the variable does not exist, accessing it this way will raise a KeyError
- **`os.environ.get(key, default=None)`** is a safer method to retrieve an environment variable
    - returns the value of the specified key if it exists, otherwise it returns None or the default value you provide
    - prevents a KeyError that would occur if you tried to access a non-existent key directly using os.environ[key]

#### Setting Environment Variables:
- you can set new environment variables or modify existing ones by assigning values to keys in the os.environ dictionary
- **`os.environ['ENV_VARIABLE'] = 'env_value'`**

**These changes are typically temporary and only affect the current Python process and its child processes. They are not persistent across system reboots or new terminal sessions unless set up externally (e.g., in .bashrc or system-wide configurations)**

3. Deleting Environment Variables:
    - you can remove an environment variable using the `del` keyword on the os.environ dictionary
    -  **`del os.environ['ENV_VARIABLE']`**



# Environment Variables
- Windows Powershell: `dir Env:`
- Mac PyCharm using Bash: `env`
- Create Environment Variable In Terminal: `export MY_API_KEY=1234567890oiuytrewqasdfgh`
    - make sure there are no spaces between the equal sign
    - the `os` module is used to use the environment variable
    - `import os`
    - `api_key = os.environ.get("MY_API_KEY")`

1. Set environment variables
    - `os.environ["APP_ID"] = APP_ID`
2. Get an environment variable
