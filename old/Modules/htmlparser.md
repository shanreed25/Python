# html.parser

- `html.parser` works by processing HTML content as a stream. It parses the input HTML and calls specific methods of a subclass as it encounters different elements like start tags, end tags, data, or comments
- `soup = BeautifulSoup(response.content, "html.parser")`


If you get an error that says "bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: html-parser." Then it means you're not using the right parser, you'll need to import lxml at the top and install the module then use "lxml" instead of "html.parser" when you make soup.
- try "lxml" to make soup with the web page HTML you get back. You would use a different parser like this:
- `soup = BeautifulSoup(response.content, "lxml")`



