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
a_min = 90
a_max = 100
b_min = 70
b_max = 89
c_min = 60
c_max = 69
d_min = 50
d_max = 59
f_min = 0
f_max = 49

score = int(input("Enter your score: "))

if score <= 100 and score >= 90:
    print("Your grade is A")
elif score <= 89 and score >= 70:
    print("Your grade is B")
elif score <= 69 and score >= 60:
    print("Your grade is C")
elif score <= 59 and score >= 50:
    print("Your grade is D")
elif score <= 49 and score >= 0:
    print("Your grade is F")

# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = input("Write a month: ")
if month in ["September", "October", "November"]:
    print("Season is Autumn")
elif month in ["December", "January", "February"]:
    print("Season is Winter")
elif month in ["March", "April", "May"]:
    print("Season is Spring")
elif month in ["June", "July", "August"]:
    print("Season is Summer")
else:
    print(f"{month} is not a valid month name")


# The following list contains some fruits:
# # fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
for i in (1,3):
    new_fruit = input("New fruit? ")
    if new_fruit in fruits:
        print("This fruit is already in the list")
    else:
        fruits.append(new_fruit)
        print(fruits)


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

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
middle = int(len(person)/2) - 1
print(person["skills"][int(len(person)/2) - 1]) if "skills" in person and len(person["skills"]) > 1 else print("Skills is not present")

print(person["skills"][list(person["skills"]).index("Python")]) if "skills" in person and "Python" in person["skills"] else print("Python is not in skills list")

print(list(person["skills"]).index("Python")) if "skills" in person and "Python" in person["skills"] else print("Python is not in skills list")

if "JavaScript" and "React" and not "Node" and not "Python" and not "MongoDB" in person["skills"]:
    print("He is a front end developer")
elif "Node" and "Python" and "MongoDB" and not "JavaScript" and not "React" in person["skills"]:
    print("He is a backend developer")
elif "React" and "Node" and "MongoDB" and not "JavaScript" and not "Python" in person["skills"]:
    print("He is a fullstack developer")
else:
    print("Unknown title")

ismarried = "is" if person["is_married"] == True else "is not"
print(person["first_name"] + f" " + person["last_name"] + f"lives in " + person["country"] + f". He " + ismarried + f" married")