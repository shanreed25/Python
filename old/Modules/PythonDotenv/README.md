# python-dotenv
- allows for managing environment variables in Python applications by loading them from a `.env` file
- particularly useful for storing sensitive information like API keys or database credentials outside of your main codebase, preventing them from being committed to version control

# How to use
1. Install `python-dotenv`
2. Create `.env` file
    - add secrets into the `.env` file
3. Import into main file
    - `import dotenv`
    - `import os` 
4. In main file 
    - `load_dotenv()`: loads the environment variables from .env
    - `api_key = os.getenv("API_KEY")`:  access the environment variables using `os.getenv()`
