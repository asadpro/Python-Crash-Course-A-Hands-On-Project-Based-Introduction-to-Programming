# Nesting in detail
# 💡💡 We can put dicionaries inside another dictionary and then put it inside a list.

# student_1 = {"name": "asad", "GPA": 2.5}
# student_2 = {"name": "hamza", "GPA": 3.4}
# student_3 = {"name": "saqib", "GPA": 3.3}

# students = [student_1, student_2, student_3]

# for student in students:
#     print(student)


# 🍟🍟🍟Make a list of aliens using range() function🍟🍟🍟
# aliens = []
# for alien in range(1,13):
#     counter = 1

#     if alien<=4:
#         aliens.append({'color':'green'})

#     elif alien<=8:
#         aliens.append({'color':'yellow'})

#     elif alien<=12:
#         aliens.append({'color':'red'})

# # for alien in aliens:
# #     print(alien)
# users = {
#     'einstein':{
#         'first':'albert',
#         'last':'einstein',
#         'location':'newyork'
#     },
#     'billo':{
#         'first':'bill',
#         'last':'gate',
#         'location':'america'
#     }
# }
# for username, user_info in users.items():
#     print(f"\nUsername: {username}")
#     fullName = user_info['first']+user_info['last']
#     location = user_info['location']
#     print(f'\tFull name: {fullName}')
# print(f'\tLocation: {location}')

# 🍟🍟🍟Medium size challenge of dictionaries🍟🍟🍟
"""
Use a dictionary to store information about a person you know. Store their
first name, last name, age, and the city in which they live. You should have keys such as
first_name, last_name, age, and city. Print each piece of information stored in your
dictionary.

"""

# p1 = {
#     "first_name": "ilyas",
#     "last_name": "ahmad",
#     "age": 24,
#     "city": "peshawar",
# }
# p2 = {
#     "first_name": "sadiq",
#     "last_name": "aslam",
#     "age": 23,
#     "city": "Kankola",
# }
# p3 = {
#     "first_name": "salman",
#     "last_name": "gohar",
#     "age": 20,
#     "city": "Hangu",
# }

# people = [p1,p2,p3]
# for ppl in people:
#     for key, value in ppl.items():
#         print(key,":",value)
#         if key =='city':
#             print('\n🎇🎇🎇🎇🎇🎇🎇🎇\n')

# 🍟🍟🍟 Pets challenge of dictionaries🍟🍟🍟
"""
Pets: Make several dictionaries, where each dictionary represents a different pet. In
each dictionary, include the kind of animal and the owner’s name. Store these dictionaries
in a list called pets. Next, loop through your list and as you do, print everything you
know about each pet

"""
# cat = {
#     'owner_name':'salena',
#     'kind':'Cat comes in cheeta\'s categories.'
# }
# dog = {
#     'owner_name':'walter',
#     'kind':'I don\'t know what\'s the kind of dog.'
# }
# elephant = {
#     'owner_name':'sameer',
#     'kind':'This is an african bush elephant.'
# }

# pets = [cat,dog,elephant]
# for pet in pets:
#     for key, value in pet.items():
#         print(key," :",value)

# 🍟🍟🍟 Favorite Places challenge of dictionaries🍟🍟🍟

"""
Favorite Places: Make a dictionary called favorite_places. Think of three names
to use as keys in the dictionary, and store one to three favorite places for each person. To
make this exercise a bit more interesting, ask some friends to name a few of their favorite
places. Loop through the dictionary, and print each person’s name and their favorite
places.
"""
# I will make this program more dynamic where i will be asking users to enter their name and
# their favourite place then we will print out that information once all the users done.
# favorite_places = {}
# terminate = False
# while not terminate:
#     name = input("Enter your name: ")
#     fav_place = input("Enter your favourite place name: ")
#     # favorite_places[name]={name:fav_place}
#     # favorite_places['Favourite Place'] = fav_place
#     favorite_places[name] = fav_place
#     ask_to_end = input('Is there anyone else left to enter their opinion? "y" or "n"')
#     if ask_to_end == "n":
#         terminate = True
# for key, value in favorite_places.items():
#     print("Name is: ", key, "\nFavourite place: ", value)

# 🍟🍟🍟 Favorite numbers challenge of dictionaries🍟🍟🍟
"""
Favorite Numbers: Modify your program from Exercise 6-2 (page 99) so each
person can have more than one favorite number. Then print each person’s name along
"""

# favourite_numbers = {}
# terminate = False
# while not terminate:
#     name = input("Enter your name: ")
#     fav_nums = input("Enter your favourite numbers separating by commas (,): ")
#     eol = input('Is there anyone else left to enter their opinion? "y" or "n"')
#     if eol == 'n':
#         terminate = True

#     list1 = list(fav_nums.split(','))
#     # converting string integer to integers numbers
#     numbers = [int(item) for item in list1] # This is list comprehension
#     favourite_numbers[name]=numbers

# for name, number in favourite_numbers.items():
#     print('Name: ',name, '\nFavourite numbers: ',number,'\n\n')

# 🍟🍟🍟 Cities challenge of dictionaries🍟🍟🍟
"""
Cities: Make a dictionary called cities. Use the names of three cities as keys in
your dictionary. Create a dictionary of information about each city and include the
'country' that the city is in, its approximate population, and one fact about that city. The
keys 'for' each city’s dictionary should be something like country, population, and fact.
'Print' the name of each city and all of the information you have stored about it.
"""
# cities = {
#     'islamabad':{
#         'country':'pakistan',
#         'population':'2,million',
#         'fact':'capital of pakistan'
#     },
#     'khyber':{
#         'country':'pakistan',
#         'population':'32,million',
#         'fact':'land of hopitality'
#     },
#     'punjab':{
#         'country':'pakistan',
#         'population':'55,million',
#         'fact':'Intelligent formers'
#     },
# }
# for city, information in cities.items():
#     print('=========================')
#     print('City name: ',city,f'\nInformation about {city}: ')
#     for key, value in information.items():
#         print(key,':',value)

# 🍟🍟🍟 Extensions challenge of dictionaries🍟🍟🍟

