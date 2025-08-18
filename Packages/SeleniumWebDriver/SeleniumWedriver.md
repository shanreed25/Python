# Selenium WebDriver: Find and Locate specific HTML elements on the webpage
- when selenium locates a particular element it will not print out the actual HTML element
- it will give you the element as a selenium element like this:
    - `<selenium.webdriver.remote.webelement.WebElement (session="bea3e4d1f9c21b66d72dcbd5881a6f74", element="f.77CF3CEEB94A63BE27B6D708F965B129.d.1E7831F2F2A09C014496EFF3606E08F8.e.63")>`
    - you can access the actual HTML elements using dot notation
        - `price_dollar.tag_name`, `search_bar.get_attribute("placeholder")`, `search_bar.find_element(By.ID, value="search")`
        - access properties: `search_bar.size`, `price_dollar.text`


## By class
- the By class in Selenium is an abstract class that provides mechanisms for locating elements within a web document
- acts as the central component for defining how web elements are located during automation, providing a structured and versatile approach to element identification
- serves as the foundation for various locator strategies used to identify specific web elements on a page
- includes static methods corresponding to different locator strategies, enabling the identification of elements based on their attributes or positions within the HTML structure
- As an abstract class, `By` cannot be instantiated directly. Instead, its static methods are called using the class name; `By.id()`
- `from selenium.webdriver.common.by import By`
- use `By.` followed by the method `By.id()`
    - `name()`, `className()`, `tagName()`, `linkText()`, `partialLinkText()`, `xpath()`, `cssSelector()`

### By class Usage with findElement and findElements
- The By class is typically used in conjunction with the `findElement()` `and findElements()` methods of the WebDriver instance or a WebElement
    - `driver.findElement(By.ID("elementId"))`: Locates and returns the first WebElement matching the specified ID.
    - `driver.findElements(By.CLASS_NAME("elementClass"))`: Locates and returns a list of all WebElements matching the specified class name
    - `driver.find_elemnt(By.CSS_SELECTOR, value=".link")`: find web elements based on their CSS selectors
- `By.xpath` is a locator strategy used to find web elements on a page using XPath expressions
    - XPath is a powerful language for navigating through the XML structure of a document, and since HTML can be treated as XML, it can be used to locate elements on a webpage
    - from web page click inspect and right click on the element in the DOM and click `Copy` --> `Copy XPath`
    - `driver.find_elemnt(By.XPATH, value='//*[@id="sfooter"]/h1')`
    - [More about XPath](https://www.w3schools.com/xml/xpath_intro.asp)
```
    price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
    price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
    print(f"The price is ${price_dollar.text}.{price_cents.text}")
```
- this is so much shorter than using `Beautiful Soup` because, you are driving a browser and the browser sends all the headers and information that the site expects from an actual user
- `Beautiful Soup` get stuck when the website is being rendered using JS, React, Angualr etc...
    - the HTML content takes time to load, or requires certain conditions to be true to load
    - Selenium allows us to act as a human looking at the elements and values