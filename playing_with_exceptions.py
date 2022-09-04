# catching error of zero division.
# try:
#     # Will cause zero division error
#     print(5 / 0)
# except ZeroDivisionError:
#     print("Zero cannot divide any number.")

# finally:
#     print("Hello this finally clause.")

# 🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭

# filename = "alice.txt"
# try:
#     with open(filename, encoding="utf-8") as f:
#         contents = f.read()

# except ZeroDivisionError:
#     print("I put this exception to check whether we can run multiple exption or not.")

# except FileNotFoundError:
#     print(f"We don't have {filename} file in current directory.")


# # 🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭
# import requests

# book1 = requests.get("https://gutenberg.org/files/1250/1250-0.txt")
# book2 = requests.get("https://www.gutenberg.org/files/51244/51244-0.txt")
# book3 = requests.get("https://www.gutenberg.org/cache/epub/26167/pg26167.txt")
# book4 = requests.get("https://www.gutenberg.org/cache/epub/26354/pg26354.txt")
# book5 = requests.get("/epub/26354/pg26354.txt")

# book_shelf = {
#     "alice.txt": book1,
#     "siddhartha.txt": book2,
#     "moby_dick.txt": book3,
#     "little_women.txt": book4,
#     "empty.txt": book5,
# }


# def count_words(filename, filetext):
#     """Count the approximate number of words in a file."""
#     try:
#         with open(filename, encoding="utf-8", mode="w") as filewrite:
#             filewrite.write(filetext)

#     except FileNotFoundError:
#         print(f"Sorry, the file {filename} does not exist.")

#     else:
#         with open(filename, encoding="utf-8", mode="r") as f:
#             contents = f.read()
#         words = contents.split()
#         num_words = len(words)
#         print(f"The file {filename} has about {num_words} words.")


# for name, content in book_shelf.items():
#     count_words(name, content.text)

# 🎃🎃🎃🎃🎃🎃🎃🎃🎃 TRY IT YOURSELF 🎃🎃🎃🎃🎃🎃🎃🎃🎃🎃🎃
"""
Addition: One common problem when prompting for numerical input occurs
when people provide text instead of numbers. When you try to convert the input to an
int, you'll get a ValueError. Write a program that prompts for two numbers. Add them
together and print the result. Catch the ValueError if either input value is not a number,
and print a friendly error message. Test your program by entering two numbers and then
by entering some text instead of a number.
"""

# try:
#     num1 = int(input("Enter num1: "))
#     num2 = int(input("Enter num2: "))
#     result = num1 + num2
# except ValueError:
#     print(
#         "Numbers you are trying to add is not integer please do rectification first. "
#     )

# 🎃🎃🎃🎃🎃🎃🎃🎃🎃 TRY IT YOURSELF 🎃🎃🎃🎃🎃🎃🎃🎃🎃🎃🎃
"""
Addition Calculator: Wrap your code from Exercise 10-6 in a while loop so the
user can continue entering numbers even if they make a mistake and enter text instead of
a number.
"""
# while True:
#     try:
#         num1 = int(input("Enter num1: "))
#         num2 = int(input("Enter num2: "))
#         print(f"Result is: {num1 + num2}")
#     except ValueError:
#         print(
#             "Numbers you are trying to add is not integer please do rectification first. "
#         )

# 🎃🎃🎃🎃🎃🎃🎃🎃🎃 TRY IT YOURSELF 🎃🎃🎃🎃🎃🎃🎃🎃🎃🎃🎃
"""
Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three names of
cats in the first file and three names of dogs in the second file. Write a program that tries
to read these files and print the contents of the file to the screen. Wrap your code in a
try-except block to catch the FileNotFound error, and print a friendly message if a file
is missing. Move one of the files to a different location on your system, and make sure
the code in the except block executes properly.
"""

# with open("cat.txt", "w") as cat_object:
#     cat_object.write("fluffy cat \n")
#     cat_object.write("Bunjy cat \n")
#     cat_object.write("Ugda cat \n")

# with open("dog.txt", "w") as dog_object:
#     dog_object.write("fluffy dog \n")
#     dog_object.write("Bunjy dog \n")
#     dog_object.write("Ugda dog \n")

# try:
#     with open("/cat.txt", "r") as cat_file:
#         content = cat_file.read()
# except FileNotFoundError:
#     print("The file you are looking for not found.")

# 🎃🎃🎃🎃🎃🎃🎃🎃🎃 TRY IT YOURSELF 🎃🎃🎃🎃🎃🎃🎃🎃🎃🎃🎃
"""
Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail silently
if either file is missing.
"""
# try:
#     with open("/cat.txt", "r") as cat_file:
#         content = cat_file.read()
# # The pass keyword will fail silently without notifying the user.
# except FileNotFoundError:
#     pass

# 🎃🎃🎃🎃🎃🎃🎃🎃🎃 TRY IT YOURSELF 🎃🎃🎃🎃🎃🎃🎃🎃🎃🎃🎃
"""
Common Words: Visit Project Gutenberg (https://gutenberg.org/) and find a few
texts you'd like to analyze. Download the text files for these works, or copy the raw text
from your browser into a text file on your computer.
You can use the count() method to find out how many times a word or phrase appears
in a string. 
"""
# import requests

# book_object = requests.get("https://gutenberg.org/cache/epub/68847/pg68847.txt")
# book_text = book_object.text
# # The count method will also count then there they so we add spaces to it to find only 'the' in text-book.
# counter = book_text.count(
#     "the ",
# )
# print(counter)

# 🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨

# We can store json file like we did with general .txt with open method
# We have to method of storing and retreiving json file json.dump() and json.load()

# import json

# json_dict = {
#     "name": "asad",
#     "father_name": "habib",
#     "address": "Dalazak road",
#     "Phone_no": "+09216794",
#     "habit": "calisthenics",
# }

# with open("profile.json", "w") as file_object:
#     json.dump(json_dict, file_object)

# with open("profile.json", "r") as file_read:
#     content = json.load(file_read)
#     for key, value in content.items():
#         print(key, " : ", value)


# 🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨🎨
# import json

# We have define the greet user function to call it once every


# def greet_user():
#     try:
#         with open("username.json") as file_obj:
#             username = json.load(file_obj)

#     except FileNotFoundError:
#         person_names = []
#         # this loop will ask the user to enter 5 name and then store them in a json file for latter.
#         for i in range(5):
#             username = input("What's your name? ")
#             person_names.append(username)

#         with open("username.json", "w") as filewrite:
#             json.dump(person_names, filewrite)
#             print(f"We'll remember all of you when you come back, {person_names}!")
#     else:
#         print(f"Welcome back,!{username}")

# greet_user()

# 🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒

"""
Favorite Number: Write a program that prompts for the user's favorite number.
Use json.dump() to store this number in a file. Write a separate program that reads in
this value and prints the message, “I know your favorite number! It's _____.”
"""
# import json


# def store_number():

#     fav_no = int(input("What's your favourite no: ______ : "))

#     with open("favouriteNo.json", "w") as f:
#         json.dump(fav_no, f)


# def read_number():

#     with open("favouriteNo.json") as f_read:
#         number = json.load(f_read)
#         print(f"I know your favorite number! It's {number}.")


# store_number()
# read_number()

# 🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒

"""
Favorite Number Remembered: Combine the two programs from Exercise 10-
11 into one file. If the number is already stored, report the favorite number to the user. If
not, prompt for the user's favorite number and store it in a file. Run the program twice to
see that it works.
"""
# import json


# def favNumber():
#     try:
#         with open("fav_no.json") as f:
#             number = json.load(f)
#             print("Your favourite number is: ", number)
#     except FileNotFoundError:
#         fav_num = int(input("Enter your favourite number: "))
#         with open("fav_no.json", "w") as f:
#             json.dump(fav_num, f)


# favNumber()


# 🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒🎒
"""
Verify User: The final listing for remember_me.py assumes either that the user has
already entered their username or that the program is running for the first time. We
should modify it in case the current user is not the person who last used the program.
Before printing a welcome back message in greet_user(), ask the user if this is the
correct username. If it's not, call get_new_username() to get the correct username.
"""
# import json


# def get_store_user():
#     """Return username if store in record."""
#     try:
#         filename = "remember.json"
#         with open(filename, "r") as f:
#             username = json.load(f)

#     except FileNotFoundError:
#         return None

#     else:
#         return username


# def get_new_user():
#     """Create new user if not in database."""
#     user = input("Enter your name: ")
#     filename = "remember.json"
#     with open(filename, "w") as f:
#         json.dump(user, f)

#     return user


# def great_user():
#     username = get_store_user()

#     if username:
#         correct = input(f"Are you {username}? Y/N").lower()
#         if correct == "y":
#             print(f"Welcom back, " + username)
#         else:
#             username = get_new_user()
#             print("We will remember you when you come back, ", username)

#     else:
#         username = get_new_user()
#         print("We will remember you when you come back, ", username)


# great_user()
