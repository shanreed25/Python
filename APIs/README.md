# Application Programming Interface: API
- a set of defined rules and protocols that allows different software applications to communicate with each other
- acts as an intermediary, enabling one application to request services or data from another application without needing to understand the internal workings of that other application
- programmers can use APIs to create software or interact with an external system
- Common examples of APIs include those used for social media integration, payment gateways, weather data, mapping services, and much more
- API is interface(like a barrier) between your Program and and external system

#### Standardized Communication
APIs define how applications should interact, including data formats, request methods, and security protocols.
#### Abstraction
They abstract away the complexity of the underlying system, allowing developers to use functionalities without needing to know the intricate details of their implementation.
#### Interoperability
- APIs enable different applications, even those built with different programming languages or on different platforms, to work together seamlessly.
#### Facilitates Development
- Developers can leverage existing functionalities and data from other services through APIs, accelerating development and reducing the need to build everything from scratch.
the API in action

_______________________________________________________________________________________

# API ENDPOINT
**When an application wants to access a specific piece of data or perform a certain action through an API, it directs its request to the corresponding API endpoint**
- a specific, addressable location within an Application Programming Interface (API) where an application can send requests and receive responses
-  the precise locations that enable communication and data exchange between different software applications through an API
- serves as the point of interaction for accessing a particular resource or executing a specific function offered by the API
- **URL** endpoints are typically represented by a Uniform Resource Locator (URL), which acts as their unique address on the internet.
- **Resource or Function:** each endpoint is designed to expose a specific resource (a list of users, a single product etc...) or a particular function (creating a new user, updating an order etc...).
- **HTTP Methods:** endpoints often support various HTTP methods (GET, POST, PUT, DELETE) to define the type of operation to be performed on the resource.
- **Request/Response:** an application sends a request to an endpoint, and the API server processes it and sends back a response, which can include data, a status code, or error messages.


_______________________________________________________________________________________


## How APTs work
1. Your Application(The Customer)
    - request data or a service(using the rules the API has set)
    - this request is made to the external system
2. The API(The Menu)
    - takes the request and passes it to the external system
    - this API is connected to the external system
    - the external system sets the rules for the API
3. The External System(The Kitchen)
    - processes the request and provides the data or service
    - you must follow the rules of the API to get the data or service
4. API Actions(The Waiter)
    - gets the results from external system and returns the results to you application