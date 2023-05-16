# a = "ciao"
# b = "luca"
# c = 1
# d = 6
# print("{} + {} = {}".format(c, d, c+d))
# print(f"{c} - {d} = {c - d}")
# # print('{} ** {} = {}'.format(a, b, a ** b))
# # print(f'{a} + {b} = {a + b}')

# name = "gianluca"
# x = dict()
# for i in range(0,len(name)):
#     x[i] = name[i]
#     # print("x{} = {}".format(i,name[i]))
#     print(f"x{i} = {name[i]}")


# print(name[0:6:2])



# Exercises - Day 4
# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
concat = "Thirty " + "Days " + "Of " + "Python"
print(concat)

concat = "Thirty,Days,Of,Python"
print(concat.replace(",", " "))

thirty = "Thirty"
days = "Days"
of = "Of"
python = "Python"
concat = "".join([thirty, days, of, python])
print(concat)
print(thirty, days, of, python)
print(thirty + days + of + python)


# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.


# Declare a variable named company and assign it to an initial value "Coding For All".
company = "coding for all"


# Print the variable company using print().
print(company)

# Print the length of the company string using len() method and print().
print(len(company))

# Change all the characters to uppercase letters using upper() method.
print(concat.upper())

# Change all the characters to lowercase letters using lower() method.
print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Cut(slice) out the first word of Coding For All string.
print(company.replace("coding ",""))

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index("coding"))
print(company.find("coding"))
print(company.rfind("coding"))


# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("coding","Python"))


# Change Python for Everyone to Python for All using the replace method or other methods.
print(company.replace("coding","Everyone"))

# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(" "))

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))

# What is the character at index 0 in the string Coding For All.
print(company[0])

# What is the last index of the string Coding For All.
print(company[-1])

# What character is at index 10 in "Coding For All" string.
print(company[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
pfe = "Python For Everyone"

# Create an acronym or an abbreviation for the name 'Coding For All'.
cfa = "Coding For All"

# Use index to determine the position of the first occurrence of C in Coding For All.
print(cfa.index("C"))

# Use index to determine the position of the first occurrence of F in Coding For All.
print(cfa.index("F"))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print("Coding For All People".rfind("l"))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("You cannot end a sentence with because because because is a conjunction".find("because"))
print("You cannot end a sentence with because because because is a conjunction".index("because"))
print("You cannot end a sentence with because because because is a conjunction"[::-1].rfind("because"[::-1]))
print("You cannot end a sentence with because because because is a conjunction"[::-1].rindex("because"[::-1]))

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("You cannot end a sentence with because because because is a conjunction".rindex("because"))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
snt = "You cannot end a sentence with because because because is a conjunction"
print(snt.replace("because because because ",""))

# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("You cannot end a sentence with because because because is a conjunction".index("because"))
print("You cannot end a sentence with because because because is a conjunction".find("because"))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'


# Does ''Coding For All' start with a substring Coding?
print("Coding For All".startswith("Coding"))
print("Coding For All".startswith("coding") is True)

# Does 'Coding For All' end with a substring coding?
print("Coding For All".endswith("Coding"))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print(("   Coding For All      ".strip()).title())

# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
print(" ".join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))