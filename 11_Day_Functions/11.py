# Exercises: Level 1
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.

import random
# def add_two_numbers(a, b):
#     print(a)
#     print(b)
#     return a + b

# add_two_numbers(random.randint(1,25), random.randint(1,10))

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
# def calc(pi, r):
#     area_of_circle = pi * r * r
#     return area_of_circle

# calc(3.14, 1)

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
# def add_all_nums(*nums):
#     sum = 0
#     for num in nums:
#         sum = sum + num
#     return sum

# add_all_nums(1, 5, 10, 2, 5, 138, 392, 30)

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
# def convert_c_to_f(c):
#     f = c * (9/5) + 32
#     return f

# print(convert_c_to_f(50))

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
# def check_season(month):
#     if month in ("Dec", "Jan", "Feb"): return "Winter"
#     if month in ("Mar", "Apr", "May"): return "Spring"
#     if month in ("Jun", "Jul", "Aug"): return "Summer"
#     else: return "Autumn"

# check_season(input("Which month? "))

# Write a function called calculate_slope which return the slope of a linear equation


# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
# def solve_quadratic_eqn(a, b, c, x):
#     eq = a * (x^2) + b * x + c
#     return eq

# solve_quadratic_eqn(1, 5, 3, 2)

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
# def print_list(*args):
#     for arg in args:
#         print(arg)

# print_list(random.randint(1,1000), random.randint(1,1000), random.randint(1,1000), random.randint(1,1000))

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# # ["C", "B", "A"]
# def reverse_list(list):
#     reverse = []
#     for arg in list:
#         reverse.append(arg)
#     reverse.sort(reverse=True)
#     return reverse

# reverse_list([1, 2, 3, 4, 5])


# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items


# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# numbers = [2, 3, 7, 9];
# print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
# def add_item(list, a):
#     list.append(a)
#     return list

# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
# add_item(food_stuff, "Gianluca")

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9];
# print(remove_item(numbers, 3))  # [2, 7, 9]


# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# print(sum_of_numbers(5))  # 15
# print(sum_all_numbers(10)) # 55
# print(sum_all_numbers(100)) # 5050
# def sum_all_numbers(a):
#     sum = 0
#     b = 0
#     while b <= a:
#         sum+=b
#         b+=1
#     return sum

# sum_all_numbers(100)

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
# def sum_of_odds(a):
#     sum = 0
#     b = 0
#     while b <= a:
#         if b % 2 != 0:
#             sum+=b
#         else:
#             pass
#         b+=1
#     return sum

# sum_of_odds(100)

# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
# def sum_of_even(a):
#     sum = 0
#     b = 0
#     while b <= a:
#         if b % 2 == 0:
#             sum+=b
#         else:
#             pass
#         b+=1
#     return sum

# sum_of_even(100)


# Exercises: Level 2
# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.
# def evens_and_odds(a):
#     count_evens = 0
#     count_odds = 0
#     i = 0
#     while i <= a:
#         if i % 2 == 0:
#             count_evens+=1
#         else:
#             count_odds+=1
#         i+=1
#     print("Evens:", count_evens)
#     print("Odds:", count_odds)

# evens_and_odds(abs(int(input("Number? "))))

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number


# Call your function is_empty, it takes a parameter and it checks if it is empty or not

# def is_empty(x):
#     if x is None:
#         return True
#     else:
#         return False
    
# a = 0
# b = 10
# c = "Text!"

# is_empty(input("Is parameter empty? "))

# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).



# Exercises: Level 3
# Write a function called is_prime, which checks if a number is prime.


# Write a functions which checks if all items are unique in the list.


# Write a function which checks if all the items of the list are of the same data type.


# Write a function which check if provided variable is a valid python variable


# Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order


# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.

