# ### Exercises: Level 1

# 1. Writ a function which generates a six digit/character random_user_id.
#    ```py
#      print(random_user_id());
#      '1ee33d'
#    ```

# import random
# import string

# def random_user_id():
#     user_id = str()
#     for i in range(1, 7):
#         print(i)
#         x = random.choice(range(1,2))
#         if x == 1: user_id = f"{user_id}{random.choice(string.ascii_letters)}"
#         if x == 2: user_id = f"{user_id}{random.choice(string.digits)}"
    
#     return user_id

# random_user_id()

# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
   
# ```py
# print(user_id_gen_by_user()) # user input: 5 5
# #output:
# #kcsy2
# #SMFYb
# #bWmeq
# #ZXOYh
# #2Rgxf
   
# print(user_id_gen_by_user()) # 16 5
# #1GCSgPLMaBAVQZ26
# #YD7eFwNQKNs7qXaT
# #ycArC5yrRupyG00S
# #UbGxOFI7UXSWAyKN
# #dIV0SSUTgAdKwStr
# ```


# import random
# import string

# def user_id_gen_by_user(chars, ids):
#     for id in range(1, ids + 1):
#         user_id = str()
#         for char in range(1, chars + 1):
#             x = random.choice(range(1,2))
#             if x == 1: user_id = f"{user_id}{random.choice(string.ascii_letters)}"
#             if x == 2: user_id = f"{user_id}{random.choice(string.digits)}"
#         print(user_id)

# user_id_gen_by_user(int(input("How many characters? ")), int(input("How many IDs? ")))


# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
   
# ```py
# print(rgb_color_gen())
# # rgb(125,244,255) - the output should be in this form
# ```

# import random

# def rgb_color_gen():
#     rgb = f"rgb({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)})"
#     return rgb

# print(rgb_color_gen())
# # rgb_color_gen()

# ### Exercises: Level 2

# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

# import random, string
# def list_of_hexa_colors():
#     hexa = "#"
#     for i in range(1,7):
#         print(i)
#         x = random.choice([1,2])
#         print(x)
#         if x == 1: hexa = f"{hexa}{random.choice(string.ascii_uppercase[:7])}"
#         if x == 2: hexa = f"{hexa}{random.choice(string.digits)}"
#     return hexa

# print(list_of_hexa_colors())

# import random
# r = lambda: random.randint(0,255)
# print('#%02X%02X%02X' % (r(),r(),r()))

# 1. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

# import random
# import string

# array = []

# r = lambda: random.randint(0,255)
# x = lambda: random.randint(0, len(array))

# def list_of_rgb_colors():
#     for i in range(150):
#         rgb = "rgb(%d,%d,%d)" % (r(), r(), r())
#         array.append(rgb)
    
#     for i in range(10):
#         print(array[i])

# list_of_rgb_colors()

# 1. Write a function generate_colors which can generate any number of hexa or rgb colors.

# import random
# import string

# array = []

# characters = string.digits + string.ascii_uppercase[:6]

# def generate_hexa_colors():
#     for i in range(150):
#         hexa = "#" + "".join(random.choice(characters) for x in range(6))
#         array.append(hexa)
    
#     for i in range(10):
#         print(array[i])

# generate_hexa_colors()


# ```py
#    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
#    generate_colors('hexa', 1) # ['#b334ef']
#    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
#    generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
#    ```

# ### Exercises: Level 3

# 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
# hexa = [
#     "#6E7F8D",
#     "#C1DA07",
#     "#82F166",
#     "#EC97E7",
#     "#4AF08A",
#     "#234181",
#     "#1E2CD8",
#     "#32305E",
#     "#E7BC7D",
#     "#7CB15C",
# ]

# hexa.sort()
# print(hexa)

# import random
# random.shuffle(hexa)
# print(hexa)


# 1. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

import random
import string



