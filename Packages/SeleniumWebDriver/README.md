# Selenium WebDriver
- free tool that allows us to automate the browser, getting the browser to do things automatically depending on a script or a piece of code that we write
- using a selenium driven browser we can type, click, scroll, search or anything that a human can do on a website
- can basically build a robot and tell it what to do in a browser
- [Selenium Docs](https://selenium-python.readthedocs.io/)
- [Selenium Dev](https://www.selenium.dev/)


# Install, Setup and get started with Selenium
- Install the selenium package
- `import selenium`
- `from selenium import webdriver`
    - contains code for us to be able to interact with browsers
    - can interact with a bunch of different browser
- `driver = webdriver.Chrome()`
    - bridges the selenium code to work with the latest version of the Chrome browser
- `driver.get("https://www.amazon.com")`
    - will open amazon.com in chrome if on windows
    - if you are on a Mac, you will get a popup to verify that the app is free od malware
        - click cancel, go to apple symbol --> system preferences --> security & privacy 
        - then you will see "chromedriver was blocked from use....." click `Allow Anyway`
        - run the code again and t=you will get another popup and just click `Open`
- the chrome browser is closed immediately after the program is done running, you must configure the web driver to keep the browser open 
    ```
        # Keeps Chrome browser open after program finishes running
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=chrome_options)
    ```
- you can also close the tabs and quit Chrome programmatically
    - closes a single active tab: `driver.close()`
    - quit the entire browser: `driver.quit()`

- [Find and Locate specific HTML elements on the webpage](./SeleniumWedriver.md)