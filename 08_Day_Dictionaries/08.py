
# Create an empty dictionary called dog
dog = {}


# Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "Doggie"
dog["color"] = "Brown"
dog["breed"] = "Husky"
dog["legs"] = 8
dog["age"] = 74

print(dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {"first_name":"Bob", "last_name":"Odenkirk", "gender":"Male", "age":15, "marital_status":"Divorced", "skills":["Python", "CSS", "HTML", "Bioengineering"], "country":"USA", "city":"Oklahoma", "address":"via Scapicollo 17"}
print(student)
print(student.get("first_name"))

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
print(student.get("skillz"))
print(student["skills"])
print(student["skills"][3])
print(type(student["skills"]))

# Modify the skills values by adding one or two skills
student["skills"] = student["skills"] + ["JS", "React"]
print(student["skills"])

# Get the dictionary keys as a list
keys_list = student.keys()
print(keys_list)
print(type(keys_list))
keys_list = list(student.keys())
print(keys_list)
print(type(keys_list))

# Get the dictionary values as a list
values_list = list(student.values())
print(values_list)

# Change the dictionary to a list of tuples using items() method
dict_tuples = student.items()

# Delete one of the items in the dictionary
student.pop("country")
print(student)
student.popitem()
print(student)

# Delete one of the dictionaries
print(student.clear())
del student

