import phonenumbers
from phonenumbers import carrier , geocoder , timezone
#import modules

mobilenr = input("Enter your Mobile Number with Countrycode ")
mobilenr = phonenumbers.parse(mobilenr)

# get timezone a phonenumber
print(timezone.time_zones_for_number+(mobilenr))


#getting carrier of a phonenumber 
print(carrier.name_for_number(mobilenr, "en" ))


#getting region information
print(geocoder.description_for_number(mobilenr, "en" ))

#Validating a phonenumber
print("Valid Phone Number  :",phonenumbers.is_valid_number(mobilenr))

#checking possibility of a number 
print("Checking possibility of a Number :", phonenumbers.is_possible_number(mobilenr))

