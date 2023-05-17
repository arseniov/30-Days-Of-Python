
# Declare an empty list
list = []

# Declare a list with more than 5 items
list = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh"]

# Find the length of your list
print(len(list))

# Get the first item, the middle item and the last item of the list
print(list[int((len(list) - 1) / 2)])
print(list[0], list[3], list[6])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = [{"name": "Luigi", "height": 150, "marited": False, "address": "Milano"}]
print(mixed_data_types)

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
print(it_companies[0], it_companies[3], it_companies[6])
print(it_companies[0], it_companies[int((len(it_companies) - 1) / 2)], it_companies[-1])

# Print the list after modifying one of the companies
it_companies[2] = "TPT"
print(it_companies)

# Add an IT company to it_companies
it_companies.append("OpenAI")
new_list = ["Bard", "MidJourney"]
print(it_companies + new_list)

# Insert an IT company in the middle of the companies list
it_companies[(int((len(it_companies) - 1) / 2))] = "Test"
print(it_companies)
it_companies.insert((int((len(it_companies) - 1) / 2)), "Test2")
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
print(it_companies[1].upper())

# Join the it_companies with a string '#;  '


# Check if a certain company exists in the it_companies list.
print("Google" in it_companies) 

# Sort the list using sort() method
print(sorted(it_companies))
print(it_companies)
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)
it_companies.sort()

# Slice out the first 3 companies from the list
print(it_companies[3:])

# Slice out the last 3 companies from the list
print(it_companies[:-3])

# Slice out the middle IT company or companies from the list
# print(it_companies.pop(int((len(it_companies) - 1) / 2)))
it_companies.pop(int((len(it_companies) - 1) / 2))
# print(int((len(it_companies) - 1) / 2))
print(it_companies)

# Remove the first IT company from the list
del it_companies[0]
print(it_companies)

# Remove the middle IT company or companies from the list
del it_companies[int((len(it_companies) - 1) / 2)]
print(it_companies)

# Remove the last IT company from the list
del it_companies[int((len(it_companies) - 1))]
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del it_companies

# Join the following lists:
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
merged1 = front_end + back_end
front_end_copy = front_end.copy()
front_end_copy.extend(back_end)
print("merged1: ", merged1)
print("front_end_copy: ", front_end_copy)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = merged1.copy()
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)


# Exercises: Level 2
# The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print("min: ", ages[0], ".", "max: ", ages[len(ages) - 1])

# Add the min age and the max age again to the list
ages.append(ages[0])
ages.append(ages[(len(ages)) - 2])
print(ages)

# Find the median age (one middle item or two middle items divided by two)
ages.sort()

# Find the average age (sum of all items divided by their number )
avg_age = sum(ages) / 2
print(sum(ages))
print(avg_age)

# Find the range of the ages (max minus min)
print(max(ages) - min(ages))

# Compare the value of (min - average) and (max - average), use abs() method
print(abs(min(ages) - avg_age))
print(abs(max(ages) - avg_age))
print(abs(min(ages) - avg_age) is abs(max(ages) - avg_age))

# Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

print(countries[int((len(countries) - 1) / 2)])

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
if len(countries) // 2:
    countries1, countries2 = countries[:int(len(countries) / 2)], countries[int(len(countries) / 2):]
else:
    countries1, countries2 = countries[:int((len(countries) + 1) / 2)], countries[int((len(countries) + 1) / 2):]

print("Last countries1 item:", countries1[len(countries1) - 1])
print("First countries1 item:", countries2[0])
print("Lenght of both lists:", len(countries1) + len(countries2))

for i in countries2:
    if i in countries1 is True:
        print(i, "is in countries1 at index", countries1.index(i))
    else:
        None

for i in countries1:
    if i in countries2 is True:
        print(i, "is in countries1 at index", countries2.index(i))
    else:
        None




# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
first, second, third, *rest = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(f"First: {first}\nSecond: {second}\nThird: {third}\nRest: {rest}")