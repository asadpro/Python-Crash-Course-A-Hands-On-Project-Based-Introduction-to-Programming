
name = 'asadjani'
print(name.count('a')) # count no of occurrences of particular words

alphabet = ['a','b','c','d']
alphabet.extend(['e','f','g','h'])
print(alphabet)

# 🍟Sorting a list in ascending order use sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Before sorting list: ',cars)
cars.sort()
print('After sorting list: ',cars)
# By putting the reverse parameter this will make the list in descending order 
cars.sort(reverse=True) 
print('After descending order: ',cars)

# 🍟 But if you want sort list temporarily & doesn't want to effect your actual list then use sorted() function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Sorted list: ",sorted(cars))
print("Original list: ",cars)

# 🍟Printing a List in Reverse Order
alphabet.reverse()
print("Alphabets in reverse order: ",alphabet)

# 🍟Printing a List in Reverse Order






