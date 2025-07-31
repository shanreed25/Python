# JavaScript Object Notation
**JSON simplifies the process of exchanging data by providing a human-readable and machine-parsable format that's both flexible and efficient**
- a lightweight data-interchange format used to transmit data between a server and a web application
- a text-based format for storing and exchanging data
- its human-readable and easy for computers to parse, making it a popular choice for web development and data exchange across different platforms
- derived from JavaScript object syntax but is language-independent, meaning it can be used with various programming languages
- based on a simple structure of key-value pairs, arrays, and other serializable values
    - Serializable values are data structures or objects that can be converted into a format suitable for storage or transmission, and then reconstructed later
    - This process is known as serialization, and the reverse process, reconstructing the original data from the serialized format, is called deserialization
- represents data in a hierarchical structure, often using curly braces {} to enclose key-value pairs
- Keys are strings, and values can be strings, numbers, booleans, arrays, or even other JSON objects
- data is transmitted as a string, making it suitable for sending information across networks

# JSON: Python
- Python provides the built-in json module for working with JSON data
- automatically maps Python data types to their JSON equivalents (e.g., Python dict to JSON object, list to array, str to string, int/float to number, True/False to true/false, None to null)
- JSON requires double quotes for string values and keys, and boolean values are lowercase (true, false)
- Be prepared to handle json.JSONDecodeError when parsing malformed JSON strings
- For serializing and deserializing custom Python objects, you can extend JSONEncoder and JSONDecoder classes respectively
- **Serialization (Python to JSON):**
    - **`json.dump()`**: writes a Python object as JSON data to a file-like object
    - **`json.dumps()`**: converts a Python object (like a dictionary or list) into a JSON-formatted string
- **Deserialization (JSON to Python):**
    - **`json.load()`**: reads JSON data from a file-like object and converts it into a python dictionary
    - **`json.loads()`**: parses a JSON-formatted string and converts it into a Python object
    - **`json.update()`**: update