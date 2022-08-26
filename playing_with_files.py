# Creating table from 2-20 and then save them to a separate .txt. file
# tables = [tab for tab in range(2,21)]

# def make_table(table_no):
#     store = ''
#     for j in range(1,11):
#         store += f'{table_no} x {j} = {table_no*j}\n'
#     store += '\n########################################## \n'
#     return store

# for table in tables:
#     save_table = make_table(table)
#     with open('tables.txt', 'a') as file:
#         file.write(save_table)

# with open('tables.txt', 'r') as read_file:
#     see_tables = read_file.read()
#     print(see_tables)


# 🌎🌎🌎🌎🌎 A file contain 'donkey' replace it with ###### in the same file. 🌎🌎🌎🌎🌎


# file = open('abusive_words.txt', 'r')
# rd = file.read()
# file.close()

# if "donkey" in rd:
#     with open('abusive_words.txt', 'w') as file:
#         file.write(rd.replace('donkey','#####'))


# file = open('abusive_words.txt', 'r')
# print(file.read())
# file.close()


# 🌎🌎🌎🌎🌎 Mine a log file and print out whether it contain 'python' or not. if yes then find it's line no 🌎🌎🌎🌎🌎
# content = True
# line_numbers = []
# counter = 0
# i = 0
# with open("log.txt", "r") as read_log:
#     while content:
#         i += 1
#         content = read_log.readline()
#         if "python" in content:
#             line_numbers.append(i)
#             counter +=1

#     print(f'Python words exist in file {counter} times.')
#     for line in line_numbers:
#         print('Python on line no: ',line)


# 🌎🌎🌎🌎🌎 Copy one file content into other file and check whether content of both are identical or not. 🌎🌎🌎🌎🌎

# with open('abusive_words.txt', 'r') as read_file:
#     content = read_file.read()

# # Copying of one file content into other.
# with open('abusive_words_duplicate.txt' , 'w') as write_file:
#     write_file.write(content)

# # To check whether both are identical or not.
# with open('abusive_words.txt','r') as file1:
#     file1.read()
# with open('abusive_words_duplicate.txt','r') as file2:
#     file2.read()

# print(file1 == file2)

# 🌎🌎🌎🌎🌎 Write a program to wipe out the content of a file. 🌎🌎🌎🌎🌎
# with open('abusive_words.txt', 'w') as write_file:
#     write_file.write('')
# with open('abusive_words.txt', 'r') as read_file:
#     content = read_file.read()
#     if content == '':
#         print('Content of the file is empty.')
#     else:
#         print("File is full of content")

# class Car:
#     def __init__(self):
#         self.name = 'asad'

#     def info(self):
#         return 'Name of the employee: ',self.name

#     # Creating a static method will not give error of 'self' keyword
#     @staticmethod
#     def great():
#         print('You are great ')

# car = Car()

# list_of_strings = ["This is my first file\n", "This file\n", "contains three lines\n"]
# pi_string = ""
# with open("pi_digit.txt", "r") as file_object:
#     lines = file_object.read()
#     print(file_object.tell())
#     for line in lines:
#         pi_string += line.rstrip()

# print(pi_string)

# 🐱‍👤🐱‍👤🐱‍👤🐱‍👤🐱‍👤🐱‍👤🐱‍👤🐱‍👤🐱‍👤🐱‍👤🐱‍👤🐱‍👤🐱‍👤🐱‍👤🐱‍👤🐱‍👤🐱‍👤

# str = 'hello python'
# print(str.find('py'))
# pi_string = ''
# birthday = input('Enter your birthday in the form of mmddyy: ')
# with open('pi_million_digits.txt','r') as file_object:
#     lines = file_object.readlines()
#     for line in lines[:100]:
#         pi_string +=line
#     if birthday in pi_string:
#        print("Your birthday appears in the first million digits of pi!")
#     else:
#        print("Your birthday does not appear in the first million digits of pi.")
# print(pi_string)

# 💖💖💖💖💖💖💖💖💖💖💖💖💖💖
""" 
Learning Python: Open a blank file in your text editor and write a few lines
summarizing what you've learned about Python so far. Start each line with the phrase In
Python you can. . .. Save the file as learning_python.txt in the same directory as your
exercises from this chapter. 

💕Write a program that reads the file and prints what you wrote three times. 
💕Print the contents once by reading in the entire file, 
💕Once by looping over the file object, 
💕Once by storing the lines in a list and then working with them outside the with block.
"""
# Task one completed 😎
# with open("learning_python.txt", "r") as file_read:
#     content = file_read.read()
#     for i in range(1, 4):
#         print("\n", str(i).center(30, "😎"), "\n")
#         print(content)

# Task Two completed
# with open("learning_python.txt", "r") as file_object:
#     entire_file = file_object.read()

#     # printing the entire file in one go.
#     print(entire_file)

# # Task Three completed
# print(" Next Line start ".center(34, "👀"))
# with open("learning_python.txt", "r") as file_loop:
#     looping_file = file_loop.readlines()
#     # Printing through looping everyline
#     for line in looping_file:
#         print(line, end="")

# # Task Four completed
# file_list = []

# with open("learning_python.txt", "r") as reader:
#     print("\n\n")
#     print("Operation with list".center(34, "🎶"))
#     file_list.append(reader.readlines())

# for item in file_list[0]:
#     print(item)

"""
Replace all words "Python" with "Python 3" using file operations.
"""

# with open("learning_python.txt", "r") as file_read:
#     content = file_read.read()
#     if "python" in content:
#         with open("learning_python.txt", "w") as file_write:
#             # filecontent.replace("Python", "Python 3")
#             file_write.write(content.replace("python", ' "Python 3"'))

# with open("learning_python.txt", "r") as file_change:
#     content = file_change.read()
#     print(content)

# 🎑🎑🎑🎑🎑🎑🎑🎑🎑🎑🎑🎑🎑🎑🎑🎑🎑🎑🎑🎑🎑🎑
# Creating a file and writing into it.
# with open("programming.txt", "w+") as file_object:
#     file_object.write("I love Programming.\n")
#     file_object.write("Coding is like magic.\n")
#     file_object.write("If you know how to write code then you are superhuman.\n")
#     # This seek method will move the file pointer to the start. It's more like cursor(handler) which is used to point the start of the file.
#     # This seek will define from where in the file the data has to read or write onto it.
#     # The first twenty will omit the first 20 characters from the file
#     # file_object.seek(20,0)
#     file_object.seek(0, 0)
#     content = file_object.read()
#     print(content)


# 🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀 Try it yourself 🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀
#  Guest: Write a program that prompts the user for their name. When they
# respond, write their name to a file called guest.txt.
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# address = input("Enter your address: ")

# with open("guest.txt", "w") as file_object:
#     file_object.write(f"Your name is : {name}\n")
#     file_object.write(f"Your age is : {age}\n")
#     file_object.write(f"Your address is : {address}\n")


# with open("guest.txt", "r") as file_reader:
#     content = file_reader.read()
#     print(content)


# 🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀
"""
Guest Book: Write a while loop that prompts users for their name. When they
enter their name, print a greeting to the screen and add a line recording their visit in a
file called guest_book.txt. Make sure each entry appears on a new line in the file.
"""
# should_continue = True

# while should_continue:
#     name = input("Enter your name: ")
#     designation = input("Enter your designation of Visit: ")

#     with open("guest_book.txt", "+a") as file_object:
#         file_object.write(f"Your name is : {name}\n")
#         file_object.write(f"Your designation is : {designation}\n")
#         file_object.write("\n==============================\n")
#         print(f"Hello Mr/Mrs: {name}")
# response = input(
#     "Do you want to continue to insert visiter in guest book Y/N: "
# ).lower()
# if response == "n":
#     should_continue = False

# 🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀
"""
Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file that stores
all the responses.
"""
# should_continue = True

# while should_continue:

#     poll = input("Why do you like programming?: ")
#     with open("responses.txt", "+a") as writer:
#         writer.write(f"\n{poll}\n")

#     response = input("Do you want to continue?  Y/N: ").lower()
#     if response == "n":
#         should_continue = False


# with open("responses.txt", "r") as reader:
#     content = reader.read()
#     print(content)
