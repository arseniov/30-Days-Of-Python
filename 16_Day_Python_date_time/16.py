# 1. Get the current day, month, year, hour, minute and timestamp from datetime module
# from datetime import datetime
# now = datetime.now().strftime("%d %m %Y")
# print(now)

# 1. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
# from datetime import datetime
# now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
# print(now)

# 1. Today is 5 December, 2019. Change this time string to time.
# from datetime import datetime

# today_string = "5 December, 2019"
# today_time = datetime.strptime(today_string, "%d %B, %Y")
# print(today_time)

# 1. Calculate the time difference between now and new year.
# from datetime import datetime

# new_year = datetime.strptime("01/01/2024", "%d/%m/%Y")
# today = datetime.strptime(datetime.now().strftime("%d/%m/%Y"), "%d/%m/%Y")
# diff = new_year - today
# print(diff)

# 1. Calculate the time difference between 1 January 1970 and now.
# from datetime import datetime

# new_year = datetime.strptime("01/01/1970 00:00:00", "%d/%m/%Y %H:%M:%S")
# today = datetime.strptime(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "%d/%m/%Y %H:%M:%S")
# diff = today - new_year
# print(diff)

# 1. Think, what can you use the datetime module for? Examples:
#    - Time series analysis
#    - To get a timestamp of any activities in an application
#    - Adding posts on a blog 