class Restaurant:

    def __init__(self, restaurant_name, cuisine_type,flavors):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.flavors = flavors


    def open_restaurant(self):
        print("Restaurant is open !!!")

    def describe_restaurant(self):
        print(f'{self.restaurant_name} is the name of restaurant')
        print(f'{self.cuisine_type} is the name of cuisine')
        print('=================================')
    
    def set_number_served(self,customer_increase):
        self.number_served +=customer_increase

    def increment_number_served(self):
            print(f'You have served {self.number_served} no of customers')
    




class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type, flavors)

        
    def displaying_flavors(self):
        for flavor in self.flavors:
            print(flavor)

"""
9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173). Store the
classes User, Privileges, and Admin in one module. Create a separate file, make an
Admin instance, and call show_privileges() to show that everything is working
correctly
"""


class User:
    def __init__(self):
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts +=1
        print('Login attempts: ',self.login_attempts)
       

    def reset_login_attempts(self):
        self.login_attempts = 0   
        print('Login attempts has been set to Zero: ',self.login_attempts) 


class Admin(User):

    def __init__(self,privileges):
        super().__init__()
        self.privileges = privileges

    def show_privileges(self):
        for privilige in self.privileges:
            print(privilige)

        