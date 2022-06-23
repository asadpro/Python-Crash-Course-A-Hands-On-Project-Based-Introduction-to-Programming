# favorite_fruits = ['apple','banana','watermelon','peach','strawberry','apricot']

# if 'apple' in favorite_fruits:
#     print('Apple is in list')

# if 'banana' in favorite_fruits:
#     print('banana is in list')

# if 'apricot' in favorite_fruits:
#     print('apricot is in list')

# if 'peach' in favorite_fruits:
#     print('peach is in list')   

# username = ['admin','asad','salim','hamza','saqib']
# for user in username:
#     if user == 'admin':
#         print(f"Hello {user}, would you like to see a status report?")
#     else:
#         print(f'Hello {user}, thank you for logging in again.')

# 🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟

"""
5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or
2nd. Most ordinal numbers end in 'th', except 1, 2, and 3.

"""

# numbers = [number for number in range(1,11)]
# new_number = []
# for num in numbers:
#     if num == 1:
#         new_number.append(str(num)+'st')
#     elif num == 2:
#         new_number.append(str(num)+'nd')
#     elif num == 3:
#         new_number.append(str(num)+'rd')
#     else:
#         new_number.append(str(num)+"th")

# print(new_number)
# print(' '.join(new_number))

# 🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟
# alien_0 = {'color': 'green', 'points': 5}
# print("Old list of alien: ",alien_0)
# for alienKey in alien_0:
#     print(alienKey)
#     if alienKey == 'points':
#         alien_0['points']=10 #updating the dictionary

# 💡💡 If you don't need a piece of information in the dictionary then you can simply delete
# that information using the del key.
# del alien_0['color']
# print("Updation of the list: ",alien_0)

# 🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟
# Taking survey of programmer to ask for their favourite programming language. They can 
# choose more than 1 language and then store that all information into dicitonary.
terminate = False
languages = []
dictionary = {}
while not terminate:
    programmer = input('Name of the programmer: ')
    no_of_lang = int(input('How many languages do you want to enter?: '))

    while no_of_lang!=0:
        languages.append(input('What are your favourite programming languages?: '))
        no_of_lang-=1

    dictionary[programmer] = languages
    end_of_life = input('Do you want to exit? "y" or "n": ')
    if end_of_life == 'y':
        terminate = not terminate


print(dictionary)






