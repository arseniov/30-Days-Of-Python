# Exercises: Level 1

# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
# # Enter your age: 30
# # You are old enough to learn to drive.
# # Output:
# # Enter your age: 15
# # You need 3 more years to learn to drive.

age = int(input("Enter your age: "))
years = 18 - age
if age > 18:
    print(f"You are {age} years old and you can drive.")
else:
    print(f"You need {years} more years to drive.")

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
# # Enter your age: 30
# # You are 5 years older than me.
my_age = 29
your_age = int(input("What is your age? "))
diff = abs(your_age - my_age)

if your_age > my_age and diff > 1:
    print(f"You are {diff} years older than me")
elif your_age > my_age and diff == 1:
    print(f"You are {diff} year older than me")
elif your_age == my_age and diff == 0:
    print(f"We both are {my_age} years old")
elif your_age < my_age and diff > 1:
    print(f"You are {diff} years younger than me")
elif your_age < my_age and diff == 1:
    print(f"You are {diff} year younger than me")

# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
# # Enter number one: 4
# # Enter number two: 3
# # 4 is greater than 3
a = int(input("Enter 'a': "))
b = int(input("Enter 'b': "))

if a > b:
    print("'a' is greater than 'b'")
elif a < b:
    print("'a' is smaller than 'b'")
else:
    print("'a' is equal to 'b'")

# ### Exercises: Level 2

# Write a code which gives grade to students according to theirs scores:
# # 80-100, A
# # 70-89, B
# # 60-69, C
# # 50-59, D
# # 0-49, F


# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer


# The following list contains some fruits:
# # fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')



# Exercises: Level 3

# Here we have a person dictionary. Feel free to modify it!

#         person={
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
#     }
# #  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# #  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
# #  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
# #  * If the person is married and if he lives in Finland, print the information in the following format:
# #     Asabeneh Yetayeh lives in Finland. He is married.