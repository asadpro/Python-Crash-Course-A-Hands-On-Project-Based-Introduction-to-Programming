# import unittest


# def get_formatted_name(fname, lname):
#     """Generate a neat full name"""
#     return f"{fname} {lname}".title()


# print("Enter 'q' at any time to quit.")

# first = input("Enter firstname: ").lower()
# if first == "q":
#     exit(0)
# last = input("Enter lastname: ").lower()
# if last == "q":
#     exit(0)

# formatted_name = get_formatted_name(fname=first, lname=last)


# # Creating a testCase class inherits from unitest module.
# class Testing(unittest.TestCase):
#     def test_first_last_name(self):
#         format_name = get_formatted_name("asad", "khan")
#         self.assertEqual(format_name, "Asad Khan")


# if __name__ == "__main__":
#     unittest.main()

# 🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫

a = 10
b = 10
# Below code will give us same memory address because python allocate memory address
# according to the value of the variable which in this case is 10 for both
# print(id(a), id(b))
# print("\t", id(a) == id(b))
# print(16 / 3)  # 5.333333333333333

# print(16 // 3)  # 5


# Finding binary of a number
# print(bin(10))
# print(bin(8))

# 🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫🎫
# Tuple is like list but it can't be changed that's the basic difference b/w list and tuple.
t = 1  # python will set the type of t as int because it will look the value inside that parenthesis as we see earlier that python is dynamic semantics
# means python will define the type of variable by looking it's value.


t1 = (
    1,
)  # type of this variable is tuple because a tuple must have more than 1 value inside it.

# print(t, type(t))
# print(t1, type(t1))


# Print in reverse integer from 10 to 0 in reverse order using range function.
# for num in range(10, 0, -1):
#     print(num)

hos = "Hospotol chowk"  # string have double 'o' the first one have index of 1 so for the last 'o' the index will be 1 as well.
# for i in range(len(hos) - 1):
#     print(hos[i], " : ", hos.index(hos[i]))

# hos_new = ""
# for index in range(len(hos) - 1, -1, -1):
#     hos_new += hos[index]
# print("Without slicing technique.".center(62, "*"))
# print(hos)
# print(hos_new)
# with the help of slicing we can do the same as above mentioned solution with more optimal and short written code.
# print("Using slicing technique.".center(62, "*"))
# print(
#     hos[::-1]
# )  # this means to start from the end upto to start position of string. in reverse order print.

# 🎍🎍🎍🎍🎍🎍🎍🎍
# Slicing of string
# print(hos[0:7])

# find() ==> To check to position of a character in a string
# index() ==> To check the index of a character in a string
# isalpha() ==> To check whether a string contain only alphabet
# isalnum() ==> To check wheter a string contain both number & alphabets
# isdigit() ==> To check whether a string contain only integers.


# find method is used to find out the index no of character in a string.
# greet = "Hello python python"
# print(
#     greet.find("p")
# )  # This will return the position of p in python but the position of first "p" not second

# # Now let's find out the second p position in greet string by tweaking it.

# print(
#     greet.find("p", 7)
# )  # if it returns -1 this means it didn't find the position of p


# print(greet.index("o"))  # Index of 'o' in greet string

# alphaNumeric = "asad123"
# print(alphaNumeric.isalnum())


# number = '123455'
# print(number.isdigit())

# 🎍🎍🎍🎍🎍🎍🎍🎍🎍🎍🎍🎍🎍🎍🎍🎍🎍🎍🎍🎍🎍🎍🎍🎍
# We have two types of encoding used used mostly one is ASCII(0-256) & UNICODE(utf-8,utf-16,utf-32)


# uni = 97
# print(chr(uni))  # chr function return the character value of 97 which is a

# print(ord("a"))  # ord function returnue


# 👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒
# Below you will notice that size of character would be less than an emoji because emojis uses the unicode encoding scheme while character uses the ascii
# import sys

# asciiCode = sys.getsizeof("a")
# unicode = sys.getsizeof("👮")

# # Converting bytes to KB
# print(f"Size in bytes of 'a':", asciiCode)
# print(f"Size in bytes of '👮‍♂️':", unicode)

# 👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒

# first = "asad"
# last = "khan"

# # Name indexing
# print("{first_name} {last_name}".format(first_name=first, last_name=last))

# # Number indexing
# print("{0} {1}".format(first, last))

# # Empty placeholders
# print("{} {}".format(first, last))

# 👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒
# Printing list in reverse order.
# num = [i for i in range(1, 11)]

# print("Reverse using slice: ", num[-1::-1])
# Instead of using above we can use below as well.
# print(num[::-1])

# reversed_num = reversed(num)
# print("Reverse using reversed function: ", list(reversed_num))

# num.reverse()
# print("Reverse using function: ", num)

# 👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒

# l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# # Python list functions.
# print(l)

# # del   #del keyword doesn't return anything.
# del l[1]  # this will delete value on index 1
# print("Del used: ", l)


# pop() The only difference b/w del and pop is del not returning anything while pop return the deleted value.
# delete = l.pop(2)
# print("Deleted through pop method: ", delete)
# print("Pop used: ", l)

# # remove()
# removed = l.remove(50)
# print("Remove used: ", l)

# # clear()
# l.clear()
# print("List has been cleared: ", l)

# 👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒👨‍🚒
# Program to convert string into a list

# name = "asad"
# list_name = [ch for ch in name]
# print(list_name)

# string = input("Enter a sentence to convert it to list: ")
# print(string.split(" "))

# 👩‍🦰👩‍🦰👩‍🦰👩‍🦰👩‍🦰 Creating list using enumerate (شمار کرنا)
# list_enumerate = []

# for index, value in enumerate(name):
#     list_enumerate.append(value)

# print(list_enumerate)

# 🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅

# listing = ["asad", "waqas", "hamza", "saqib"]
# all_names_characters = []
# for numerate, value in enumerate(listing):
#     print(value)
#     for k, v in enumerate(value):
#         all_names_characters.append(v)

# print(all_names_characters)

# 🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅
# Stack in python and it's operations
# import os

# Stack work as LIFO (Last-in-First-Out)
# stack = []
# should_continue = True
# while should_continue:
#     try:
# reply = int(
#     input(
#         """
# 1: Push elements\b
# 2: Pop elements\b
# 3: Peek elements\b
# 4: Display elements\b
# 5: Exit\b
# 6: Clear console\n
# 👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻
# """
#     )
# )

#         if reply == 1:
#             value = input(
#                 "Enter value you want to push: if multiple then use comma => ',' :  "
#             )
#             new_value = value.split(",")
#             stack.extend(new_value)
#             print(stack)

#         elif reply == 2:
#             try:
#                 pop_value = stack.pop(-1)
#                 print(pop_value)
#                 print(stack)
#             except IndexError:
#                 print("List is empty please enter some values into it first.")

#         elif reply == 3:
#             print("Value of peek in stack: ", stack[-1])
#             print(stack)

#         elif reply == 4:
#             print("Displayed elements: {}".format(stack))

#         elif reply == 5:
#             exit(0)

#         elif reply == 6:
#             os.system("cls")

#         elif reply > 5:
#             pass

#     except ValueError:
#         print("Value error please enter some value first.")
#         pass

# 🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅🎅
# Queue in python and it's operations
# import os

# queue = []
# should_continue = True
# while should_continue:
#     try:
#         reply = int(
#             input(
#                 """
#             1: Enqueue elements\b
#             2: Dequeue elements\b
#             3: Front elements\b
#             4: Rear elements\b
#             5: Display elements\b
#             6: Exit\b
#             7: Clear console\n
#             👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻
#             """
#             )
#         )

#         if reply == 1:
#             value = input(
#                 "Enter value you want to Enqueue: if multiple then use comma => ',' :  "
#             )
#             new_value = value.split(",")
#             queue.extend(new_value)
#             print(queue)

#         elif reply == 2:
#             try:
#                 pop_value = queue.pop(0)
#                 print("Dequeued value: ",pop_value)
#                 print(queue)
#             except IndexError:
#                 print("List is empty please enter some values into it first.")

#         elif reply == 3:
#             print("Front value of queue: ", queue[0])
#             print(queue)

#         elif reply == 4:
#             print("Rear value of queue: ", queue[-1])
#             print(queue)

#         elif reply == 5:
#             print("Displayed elements: {}".format(queue))

#         elif reply == 6:
#             exit(0)

#         elif reply == 7:
#             os.system("cls")

#         elif reply > 8:
#             pass

#     except ValueError:
#         print("Value error please enter some value first.")
#         pass

# 🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩
# Dictionary function and usage
# my_dict = {
#     "name": "asad",
#     "fname": "habib",
#     "age": 26,
#     "address": "fattu",
# }

# # Getting keys only
# print(my_dict.keys())
# print(my_dict.values())

# # Getting both key value at the same time.
# for k, v in my_dict.items():
#     print(k, " : ", v)


# # Using fromkeys method of dictionary to create a new dictionary from keys

# print("Fromkey method".center(23, "*"))
# key = {"a", "e", "i", "o", "u"}

# dictionary = dict.fromkeys(key, "vowels")
# print(dictionary.values())

# # Update dictionary using update() method
# my_dict.update({"age": 24})  # Updating dictionary value of 26 to 24
# print(my_dict)

# # Clear dictionary
# print("Copy of dictionary".center(43, "🚍"))
# dict_copy = my_dict.copy()
# print(dict_copy)

# print("Memory address : ", id(my_dict), id(dict_copy))

# 🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚
# Nested dictionary
# people = {
#     1: {"name": "John", "age": "27", "sex": "Male"},
#     2: {"name": "Marie", "age": "22", "sex": "Female"},
#     3: {"name": "Luna", "age": "24", "sex": "Female", "married": "No"},
#     4: {"name": "Peter", "age": "29", "sex": "Male", "married": "Yes"},
# }
# # Printing all key value pairs in dictionary.
# # for k, v in people.items():
# #     print(k, v)

# # 🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎
# # Printing first nested dictionary in people dictionary.
# # for k, v in people[1].items():
# #     print(k, v)

# # 🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎
# # Print only names of every nested dictionary.
# valuesOfNames = []
# for i in range(1, 5):
#     valuesOfNames.append(people[i].get("name"))
#     print(valuesOfNames)

# # 🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎
# # Updating value age of first dictionary in people dictionary.
# print("Before updating age: ", people[1])
# people[1].update({"age": "20"})  # setting age from 27 to 20
# print("After updating age: ", people[1])

# 🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚🚚

import random

# randit = random.randint(1, 4)  # Include both 1 & 4
# range = random.randrange(1, 4)  # Include 1 but not 4
# print(randit, range)

# ⛵⛵⛵⛵⛵⛵⛵⛵ Using Uniform method ⛵⛵⛵⛵⛵⛵⛵⛵
# Uniform method return a floating number between two floating numbers.
# print(random.uniform(1.1, 1.2))

# ⛵⛵⛵⛵⛵⛵⛵⛵ Using shuffle method ⛵⛵⛵⛵⛵⛵⛵⛵

# l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print("Before shuffle: ", l)
# shuffle = random.shuffle(l)
# print("After shuffle: ", l)

# ⛵⛵⛵⛵⛵⛵⛵⛵ Using random.random() method ⛵⛵⛵⛵⛵⛵⛵⛵
# num = 0
# while num != 10:

#     randvalue = (
#         random.random()
#     )  # this module will return the floating value b/w 0,1 but not one less than 1
#     num += 1
#     print(round(randvalue, 2))

