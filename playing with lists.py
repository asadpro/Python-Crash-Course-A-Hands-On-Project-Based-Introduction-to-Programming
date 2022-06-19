bicyles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicyles) # this will print the representation of the list which we do not want to show to the users.

#🍟 To ignore the newline use strip method which will omit the \n 
str1 = "\n Starbucks has the best coffee \n" 
print(str1.strip())

#🍟 Converting string into list
toList = "asad, bilal, salim, sadiq"
converted = toList.split(',')
print(converted)

"""
3-1. Names: Store the names of a few of your friends in a list called names. Print each
person’s name by accessing each element in the list, one at a time.

"""
friend_list = ['hamza','waqas','saqib','usman','muhib']
for i in range(len(friend_list)):
    print(friend_list[i].strip())
    

"""
3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing
each person’s name, print a message to them. The text of each message should be the
same, but each message should be personalized with the person’s name.

"""
for i in range(len(friend_list)):
    print("Hello, ",friend_list[i].strip())
    
# 🍟 Inserting Elements into a List
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0,"Kawasaki") # Insert method will put value at index 0 and will push the old value further an index.
print(motorcycles,"\n\n")
# To remove an element from a list use del keyword with the specifying list item
"""
# 🍟 Removing Elements from the List using pop and del method
The key difference b/w 'del' and 'pop' method is that del keyword delete the value forever but pop method will
take out the value from list and will give us in return or we can store it in a variable. we can use pop method to remove any item
in a list and can store them in a variable.
"""
print("Before del method:\n\n",motorcycles)
del motorcycles[1]
print(motorcycles,'\n\n') #['Kawasaki', 'honda', 'yamaha'] ==> suzuki removed from the end
print("Before pop method:\n",motorcycles)
pop_motorcycle = motorcycles.pop(2)
print("Popped list: ",motorcycles)
print("Popped motorcycle: ",pop_motorcycle)

print('🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟')

# 🍟 Removing an Item by Value
names = ['asad','bilal','salim','sadiq']
print("Before removing asad element: ",names)
remove_value = names.remove("asad")
print("After removing: ",names)


# remove() method will only remove the first occurence of the element if the list contains more than one element with the same name
# then we have to put the loop to go through all the list and make sure to delete every occurrence of that element. e.g.
 
duplicate = ['asad','bilal','asad','sadiq','salim', 'saqib','hamza','asad']
print("\n\nBefore removing: ",duplicate)
for delete in duplicate:
    if delete == "asad":
        duplicate.remove(delete)
    
print("Deleting all duplicate of asad: ",duplicate)

"""
3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would
you invite? Make a list that includes at least three people you’d like to invite to dinner.
Then use your list to print a message to each person, inviting them to dinner.

"""
guest_list = []
no_of_guests = int(input('How many guest you want to invite?: '))
i = 0
while i!= no_of_guests:
    guest_list.append(input('Enter the name of the guest: '))
    i+=1

for guest in guest_list:
    print(f"Hello, {guest}. I invite you to my wedding.")

"""
3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner,
so you need to send out a new set of invitations. You’ll have to think of someone else to
invite.

"""
print("Before replacing guest: ",guest_list)
remove_guest = input('Do you want to remove a guest and invite someone else instead?: ')
old_guest_index = guest_list.index(remove_guest)
if remove_guest in guest_list:
    guest_list.remove(remove_guest)

new_guest = input('Enter the name of the new guest: ')
guest_list.insert(old_guest_index,new_guest)

print("After replacing guest: ",guest_list)


"""
3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive
in time for the dinner, and you have space for only two guests.

"""

print('\n\n🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟')

#Leave space only two guest in a list
while len(guest_list) != 2:
    guest_list.pop()

print("We have only these guest in list: ",guest_list)
del guest_list[0:len(guest_list)] # remove from the list from index 0 upto the end of the list
print("Empty list: ",guest_list)

