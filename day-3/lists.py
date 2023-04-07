my_list = [1, 2, 3, "four", ["five", "six"]]

print(my_list)

my_list = [1, 2, 3, 4, 5]
print(len(my_list))         # returns the number of items in a list => prints 5
my_list.append(6)           # adds an item to the end of a list
print(my_list)              # prints [1, 2, 3, 4, 5, 6]
my_list.insert(2, "three")  # inserts an item at a specified position in a list.
print(my_list)              # prints [1, 2, "three", 3, 4, 5, 6]
my_list.remove(3)           # removes the first occurrence of an item from a list.
print(my_list)              # prints [1, 2, "three", 4, 5, 6]
item = my_list.pop(3)       # removes and returns the item at a specified position in a list.
print(my_list)              # prints [1, 2, "three", 5, 6]
print(item)                 # prints 4
integer_list = [4, 3, 2, 0]
integer_list.sort()
print(integer_list)         # print [0, 2, 3, 4]
my_list.sort()              # throws error
print(my_list)              #
