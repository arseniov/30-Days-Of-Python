a = "ciao"
b = "luca"
c = 1
d = 6
print("{} + {} = {}".format(c, d, c+d))
print(f"{c} - {d} = {c - d}")
# print('{} ** {} = {}'.format(a, b, a ** b))
# print(f'{a} + {b} = {a + b}')

name = "gianluca"
x = dict()
for i in range(0,len(name)):
    x[i] = name[i]
    # print("x{} = {}".format(i,name[i]))
    print(f"x{i} = {name[i]}")


print(name[0:6:2])

