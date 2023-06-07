
# 1. Filter only negative and zero in the list using list comprehension
#    ```py
#    numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
#    ```
# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
# negative = [i for i in numbers if i <= 0]
# print(negative)

# print([i for i in numbers if i <= 0])

# 2. Flatten the following list of lists of lists to a one dimensional list :

#    ```py
#    list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

#    output
#    [1, 2, 3, 4, 5, 6, 7, 8, 9]
#    ```
# list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# flattened = [num for row in list_of_lists for row in num for num in row]
# print(flattened)

# list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# flattened = [num for row in [num for row in list_of_lists for num in row] for num in row]
# print(flattened)

# 3. Using list comprehension create the following list of tuples:
#    ```py
#    [(0, 1, 0, 0, 0, 0, 0),
#    (1, 1, 1, 1, 1, 1, 1),
#    (2, 1, 2, 4, 8, 16, 32),
#    (3, 1, 3, 9, 27, 81, 243),
#    (4, 1, 4, 16, 64, 256, 1024),
#    (5, 1, 5, 25, 125, 625, 3125),
#    (6, 1, 6, 36, 216, 1296, 7776),
#    (7, 1, 7, 49, 343, 2401, 16807),
#    (8, 1, 8, 64, 512, 4096, 32768),
#    (9, 1, 9, 81, 729, 6561, 59049),
#    (10, 1, 10, 100, 1000, 10000, 100000)]
#    ```
# list_of_tuples = [(a, a-a+1, a, a**2, a**3, a**4, a**5) for a in range(0,10)]
# print(list_of_tuples)


# 4. Flatten the following list to a new list:
#    ```py
#    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#    output:
#    [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
#    ```
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# flattened = [country for row in [country for row in countries for country in row] for country in row]
# print(flattened)

# 5. Change the following list to a list of dictionaries:
#    ```py
#    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#    output:
#    [{'country': 'FINLAND', 'city': 'HELSINKI'},
#    {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#    {'country': 'NORWAY', 'city': 'OSLO'}]
#    ```
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
list_of_dict = []
# list_of_dict.append({"country": [data for sublist in [data for sublist in countries for data in sublist] for data in sublist], "city": "dsad"})
list_of_dict = [{"country": {data[0] for data in sublist}, "city": [data[1] for data in sublist]} for sublist in countries]


print(list_of_dict)

# 6. Change the following list of lists to a list of concatenated strings:
#    ```py
#    names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
#    output
#    ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
#    ```



# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.

