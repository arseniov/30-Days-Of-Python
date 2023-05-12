class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# age = int(138)
# height = float(158)
# complex_num = 1 + 4j

# triangle_area = print("The area of the triangle is", int(input("Base of triangle: ")) * int(input("Height of triangle: ")), "cm^2")

# a = int(input("Side A: "))
# b = int(input("Side B: "))
# c = int(input("Side C:"))
# perimeter = print("Perimeter =", a + b + c)

# length = int(input("Length: "))
# width = int(input("Width: "))
# area = print("Area =", length * width)
# perimeter = print("Perimeter =", length * 2 + width * 2)

# pi = 3.14
# radius = int(input("Radius of circle:"))
# area = print("Area =", radius ** 2 * pi)

# x = 10
# y = x * 2 - 2
# slope = y / x
# print(y, slope)



# x1 = 2
# x2 = 6
# y1 = 2
# y2 = 10
# slope = print((y2 - y1) / (x2 - x1))
# distance = print((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1/2) )


# x = -200

# while x <= 200:
#     y = (x ** 2) + (x * 6) + 9
#     if y == 0:
#         print(bcolors.OKGREEN + "x for y == 0 is x =", str(x) + bcolors.ENDC)
#         break
#     x += 1
#     # print("y is", y, ". Adding 1 to x; x is now", x)


# print(len("python"))
# print(len("dragon"))
# print(len("python") != len("dragon"))
# print(len("python") is not len("dragon"))
# print("on" in "python" and "on" in "dragon")


# print("jargon" in "I hope this course is not full of jargon")


# print("on" not in "dragon" and "on" not in "python")


# a = len("python")
# print(a)
# b = float(a)
# print(b)
# c = str(a)
# print(c)

# i = 1
# while i <= 10:
#     if i % 2 == 0:
#         print(i, "is even")
#     i += 1
# print(16 % 2 == 0)



# print(7 % 3)
# print(int(7 % 3) is int(1.7))



# print(type("10") is type(10))



# print(type(int(9.8)) is type(10))



# hours = int(input("Enter hours: "))
# rate = int(input("Enter hourly rate: "))
# print("weekly pay:", hours * rate)



# years = int(input("Years lived: "))
# seconds = print("Seconds lived:", years * 60 * 60 * 24 * 365)


# print("1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125")

x = int(1)
while x <= 5:
    print(x, x // x, x, x * x, x ** 3)
    x += 1