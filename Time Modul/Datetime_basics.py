import datetime
#from datetime import *
#import calendar

# # Task 1

# current_datetime = datetime.datetime.now()
# print(current_datetime.year)
# print(current_datetime.strftime("%A"))

# # Task 2

# some_date = datetime.datetime(2021, 7, 14)

# weekday = some_date.weekday()

# print(weekday)

# Task 3

# user_inp = int(input("Enter  a Year: "))

# check_inp = calendar.isleap(user_inp)
# if check_inp == True:
#     print("The Year", user_inp, "is a Leap: ")
# else:
#     print("The Year", user_inp, "is not Leap: ")


# Task 4

# user_inp = input("Enter a date in this format: Mmm dd jjjj hh:mmAM/PM: ")

# date_as_string = datetime.strptime(user_inp,"%b %d %Y %H:%M")

# print("The time: ", date_as_string)

# Task 5

# current_datetime = datetime.datetime.now()

# sub_days = current_datetime - datetime.timedelta(days=15)

# sub_days2 = datetime.strptime(sub_days)

# print(sub_days)

# Task 6

# current_datetime = datetime.datetime.now()

# sub_days = current_datetime + datetime.timedelta(days=7)

# print(sub_days)

# Task 7 

# user_inp = input("Type the time of moving: dd mm Year: ")

# string_as_date = datetime.datetime.strptime(user_inp,"%d %m %Y")

# day_of_pay = string_as_date + datetime.timedelta(days=25)

# print("Hello Friedrich, your rent of 300 € is due on:", day_of_pay)

print(240.5 / 30.25)