myn = [45, 66, 12, 3, 99, 3.142, 42]
print("min:", min(myn), "max:", max(myn))
print("sum:", sum(myn))

myd = {'Fred':3, 'Jim':8, 'Dave':42}
print("min:", min(myd), "max:", max(myd))
# will error if you try to add two things that are not integers
# print("sum:", sum(myd))

mytuple = ('eggs', 'bacon', 'spam', 'tea', 'beans')
print(mytuple[2:4])
print(mytuple[-4])

# converts tuple into list
mylist = list(mytuple)
# prints from position 1 to end as end value is blank
print(mylist[1:])
# prints from start to position 2 as start value is blank
print(mylist[:2])

cheese = ['cheddar', 'camembert', 'brie', 'stilton']
print(cheese)
# del is a function not a statement therefore does not need brackets
del cheese[1:3]
print(cheese)
# .append will just add one item to the end
cheese.append('gouda')
print(cheese)
# using .extend to add to list
cheese.extend(['edam', 'wensleydale'])
print(cheese)
# can also use +=
cheese += ['gorgonzola', 'swiss']
print(cheese)
# or.insert to specify index location
cheese.insert(2, 'babybel')
print(cheese)

# can use .pop to remove an item from a specific index, leaving the () blank will just remove the last item
saved = cheese.pop(1)
print("Saved1:", saved, ", Result:", cheese)

# .remove will take off the leftmost item matching the value
cheese.remove('gouda')
print(cheese)

# .sort will sort the list in place, here we are sorting by length
cheese.sort(key=len)
print(cheese)

# .sort with no parameter will just do alphabetical
cheese.sort()
print(cheese)

# .sort with reverse=True will do reverse alphabetical
cheese.sort(reverse=True)
print(cheese)

# can also use sorted function - sorted() can be used on any iterable, .sort can only be used on lists
# sorted() gives you new list, preserving the old order on the original variable, .sort modifies the original list
alphabetical_cheese = sorted(cheese)
print(alphabetical_cheese)

