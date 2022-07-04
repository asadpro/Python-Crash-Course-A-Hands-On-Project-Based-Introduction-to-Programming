# # 🍟🍟 Looping Through an Entire List
# magicians = ['alice', 'david', 'carolina']

# for magician in magicians:
#     print(magician)

# # To create a list of numbers using range function.
# # When we wrap a range function with list call then every number that return out from that range 
# # function will be convert into list.
# numbers = list(range(1,30,3))
# print(numbers)
# even = list(range(2,11,2))
# odd = list(range(0,10,3))
# print('Even numbers: ',even)
# print('Odd numbers: ',odd)

# # 🍟🍟Make a list of 10 square numbers using range function.
# squares = []
# for value in range(1,11):
#     square = value ** 2
#     squares.append(square)
# print(squares)

# print("Minimum is: ",min(squares))
# print("Maximum is: ",max(squares))
# print("Sum of list is: ",sum(squares))

# # 🍟🍟 List Comprehensions

# list_comprehension = [ value ** 2 for value in range(1,11)]
# print("list comprehension example: ", list_comprehension)

#🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌

# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
# for number in range(1,21):
#     print(number)

"""
4-5. Summing a Million: Make a list of the numbers from one to one million, and then
use min() and max() to make sure your list actually starts at one and ends at one million.
Also, use the sum() function to see how quickly Python can add a million numbers.

"""
# million_numbers = [number for number in range(1,10**6+1)]
# print("Minimum is: ",min(million_numbers))
# print("Maximum is: ",max(million_numbers))
# print("Sum of list is: ",sum(million_numbers))

"""
4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the
numbers in your list.

"""
# multiples = [number for number in range(3,33,3)]
# print("List of multiples of 3: ",multiples)

# """
# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10
# cubes.
# """
# cube = [cube **3 for cube in range(1,10)]
# print("List of cube using comprehension: ",cube)

# 🍟🍟 Slicing a List
""" To make a slice in a list we need to specify the first index and the last
index of the element who you want to work with e.g. from the following list we want to print the first 
3 element of the list.
"""
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# for winner in players[0:len(players):2]:
#     print('Congragulation you have won the 🏆: ',winner)

# To print the last three of the elements
# for new_commer in players[-3:]:
#     print(new_commer)
#🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌

"""
Copying one list into other using slices
"""
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]
# print("My favorite foods are:")
# my_foods.insert(0,"Burger")
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friend_foods)
#🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌

"""
Copying one list into other using copy method.
"""
# my_favourite = ['Chilli','egg','sauce']
# your_favourite = my_favourite.copy()
# print("My favorite foods are:")
# print(my_favourite)
# print("Your favorite foods are:")
# my_favourite.insert(0,"Hot dog")
# print(your_favourite)
# print('After changing to my_favourite list: ')
# print(my_favourite)

#🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌

# my_foods = ['pizza', 'falafel', 'carrot cake']
# # This doesn't work:
# friend_foods = my_foods
 
# # This will work
# friend_foods = my_foods.copy()

# my_foods.append('cannoli')
# friend_foods.append('ice cream')
# print("My favorite foods are:")
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friend_foods)

#🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌

"""
Print the message 'The first three items in the list are:'. Then use
a slice to print the first three items from that program’s list.

"""
# squares = [value ** 2 for value in range(2,10)]
# print(squares)
# print("The first three items in the list are: ",squares[-3:])


#🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌🙌

"""
Print the message 'Three items from the middle of the list are:'.
Use a slice to print three items from the middle of the list.
"""

middle = [number for number in range(1, 31)]
average_of_list = round(sum(middle)/len(middle))
three_items = middle[average_of_list:]

print("Three items from the middle of the list are: ",three_items[0:3])

"""
Print the message 'The last three items in the list are:'. Use a slice
to print the last three items in the list.
"""
print("The last three items in the list are: ",three_items[-3:])
