
# Exercises: Level 1
# Create an empty tuple
tpl = ()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("Luigi", "Giancarlo")
sisters = ("Alessia", "Federica", "Martina")

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)

# How many siblings do you have?
print(len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ("Father", "Mother")
family_members = siblings + parents
print(family_members)

# Exercises: Level 2
# Unpack siblings and parents from family_members
siblings, parents = family_members[:4], family_members[-2:]
print(siblings, parents)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("Apple", "Pear", "Strawberry")
vegetables = ("Salad", "Kale", "Tomato", "Potato")
animal_products = ("Food", "Crackers")
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
if len(food_stuff_tp) // 2 == 0:
    print(food_stuff_tp[:int((len(food_stuff_tp)) / 2)] + food_stuff_tp[int(len(food_stuff_tp) + 1 / 2)])
else:
    print(food_stuff_tp[:int((len(food_stuff_tp) - 1) / 2)], food_stuff_tp[int((len(food_stuff_tp)) / 2):])


# Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt[3:6])

# Delete the food_staff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
if ("Estonia" in nordic_countries) == True:
    print("Estonia IS a nordic country.")
else:
    print("Estonia is NOT a nordic country")

# Check if 'Iceland' is a nordic country
if ("Iceland" in nordic_countries) == True:
    print("Iceland IS a nordic country.")
else:
    print("Iceland is NOT a nordic country")

# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')