from datetime import datetime, timedelta


#user_birth = input("Enter a date in format: dd mm yyy: ")

user_birth = "25 01 1992"

celebrate = datetime.strptime(user_birth, "%d %m %Y")

today = datetime.today()

time_until = celebrate - today
print(time_until)