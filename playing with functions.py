"""
Positional arguments vs keyword arguments (in dart named arguments). Positional parameter look 
for the position of the argument in function call whereas keyword argument doesn't required position of the 
arguments.
"""
# 🍟🍟T-Shirt challenge of functions🍟🍟
"""
T-Shirt: Write a function called make_shirt() that accepts a size and the text of a
message that should be printed on the shirt. The function should print a sentence
summarizing the size of the shirt and the message printed on it.
"""

# def make_shirt(t_size,message):
#     print('Size of the T-shirt: ',t_size)
#     print('Message on shirt: ',message)

# # Calling function using positional argument
# make_shirt(55,'Afghan Taliban Zindabad')
# # Calling function using keyword argument
# make_shirt(t_size=34,message='Long live pakistan')

# 🍟🍟Large T-Shirt challenge of functions🍟🍟

"""Large Shirts: Modify the make_shirt() function so that shirts are large by default
with a message that reads I love Python. Make a large shirt and a medium shirt with the
default message, and a shirt of any size with a different message.
"""
# def make_shirt(t_size='large',message='I love python'):
#     if t_size=='large' or t_size == 'medium':
#         print('Size: ',t_size)
#         print('Message: ',message)
#     else:
#         print('Size: ',t_size)
#         print('Message: ',message)

# make_shirt()
# print('printing with default values')
# make_shirt(t_size='medium',message='Knowlege is potential power')

# 🍟🍟Large T-Shirt challenge of functions🍟🍟
"""
Cities: Write a function called describe_city() that accepts the name of a city and
its country. The function should print a simple sentence, such as Reykjavik is in
Iceland. Give the parameter for the country a default value. Call your function for three
different cities, at least one of which is not in the default country.

"""


# def describe_city(name, city, country="pakistan"):
#     print(f"{name} is in {city} which is the city of {country}")


# describe_city(name="asad", city="khyber pakhtunkhwa")
# describe_city(name="shehryar", city="Punjab")
# describe_city(name="amir khan", city="Delhi",country='India')


# 🍟🍟City Names return challenge of functions🍟🍟
"""
City Names: Write a function called city_country() that takes in the name of a
city and its country. The function should return a string formatted like this:
"Santiago, Chile"

Call your function with at least three city-country pairs, and print the values that are
returned.
"""
# def city_country(city,country):
#     dictionary = {}
#     dictionary[city] = country 
#     return dictionary

# res = city_country(city='Balochistan',country='Pakistan')
# print(res)

# 🍟🍟Passing list into function parameter challenge of functions🍟🍟
# def greet_users(users):
#     for user in users:
#         print(f"Hello, {user.title()}")


# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)


# 🍟🍟 Sending Messages challenge of functions🍟🍟
# messages = ['how are you? ', 'fine', 'good to see you','glad to see you alive']
# def send_messages(list_msg):
#     sent_messages = []
#     for msg in list_msg:
#         sent_messages.append(msg)

#     print("Old message list: ",list_msg)
#     print("Updated message list: ",sent_messages)

# send_messages(messages)


# 🍟🍟 Passing no of arbitrary arguments in the function call  challenge of functions🍟🍟

"""
Sometime we need to pass more than one arguments to the function but we don't know ahead of time
so we need the asterik * approach e.g. below mobiles variable will take no input and will put it into tuple
no matter how many we want. In other words * tell the python to create an empty tuple name mobiles."""
# def mobile_buying(* mobiles):
#     for mobile in mobiles:
#         print(mobile)

# mobile_buying('samsung','nokia','iphone','motorolla','oppo','poco')

# 🍟🍟 Passing no of arbitrary keyword arguments in the function  challenge of functions🍟🍟
""" Sometime we need to pass more than one dictionary item to the function so to create an empty dictionary
we need double asteriak (**) e.g."""


# def build_user(firstName,lastName,**user_info):
#     user_info['First_name'] = firstName
#     user_info['Last_name'] = lastName
#     return user_info

# user_information = build_user(firstName='Asad',lastName='Pro3.1',location = 'Dalazak Road',email = 'saeed.mlops.techy@gmail.com',postalCode = 25000)
# # for index in range(len(user_information)-1,-1,-1):
# print(user_information)

# 🍟🍟 Sandwiches challenge of functions🍟🍟
"""
Sandwiches: Write a function that accepts a list of items a person wants on a
sandwich. The function should have one parameter that collects as many items as the
function call provides, and it should print a summary of the sandwich that’s being
ordered. Call the function three times, using a different number of arguments each time."""

# def sandwitch(*items_sandwitch):
#     for item in items_sandwitch:
#         print('You ordered: ',item)

# sandwitch('mushrooms','green peppers','extra cheese')
# print('\n===second order===\n')
# sandwitch('burger','chili burger')

# 🍟🍟 User Profile challenge of functions🍟🍟

"""
User Profile: Start with a copy of user_profile.py from page 149. Build a profile of
yourself by calling build_profile(), using your first and last names and three other keyvalue pairs that describe you.
"""

# def build_profile(first, last, **user_info):

#        """Build a dictionary containing everything we know about a user."""
#        user_info['first_name'] = first
#        user_info['last_name'] = last    
#        return user_info


# user_profile = build_profile('Asad','Pro3.1',education ='BCS',designation='Computer researcher')
# print(user_profile)

# 🍟🍟 Car challenge of functions🍟🍟

def car_info(manufacturer,model_name,**car_info):
    """Return car information"""
    car_info['Manufacturer'] = manufacturer
    car_info['ModelName'] = model_name
    return car_info

car = car_info(manufacturer='Suzuki',model_name='ravi',color='blue',speed=150,wheels = 4)
for key,value in car.items():
    print(key,':',value)

# We can call the pizza file like this 
import pizza as pz
pz.make_pizza()

# We can call import the make_pizza function without importing the whole module

from pizza import make_pizza
make_pizza() 

# We can also import all the function within module with a single asterik * which tells python
# to select all the stuff from that module and import it in the current file so we don't have to import it one by one.

from pizza import *
print('\n\nCalled using asterik (*) keyword')
make_burger()

