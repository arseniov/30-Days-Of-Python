# Exercises: Level 1
# Iterate 0 to 10 using for loop, do the same using while loop.
# for a in range(11):
#     print(a)

# b = 1
# while b <= 10:
#     print(b)
#     b = b + 1


# # Iterate 10 to 0 using for loop, do the same using while loop.
# for c in range(10,0,-1):
#     print(c)

# d = 10
# while d >= 1:
#     print(d)
#     d = d - 1


# Write a loop that makes seven calls to print(), so we get on the output the following triangle:

# #   #
# #   ##
# #   ###
# #   ####
# #   #####
# #   ######
# #   #######

# line1 = ""

# for e in range(0,7):
#     line1 = line1 + "#"
#     print(line1)
    


# Use nested loops to create the following:

# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #

# for f in range(0,8):
#     line = ""
#     for g in range(0,10):
#         line = line + " " + "#"
#     print(line)

# Print the following pattern:

# # 0 x 0 = 0
# # 1 x 1 = 1
# # 2 x 2 = 4
# # 3 x 3 = 9
# # 4 x 4 = 16
# # 5 x 5 = 25
# # 6 x 6 = 36
# # 7 x 7 = 49
# # 8 x 8 = 64
# # 9 x 9 = 81
# # 10 x 10 = 100

# h = 0
# while h <= 10:
#     print(h, "x", h, "=", h*h)
#     h = h + 1


# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

# lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
# for item in lst:
#     print(item)


# Use for loop to iterate from 0 to 100 and print only even numbers

# for i in range(0,100,2):
#     print(i)

# Use for loop to iterate from 0 to 100 and print only odd numbers
# for l in range(1,100,2):
#     print(l)



# Exercises: Level 2
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# # The sum of all numbers is 5050.
# sumall =  0
# for m in range(0,101):
#     sumall = sumall + m
#     print(sumall)

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# # The sum of all evens is 2550. And the sum of all odds is 2500.
# sumall_even = 0
# sumall_odd = 0
# for n in range(0,101):
#     if (n % 2) == 0:
#         sumall_even = sumall_even + n
#     else:
#         sumall_odd = sumall_odd + n

# print("Sum of even numbers is", sumall_even)
# print("Sum of all odd numbers is", sumall_odd)



# Exercises: Level 3
# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

from countries import countries

for country in countries:
    print(country)

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

fruits = ['banana', 'orange', 'mango', 'lemon']

for fruit in fruits[::-1]:
    print(fruit)

# Go to the data folder and use the countries_data.py file.
# # What are the total number of languages in the data


# # Find the ten most spoken languages from the data


# # Find the 10 most populated countries in the world

