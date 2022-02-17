# need to generate and display 6 random lottery numbers between 1 and 50

# need to import the random functionality
import random

# going to use empty list to store the numbers
lotto_numbers = []

# to generate one random number and store it
# number_one = random.randint(1, 50)
# print(number_one)
#
# # but we want to add to a list
# lotto_numbers.append(number_one)
# print(lotto_numbers)
#
# # can now add second number
# number_two = random.randint(1, 50)
# print(number_two)
# lotto_numbers.append(number_two)
# print(lotto_numbers)

# we must be able to do this for a loop
for i in range (0, 6):
    number = random.randint(1, 50)
    # what if we get duplicate numbers? can we check this as we go, and not add if it is already on the list?
    while number in lotto_numbers:
        number = random.randint(1, 50)
# if it isn't already on the list, we can now add it to the list with .append
    lotto_numbers.append(number)

# print(lotto_numbers)

# a sorted list would look nicer
lotto_numbers_sorted = sorted(lotto_numbers)
print("This week's lotto numbers are:" , lotto_numbers_sorted)


