import requests as rq




######################*********************************************************************************************
response = rq.get(url="http://api.open-notify.org/iss-now.json")#get data from endpoint
response.raise_for_status()
data = response.json()
print(data )# {'iss_position': {'longitude': '-82.2386', 'latitude': '24.2127'}, 'timestamp': 1754062642, 'message': 'success'}

# Get iss position, can tap into the json object just like a dictionary
iss_position = data["iss_position"]
longitude = data["iss_position"]["longitude"] # String
latitude = data["iss_position"]["latitude"] # String
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


#####API With Paramters********************************************************************************************************

MY_LAT = 36.169941
MY_LONG = -115.139832

# requests.get() function in Python offers several optional parameters to customize HTTP GET requests.
parameters = {
"lat": MY_LAT,
"lng": MY_LONG,
"formatted": 0
}

#API: https://sunrise-sunset.org/api

# Format parameters in URL String
# You can paste this URL in a browser with a json formatter and see a nicer version of the data
# response = rq.get(url="https://api.sunrise-sunset.org/json?lat=36.169941&lng=-115.139832")
#OR use params option*******************************************
response = rq.get(url="https://api.sunrise-sunset.org/json", params=parameters,)
response.raise_for_status()
data = response.json()
print(data)

# Get Sunrise and Sunset Hour Values
sunrise = data["results"]["sunrise"]# String
sunrise_hour = sunrise.split("T")[1].split(":")[0]# String
# print(f"Sunrise: {sunrise}")# 2025-08-01T12:46:43+00:00
print(f"Sunrise Hour: {sunrise_hour}")# ['2025-08-01', '12:46:43+00:00']

sunset = data["results"]["sunset"]# String
sunset_hour = sunset.split("T")[1].split(":")[0]# String
# print(f"Sunset: {sunset}")# 2025-08-02T02:47:02+00:00
print(f"Sunset Hour: {sunset_hour}")# ['2025-08-02', '02:47:02+00:00']

