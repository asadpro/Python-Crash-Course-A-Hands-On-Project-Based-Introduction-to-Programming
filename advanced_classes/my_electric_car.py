# from car import ElectricCar , Car
# Above & below code do the same
# import car
# from car import *
# """
# The above * approach is not recommended bcz it can lead to confusion
# with the same name in the file which is hard to diagnose.
# """

# """Making an Electric car"""
# tesla = ElectricCar('Tesla','model s', 2022)
# print(tesla.get_descriptive_name())
# tesla.fuel_tank()

# """Making simple Car run on CNG"""
# suzuki = Car('Suzuki','Ravi',2021)
# print(suzuki.get_descriptive_name())
# suzuki.fuel_tank()


# 🚒🚒🚒🚒 Try it yourself 🚒🚒🚒🚒
"""
9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module.
Make a separate file that imports Restaurant. Make a Restaurant instance, and call one
of Restaurant’s methods to show that the import statement is working properly.
"""
# from restaurant import Restaurant
# Restaurant.describe_restaurant(self=Restaurant(cuisine_type='portuguese',flavors=['banana','mango'],restaurant_name='Tory kababi'))

# 🚒🚒🚒🚒 Try it yourself 🚒🚒🚒🚒
"""
9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173). Store the
classes User, Privileges, and Admin in one module. Create a separate file, make an
Admin instance, and call show_privileges() to show that everything is working
correctly
"""

# from restaurant import Admin
# admin_prvileges = Admin(privileges=['create','update','delete','rename'])
# admin_prvileges.show_privileges()


# 🚒🚒🚒🚒 Try it yourself 🚒🚒🚒🚒

"""
9-13. Dice: Make a class Die with one attribute called sides, which has a default value of
6. Write a method called roll_die() that prints a random number between 1 and the
number of sides the die has. Make a 6-sided die and roll it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""

# import random
# class Die: 
#     def __init__(self):
#         self.sides = 6

#     def roll_die(self):
#         i=1
#         random.seed(42)
#         while i!=10:
#             i +=1
#             print(random.randint(1,6)) 
    
# die = Die()
# die.roll_die()


# 🚒🚒🚒🚒 Try it yourself 🚒🚒🚒🚒
"""
9-14. Lottery: Make a list or tuple containing a series of 10 numbers and five letters.
Randomly select four numbers or letters from the list and print a message saying that any
ticket matching these four numbers or letters wins a prize.

"""

# from random import choice, random


# possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

# winners = []

# for winner in range(5):
#     if winner not in winners:
#         winners.append(choice(possibilities))

# for winner in winners:
#     print(f'Ticket no : {winner} have won the prize.')




# 🚒🚒🚒🚒 Try it yourself 🚒🚒🚒🚒
"""
Lottery Analysis: You can use a loop to see how hard it might be to
win the kind of lottery you just modeled. Make a list or tuple
called my_ticket. Write a loop that
"""

from random import choice

def get_winning_ticket(possibilities):
    """Return a winning ticket from a set of possibilities."""
    winning_ticket = []

    # We don't want to repeat winning numbers or letters, so we'll use a
    #   while loop.
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)

        # Only add the pulled item to the winning ticket if it hasn't
        #   already been pulled.
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    # Check all elements in the played ticket. If any are not in the 
    #   winning ticket, return False.
    for element in played_ticket:
        if element not in winning_ticket:
            return False

    # We must have a winning ticket!
    return True

def make_random_ticket(possibilities):
    """Return a random ticket from a set of possibilities."""
    ticket = []
    # We don't want to repeat numbers or letters, so we'll use a while loop.
    while len(ticket) < 4:
        pulled_item = choice(possibilities)

        # Only add the pulled item to the ticket if it hasn't already
        #   been pulled.
        if pulled_item not in ticket:
            ticket.append(pulled_item)

    return ticket


possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_ticket(possibilities)

plays = 0
won = False

# Let's set a max number of tries, in case this takes forever!
max_tries = 1_000_000

while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")




