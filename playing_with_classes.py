# class Dog:
#     """Blueprint of a dog"""
#     # __init__ method works like a constructor and gets called whenever we create an object of a class
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     # Every method in a class have self parameter which refers to the current instance of the class
#     def sit(self):
#         """Dog is sitting"""
#         print(f'{self.name} is sitting')

#     def roll(self):
#         """Dog is rolling"""

#         print(f'{self.name} is now rolling')

# obj = Dog(age=34,name='Puppy')
# obj.roll()

# # 🍟🍟🍟🍟 Restaurants challenge of Class 🍟🍟🍟🍟
# """
# Exercise 9-1=> Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a
# method called describe_restaurant() that prints these two pieces of information, and a
# method called open_restaurant() that prints a message indicating that the restaurant is
# open.
# """
# # 🍟🍟🍟🍟 Expand the same challenge 🍟🍟🍟🍟
# """
# Three Restaurants: Start with your class from Exercise 9-1. Create three different
# instances from the class, and call describe_restaurant() for each instance.

# """
# class Restaurant:

#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def open_restaurant(self):
#         print("Restaurant is open !!!")

#     def describe_restaurant(self):
#         print(f'{self.restaurant_name} is the name of restaurant')
#         print(f'{self.cuisine_type} is the name of cuisine')
#         print('=================================')


# restaurant1 = Restaurant(restaurant_name='Habibi restaurant',cuisine_type='Lebanese Cuisine')
# restaurant2 = Restaurant(restaurant_name='Tory kababi restaurant',cuisine_type='Geek Cuisine')
# restaurant3 = Restaurant(restaurant_name='Roshan restaurant',cuisine_type='spanish Cuisine')
# restaurant1.open_restaurant()
# restaurant1.describe_restaurant()

# restaurant2.open_restaurant()
# restaurant2.describe_restaurant()

# restaurant3.open_restaurant()
# restaurant3.describe_restaurant()

# # 🍟🍟🍟🍟 Users challenge of Class 🍟🍟🍟🍟
# """
# 9-3. Users: Make a class called User. Create two attributes called first_name and
# last_name, and then create several other attributes that are typically stored in a user
# profile. Make a method called describe_user() that prints a summary of the user’s
# information. Make another method called greet_user() that prints a personalized
# greeting to the user.
# Create several instances representing different users, and call both methods for each
# user.

# """


# class User:
#     """User blue to create user instance"""
#     def __init__(self, first_name, last_name, address, phone_no):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.address = address
#         self.phone_no = phone_no
        
#     def greet_user(self):
#         """Greet the user"""
#         print(f"Hello {self.first_name+self.last_name}")

#     def describe_user(self):
#         """Describe information regarding the user"""
#         print(f'First name: {self.first_name}')
#         print(f'Last name: {self.last_name}')
#         print(f'Address: {self.address}')
#         print(f'Phone no: {self.phone_no}')
#         print('======================')

# user1 = User('asad','pro','dalazak road',+92313900784)
# user2 = User('hamad','khan','kohat road',+92312890784)
# user3 = User('bilal','jan','badhaber road',+92361990784)

# user1.greet_user()
# user1.describe_user()

# user2.greet_user()
# user2.describe_user()

# user3.greet_user() 
# user3.describe_user()

# # 🍟🍟🍟🍟 Changing Attribute value challenge of Class 🍟🍟🍟🍟

"""
9-4. Number Served: Start with your program from Exercise 9-1 (page 162). Add an
attribute called number_served with a default value of 0. Create an instance called
restaurant from this class. Print the number of customers the restaurant has served, and
then change this value and print it again.
Add a method called set_number_served() that lets you set the number of customers
that have been served. Call this method with a new number and print the value again.
Add a method called increment_number_served() that lets you increment the
number of customers who’ve been served. Call this method with any number you like
that could represent how many customers were served in, say, a day of business.

"""

# class Restaurant:

#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0


#     def open_restaurant(self):
#         print("Restaurant is open !!!")

#     def describe_restaurant(self):
#         print(f'{self.restaurant_name} is the name of restaurant')
#         print(f'{self.cuisine_type} is the name of cuisine')
#         print('=================================')
    
#     def set_number_served(self,customer_increase):
#         self.number_served +=customer_increase

#     def increment_number_served(self):
#             print(f'You have served {self.number_served} no of customers')


        
# 🚕🚕🚕🚕 Task one completed as shown below
# restaurant = Restaurant(restaurant_name='Habibi restaurant',cuisine_type='Lebanese Cuisine')
# restaurant.increment_number_served()
# restaurant.set_number_served(4)
# restaurant.increment_number_served()

'''
9-5. Login Attempts: Add an attribute called login_attempts to your User class from
Exercise 9-3 (page 162). Write a method called increment_login_attempts() that
increments the value of login_attempts by 1. Write another method called
reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts() several
times. Print the value of login_attempts to make sure it was incremented properly, and
then call reset_login_attempts(). Print login_attempts again to make sure it was
reset to 0.
'''

class User:
    def __init__(self):
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts +=1
        print('Login attempts: ',self.login_attempts)
       

    def reset_login_attempts(self):
        self.login_attempts = 0   
        print('Login attempts has been set to Zero: ',self.login_attempts) 


user1 = User()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()



