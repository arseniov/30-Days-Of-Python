print("Day 2: 30 days of Python programming")

first_name = "Andrea"
last_name = "Luigi"
full_name = first_name + " " + last_name
country = "Italy"
city = "Milan"
age = 250
year = 2023
is_married = True
is_true = False
is_light_on = True

job, occupation, annual_revenue = "None", "Director", 150


for name in vars().keys():
    if not name.startswith("_"):
        myvalue = eval(name)
        print(name, "is", type(myvalue), "and is equal to ", myvalue)


for name in vars().keys():
    if not name.startswith("_"):
        myvalue = str(eval(name))
        print(myvalue, "is", len(myvalue), "characters long.")



num_one = 5
num_two = 4

sum = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one / num_two
remainder = num_one // num_two
exp = num_one ^ num_two
floor_division = num_one % num_two

radius = 30
area_of_circle = (radius * radius) * 3.141592653589793
print("Area of the circle is", area_of_circle,"m2")

radius = int(input("What's the circle radius? "))
circum_of_circle = radius * 2 * 3.141592653589793
print("Circum of the circle is", circum_of_circle,"m")

first_name = input("First name? ")
last_name = input("Last name? ")
country = input("Country? ")
age = input("Age? ")
print(first_name, last_name, "is from", country, "and is", age, "years old")

first_name, last_name, country, age = input("Enter First name, Last name, Country and Age divided by a space").split(", ")
print(first_name, last_name, "is from", country, "and is", age, "years old")