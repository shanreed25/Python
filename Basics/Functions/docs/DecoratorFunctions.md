# Decorator Functions
- allow you to modify or extend the behavior of functions or methods without directly altering their original source code
- they "wrap" a function, adding functionality before, after, or even in place of the original function's execution
- typically applied using the `@decorator_name` syntax placed immediately above the function definition you want to decorate
- is syntactic sugar for function_name = decorator_name(function_name)
- imagine that you have a bunch of functions in a class or module and you want to add some functionality to each of these functions, a decorator function can help you do this
- decorators provide a clean and concise way to add "meta-functionality" to your code, promoting reusability and maintainability

__________________________________________________________________

### How To Create Decorator Functions
- A decorator function(`decFunc`) takes the function(`paraFunc`) it is decorating as an argument
- Inside the decorator, a new "wrapper" function(`wrapperFunc`) is defined
- This wrapper function(`wrapperFunc`) contains the additional logic you want to apply, and it also calls the original decorated function(`paraFunc`)
- the decoratorn(`decFunc`) returns this wrapper function(`wrapperFunc`)
- when the decorated function(`decFunc`) is called, it's actually the wrapper function that executes, incorporating the added behavior

__________________________________________________________________

### Use Cases
**Decorators are widely used for various purposes, including:**
- **Logging:** Adding logging messages before and after function calls.
- **Authentication/Authorization:** Checking user permissions before allowing access to a function.
- **Timing/Profiling:** Measuring the execution time of a function.
- **Caching/Memoization:** Storing and retrieving the results of expensive function calls to avoid recalculation.
- **Error Handling:** Wrapping functions with try-except blocks to handle exceptions gracefully.
- **Separation of Concerns:** Keeping cross-cutting concerns (like logging or security) separate from the core business logic.