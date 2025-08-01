import requests as rq




######################*********************************************************************************************
response = rq.get(url="http://api.open-notify.org/iss-now.json")#get data from endpoint
response.raise_for_status()
data = response.json()
print(data )# {'iss_position': {'longitude': '-82.2386', 'latitude': '24.2127'}, 'timestamp': 1754062642, 'message': 'success'}

# Get iss position, can tap into the json object just like a dictionary
iss_position = data["iss_position"]
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
print(latitude)



#### EXCEPTIONS*******************************************
response = rq.get(url="http://api.open-notify.org/iss-ssnow.json")#get data from endpoint

print(response)# returns response code: <Response [200]>


# Response Object Attributes
#.status_code is an attribute of the Response object returned after an HTTP request is made
# holds the numerical HTTP status code that the server returned in response to your request
print(response.status_code)# returns status code: 200

# What should we do if our program fails,
# it would be very hard to write code to
# rasie exceptions for every status code
# Use the request Module to generate exceptions

response.raise_for_status()# will raise an HTTPError if the HTTP request returned an unsuccessful status code.
#