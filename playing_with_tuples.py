# 🍟🍟 Here parenthesis is used for neatness purpose if you just write down the numbers with trailing comma then it won't cause any issue and will
# and will consider it as 'tuple'
# tuples = 2,3,4,5,2,2,2,9
# print(type(tuples))

# list and tuples are the same but tuple are immutables.
# We can access tuple as we do with list
# print(tuples[0])

# return the no of occurrnces of 2 in a list

# number = tuples.count(2)
# print(number)

# 🍟🍟 Looping Through All Values in a Tuple
# recipes = ('chips','noodles','samosa','pakory')
# recipe_list = []
# for recipe in recipes:
#     recipe_list.append(recipe)

# print(recipe_list)

# 🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌
# new_recipe_list = []
# count = int(input('How many dishes you want to add? '))
# while count!=0:
#     new_recipe_list.append(input(f'Add recipe to the list: {count}=> '))
#     count-=1
# print(new_recipe_list)
# new_tuple = tuple(new_recipe_list)
# change = input('Do you want to change the menu list? "y" for yes & "n" for no: ').lower()
# element = input('Which recipe do you want to change?')
# replace_recipe = input('Enter the name of the new recipe? ')
# if change == 'y' and element in new_tuple:
#     change_tuple = list(new_tuple)
#     for recipe in change_tuple:
#         if recipe == element:
#             change_tuple[change_tuple.index(recipe)] = replace_recipe
#     new_tuple = tuple(change_tuple)
# print("Changed recipe: ",change_tuple)

# 🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌
# tuply = ('chips','noodles','samosa','pakory')
# single_string = " ".join(tuply)
# print(single_string)

# 💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡

# Python list exercises
# Exercise 1: Write a program to create a list with random data types elements.
# num = [22,'PythonLobby',22.3]
# datype = []
# for i in num:
#     datype.append(type(i))
# print(datype)

# Exercise 2: Write a program to print all the elements of a list in single line.
# num = [23,24,54,34]
# for i in range(len(num)):
#     print(num[i], end=' ')

# Exercise 3: Write a program to count the number of items stored in a list.
# num = [23, 34, "hello", 32, 56]
# print('\nNo of item in a list: ',len(num))

# Exercise 4: Write a program to reverse a list in Python.
# num = [23, 34, "hello", 32, 56]
# num.reverse()
# print(num)

# Exercise 5: Python program to square each element of a list.
# x = [2, 3, 4, 5, 6]
# for num in x:
#     print(num**2, end=" ")

# Exercise 6: Python program to remove an empty element from a list.
# num = ["Hello", 34, 45, "", 40]
# while "" in num:
#     num.remove("")
# print("\nEmpty element has been removed: ",num)

# Exercise 8: Write a program to display those items from a list that is divisible by 5.
# num = [3, 5, 7, 9, 23, 15]
# new_num = []
# for num in num:
#     if num%5 ==0:
#         new_num.append(num)
# print(new_num)

# Exercise 10: Write a program in Python to remove duplicate items from a list.

# num = [2,3,4,5,2,6,3,2]
# navality = []
# for i in range(len(num)):
#     if num[i] not in navality:
#         navality.append(num[i])
#     else:
#         pass
# print(navality)

# Exercise 11: Write a program in Python to choose a random item from a list.
# import random
# num = [2,3,4,5,6,8,9]
# randomNumber = random.choice(num)
# print(randomNumber)

# Exercise 12: Write a program to append data of the second list to the first list
# list1, list2= [23, 24, 25, 26],[27, 28, 29, 30]
# list1.extend(list2)
# print(list1)


# Exercise 13: Write a program in Python to filter odd and even number from a list.
numbers = [2, 23, 24, 51, 46, 67]
Even = []
Odd = []

for num in numbers:
    if num%2==0:
        Even.append(num)
    else:
        Odd.append(num)
print('Even numbers: ',Even)
print('Odd numbers: ',Odd)
