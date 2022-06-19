"""
2-1. Simple Message: Assign a message to a variable, and then print that message.
2-2. Simple Messages: Assign a message to a variable, and print that message. Then
change the value of the variable to a new message, and print the new message.

"""

message = 'Those who are not obey to the almighty allah will be punished at the day of judgment.'
print(message)

message = 'Muhammad (PBUH) said: "The one who are are good with their wives is the better muslim."'
print(message)

""" 
Below the name variable refers to the smaller case of 'ada lovelace' but when we call title() by placing the dot (.)
between name variable and title method basically the (.) tells the python to act on the variable.
"""
name = "ada lovelace"
print(name.title())

# 🍟 f-string in python is used for the purpose of string interpolation e.g. 
name = 'asadpro 3.1'
message = f"Hello, {name}" # we can use f-string for composing the string like this.
print(message)

"""
if you are using python before version 3.6 then we have to write it like below where  name and message variable will
be placed inside parenthesis in corresponding positions.
"""
full_name = "Before python 3.6 version: {} {}".format(name, message)
print(full_name)

# 🍟 Adding Whitespace to Strings with Tabs or Newlines
# Below i have add \t which refers to the tab equal to 4 spaces and newline
print("Languages:\n\tPython\n\tC\n\tJavaScript")

name1 = "asad" #apply rstrip()
name2 = "asad " #apply lstrip()
name3 = " asad " #apply strip()
# it will print false because name2 have the extra whitespace 
# to insure that no whitespace remain on the right side of the text
# use rstrip() method on that variable.
# To remove whitespaces from left side use lstrip() method
# and to remove all the whitespaces from text use strip().
print(name1 == name2) # False
print(name1 == name2.rstrip()) # True

"""
2-4. Name Cases: Use a variable to represent a person’s name, and then print that
person’s name in lowercase, uppercase, and title case.
"""
name = 'Eric davinchi'
print("Capitalize => ",name.capitalize(),"\nLower => ",name.lower(),"\nUpper => ",name.upper(),"\nTitle => ",name.title())

"""
2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote
and the name of its author. Your output should look something like the following,
including the quotation marks:
Albert Einstein once said, “A person who never made a mistake
never tried anything new.”

"""
author_name = "Albert Einstein"
quote = '“A person who never made a mistake never tried anything new.”'
quote = quote.rstrip()
print(author_name,"once said, ",quote)

"""
Print the name once, so the whitespace around the name is displayed. Then print the
name using each of the three stripping functions, lstrip(), rstrip(), and strip().

"""
famous_name = "a   Albert einstein    a"
print(famous_name.lstrip('a'))
print(famous_name.rstrip('a'))
print(famous_name.strip('a'))









