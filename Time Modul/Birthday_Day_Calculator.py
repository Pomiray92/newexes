import datetime

user_birthday = input("Type your Birthday: ")

converting = datetime.datetime.strptime(user_birthday,"%B %d %Y")

print(converting)