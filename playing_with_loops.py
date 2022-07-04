# prints only odd number using continue statement
# the following continue keyword will ignore that numbers which are divisible by 2
# for number in range(0,11):
#     if number%2==0:
#         continue
#     else: 
#         print(number)

# 🍟🍟Pizza topping challenge🍟🍟
"""
Pizza Toppings: Write a loop that prompts the user to enter a series of pizza
toppings until they enter a 'quit' value. As they enter each topping, print a message
saying you’ll add that topping to their pizza.

"""
# quiting = ''
# pizza = []
# while pizza != 'quit':
#     pizza.append(input('Enter pizza name: '))
#     if pizza[-1] == 'quit':
#         break
# print(pizza[0:-1])

# 🍟🍟Movie tickets challenge🍟🍟
"""

Movie Tickets: A movie theater charges different ticket prices depending on a
person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and
12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which
you ask users their age, and then tell them the cost of their movie ticket.
"""

# ticket_cost = ''
# flag = False
# while not flag:
#     age = int(input('What is your age?: '))
#     if age == 'quit' or type(age)!=int:
#         break
#     elif age <3:
#         ticket_cost = 'free'
#         print("You have to pay: ",ticket_cost)

#     elif age>=3 and age<12:
#         ticket_cost = '$10'
#         print("You have to pay: ",ticket_cost)

#     elif age>=12:
#         ticket_cost = '$15'
#         print("You have to pay: ",ticket_cost)

# 🍟🍟Try & exception method in python🍟🍟

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")

# Moving Items from One List to Another
# unconfirmed_users = ['asad','saqib','hamza','usman']
# confirmed_users = []
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print('Verifying user: ',current_user.title())
#     confirmed_users.append(current_user)
# print('unconfirmed_users: ',unconfirmed_users)
# print("Confirmed users: ",confirmed_users)

# 🍟🍟Remove all instances of cat from the list🍟🍟
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)


# 🍟🍟sandwitch order list challenge🍟🍟
"""
Deli: Make a list called sandwich_orders and fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop through the
list of sandwich orders and print a message for each order, such as I made your tuna
sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all
the sandwiches have been made, print a message listing each sandwich that was made.
"""

sandwich_orders = ['sandwitch_1','sandwitch_2','sandwitch_3','sandwitch_4']
# finished_sandwiches = []

# for sandwitch in sandwich_orders:
#     print(f'I made your {sandwitch} sandwich ')
#     finished_sandwiches.append(sandwitch)
# print('All the made sandwitches are:\n',finished_sandwiches)


# 🍟🍟Remove all instances of pastrami from the list🍟🍟

"""
 No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the
sandwich 'pastrami' appears in the list at least three times. Add code near the beginning
of your program to print a message saying the deli has run out of pastrami, and then use
a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make
sure no pastrami sandwiches end up in finished_sandwiches.
"""
# sandwich_orders = ['pastrami','sandwitch_2','pastrami','sandwitch_4','pastrami']
# print('Deli has run out of pastrami.')
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# print('Sandwitch list: ',sandwich_orders)

