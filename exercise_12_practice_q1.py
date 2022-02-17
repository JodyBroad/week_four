cheese = ['cheddar', 'stilton', 'cornish yarg']
print(cheese)

# this is adding them as individual letters, each one being a new item
# cheese += 'Oke'
# print(cheese)

# [] will add as a new item on the list
cheese += ['Oke']
print(cheese)

# using .extend to add to list
cheese.extend(['edam', 'wensleydale'])
print(cheese)

# can also use +=
cheese += ['gorgonzola', 'swiss']
print(cheese)

