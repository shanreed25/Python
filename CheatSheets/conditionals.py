

def my_function():
    if 5 < 10:
        return True
    else:
        return False
# the above code can be simplfied

def my_function():
    return 5 < 10

 # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= 5 + MY_LAT and MY_LONG - 5 <= iss_longitude<= 5 + MY_LONG:
            return True
    
#**************************************************************************************************************************

# To check if price_a is within 5% higher or lower than price_b in Python, you can calculate the lower and upper bounds 
# of the acceptable range around price_b, and then check if price_a falls within that range. Here's how you can do it