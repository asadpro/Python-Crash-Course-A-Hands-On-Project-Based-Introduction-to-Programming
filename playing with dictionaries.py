# 🍟🍟 Accessing Values in a Dictionary
# we can access value of the dictionary using their keys

# favorite_languages = {
#     "jen": "python",
#     "sarah": "c",
#     "edward": "ruby",
#     "phil": "python",
# }

# print(f"Favourite language of phil is: ",favorite_languages["phil"])


# 🍟🍟 Adding New Key-Value Pairs to the Dictionary
# favorite_languages['asad']=['python','javascript']
# print(favorite_languages)

# 🍟🍟 Modifying Values in a Dictionary
# language_to_change = input('Enter the name of the language do you want to change?: ')
# new_language = input('Enter the new language name?: ')
# if language_to_change in favorite_languages["asad"]:
#     index = favorite_languages["asad"].index(language_to_change)
#     favorite_languages["asad"].insert(index,new_language)
# print(favorite_languages)

# 🍟🍟 Removing Key-Value Pairs in a Dictionary
# print("Before deletion: ",favorite_languages)
# del favorite_languages["edward"]
# print("After deletion: ",favorite_languages)


# 🍟🍟 Using get() to Access Values in a Dictionary
# if you want to access value of a key & it doesn't exist there then using get() method will
# prevent you falling into pitfall of errors e.g.
# for key in favorite_languages:
#     print(f"{key} : {favorite_languages[key]}")
# print(favorite_languages.get("Sarah", "Key is not in the dictionary sorry!!\n"))

# 🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟
"""
Think of five programming words you’ve learned about in the
previous chapters. Use these words as the keys in your
glossary, and store their meanings as values.
"""
# print("🍟🍟🍟 Printing dictionary in a beautiful order: 🍟🍟🍟\n")
# eng_to_urdu = {
#     "python": "Samp",
#     "function": "To do something",
#     "loop": "To act upon something again & again",
#     "if_statement": "conditional statements",
# }

# Print a dictionary line by line using for loop & dict.items()

# for key, value in eng_to_urdu.items():
#     print(key ," : ", value )


# print("🍟🍟🍟 Printing dictionary in sorted order: 🍟🍟🍟\n")
"""
Looping Through a Dictionary’s Keys in a Particular
Order
"""
# print('Unsorted order of dictionary')
# for keys in eng_to_urdu:
#     print(keys)

# We can use the sorted() method which takes an iterable as an argument.
# print('\nSorted order of dictionary')
# sorting = []
# for keys in sorted(eng_to_urdu):
#     {
#         print(keys)
#     }

# 🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟
# print("🍟🍟🍟 Looping Through All Values in a Dictionary: 🍟🍟🍟\n")

# alphabets = {
#     0: "a",
#     1: "b",
#     2: "c",
#     3: "d",
# }
# for key, value in alphabets.items():
#     print(key, " : ", value)
# print("\nValues of the above dictionaries: \n")
# for value in alphabets.values():
#     print(value)


# when you wrap a list that contain duplicate value inside set() method then this method will
# return only the unique values inside that list.
# duplicate_values = [11, 12, 13, 13, 14, 11, 15, 16, 16, 17, 18, 17, 18]
# print("Duplicated value exist: ", duplicate_values)

# unique_list = set(duplicate_values)
# print("Unique list: ", unique_list)

print("\n🍟🍟🍟 Sets in python: 🍟🍟🍟\n")
# Sets contain only unique values. Defining a set is more like defining dictionary but if 
# you see dictionary without key-value pair then you're probably seeing the sets.

set1 = {'asad','asad','bilal','salim'} # if you put the same value again then it will return only the single occurence of that value.
print(set1)

for set_value in set1:
    if set_value.endswith('d'):
        print(True)

set1.update(['sadiq','farooq','rehan','bahar'])
print(set1)
# See the common values b/w both sets
A = {2, 3, 5}
B = {1, 3, 5}

common = A.intersection(B)
print('Common values in both A & B: ',common)