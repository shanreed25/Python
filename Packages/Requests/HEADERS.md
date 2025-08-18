# Headers
When making a request to any website, your browser will send some additional data along with the request
- typically the information included in the headers will be information regarding what browser you are using, what computer you have, and what your preferred language is
- by using the headers, servers can respond with the right website for your region and your language
- you can see headers that your own browser is sending by going to this website: `http://myhttpheader.com/`
    - try different browsers (Chrome, Brave, Firefox, Safari) and see how the headers change

### Add the headers to your code
- if you pass some headers along then servers can give you pages in your language, currency, etc...
- will make your request look (slightly) more human and less like a bot
    - headers include data that is sent over by a browser rather than a script
    - many web servers like Amazon's may block requests they think originate from bots
- request without headers: `response = requests.get("https://www.udemy.com/")`
- pass some headers alongside your requests: `response = requests.get("https://www.udemy.com/", headers={"Accept-Language":"en-US"})`