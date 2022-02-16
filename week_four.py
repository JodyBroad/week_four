a = 3
b = 5
print(a, b)

# can swap the references
a, b= b, a
print(a, b)

# produces range of integers
# x, y, z = range(3)
# print(x, y, z)

# needs parameters in certain stop, start and step - in this example the start is 1, stop is 6, step is 2
c, d, e = range(1, 6, 2)
print(c, d, e)

# overloaded operator so will print multiple times
word = "spam "
print(word * 4)

# also works for tuples
names_tuple = 'Alice', 'Orlane', 'Jeje', 'Jodie', 'Ella', 'Mya', 'Christelle', 'Mya'
print(names_tuple * 3)

# will just print one at a specific index position
print(names_tuple[0])

# will just print a slice , first number is start (included), second number is end (excluded) - end+1 situation
print(names_tuple[0:2])

# omitting a start or end value will just default to the end/start of the list
print(names_tuple[:2])
print(names_tuple[0:])

# can also use negative values to locate
print(names_tuple[-1])

# asterisk before the variable name will make everything in the middle into a list a put it in the asterisked item
# it is just unpacking the start and end value
x, *y, z = range(14)
print(x, y, z)

# can use the asterisk on any of the positions
a, b, *c = names_tuple
print(a, b, c)

# can convert the tuple to a list
names_list = list(names_tuple)
# print the data type of the variable names_list
print(type(names_list))
print(names_list)

# use the sort method - this is permanent and cannot be reverted back to original order
# names_list.sort()

# sorted function (always returns sorted list) saves the sorted list to a new variable, so you can retain the original unsorted order
names_sorted = sorted(names_list)
print(names_sorted)

#names_sorted_tuple = sorted(names_tuple)
#print(names_sorted_tuple)

number_list = [4, 7, 2, 66, 12, 99]
# passing in reverse=True will sort high to low instead of low to high
number_list.sort(reverse=True)
print(number_list)

# sort key is name of the function that will work on each item in the collection, will sort by length of the name
names_list.sort(key=len)
print(names_list)

# when turning into a set will get rid of duplicates
names_set = set(names_list)
print(names_set)