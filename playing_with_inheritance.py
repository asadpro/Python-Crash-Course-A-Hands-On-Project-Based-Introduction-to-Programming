# class Car:
#        """A simple attempt to represent a car."""
#        def __init__(self, make, model, year):
#            self.make = make
#            self.model = model
#            self.year = year
#            self.odometer_reading = 0
           
#        def get_descriptive_name(self):
#            long_name = f"{self.year} {self.make} {self.model}"
#            return long_name.title()
           
#        def read_odometer(self):
#            print(f"This car has {self.odometer_reading} miles on it.")

#        def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#                self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")

#        def increment_odometer(self, miles):
#            self.odometer_reading += miles

# # When inheriting a class from parent class the parent class name must be inside parenthesis
# class ElectricCar(Car):
#     """Child class of Car class"""
    
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery_size = 75

#     def describe_battery(self):
#         """print a statement describing the battery size."""
#         if self.battery_size == 75:
#             print(f'This has a {self.battery_size}-kWh battery.')
#         else:
#             print(f'Extended battery upto {self.battery_size}-kWh battery.')


#     def extending_battery(self, new_battery):
#         self.battery_size = new_battery
    
#     def read_odometer(self):
#         """Method override from parent class Car"""
#         print(f'Tesla car have no Odometer Sorry!')


# tesla = ElectricCar(make='Tesla',model="model s", year = 2019)

# store = tesla.get_descriptive_name()

# tesla.describe_battery()
# tesla.extending_battery(new_battery=150)
# tesla.describe_battery()
# tesla.read_odometer()

# 🚚🚚🚚🚚🚚 Try it yourself challenges 🚚🚚🚚🚚🚚
"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class
called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1
(page 162) or Exercise 9-4 (page 167). Either version of the class will work; just pick the
one you like better. Add an attribute called flavors that stores a list of ice cream flavors.
Write a method that displays these flavors. Create an instance of IceCreamStand, and call
this method.

"""
# class Restaurant:

#     def __init__(self, restaurant_name, cuisine_type,flavors):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#         self.flavors = flavors


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
    




# class IceCreamStand(Restaurant):

#     def __init__(self, restaurant_name, cuisine_type, flavors):
#         super().__init__(restaurant_name, cuisine_type, flavors)

        
#     def displaying_flavors(self):
#         for flavor in self.flavors:
#             print(flavor)


# polka = IceCreamStand(cuisine_type='Geek',restaurant_name='Habib restaurant',flavors=['strawberry','banana','mango','avocada'])
# polka.displaying_flavors()

# 🚚🚚🚚🚚🚚 Try it yourself challenges 🚚🚚🚚🚚🚚
"""
9-7. Admin: An administrator is a special kind of user. Write a class called Admin that
inherits from the User class you wrote in Exercise 9-3 (page 162) or Exercise 9-5 (page
167). Add an attribute, privileges, that stores a list of strings like "can add post", "can
delete post", "can ban user", and so on. Write a method called show_privileges()
that lists the administrator’s set of privileges. Create an instance of Admin, and call your
method.

"""

# class User:
#     def __init__(self):
#         self.login_attempts = 0

#     def increment_login_attempts(self):
#         self.login_attempts +=1
#         print('Login attempts: ',self.login_attempts)
       

#     def reset_login_attempts(self):
#         self.login_attempts = 0   
#         print('Login attempts has been set to Zero: ',self.login_attempts) 


# class Admin(User):

#     def __init__(self,privileges):
#         super().__init__()
#         self.privileges = privileges

#     def show_privileges(self):
#         for privilige in self.privileges:
#             print(privilige)

# admin_obj = Admin(privileges=['can add post','can delete post','can update post','can create post'])
# admin_obj.show_privileges()
    
# 🚚🚚🚚🚚🚚 Try it yourself challenges 🚚🚚🚚🚚🚚
"""
9-8. Privileges: Write a separate Privileges class. The class should have one attribute,
privileges, that stores a list of strings as described in Exercise 9-7. Move the
show_privileges() method to this class. Make a Privileges instance as an attribute in
the Admin class. Create a new instance of Admin and use your method to show its
privileges.

"""


# class User:
#     def __init__(self):
#         self.login_attempts = 0

#     def increment_login_attempts(self):
#         self.login_attempts +=1
#         print('Login attempts: ',self.login_attempts)
       

#     def reset_login_attempts(self):
#         self.login_attempts = 0   
#         print('Login attempts has been set to Zero: ',self.login_attempts) 


# class Admin(User):
#     """Admin is special type of User which inherits from User class"""

#     def __init__(self):
#         super().__init__()

#         # Accessing instance as an attribute
#         self.privileges = Privileges(privileges=['can add post','can delete post','can update post','can create post'])
        

 

# class Privileges():
#     """This is a seperate and independing class inherited from no one."""
#     def __init__(self, privileges):
#         self.privileges = privileges
    
#     def show_privileges(self):
#         """Show priviliges regarding to admin"""
#         for privilige in self.privileges:
#             print(privilige)


# admin_obj = Admin()
# admin_obj.privileges.show_privileges()


