from datetime import datetime
import os, sys
import time
os.system("clear")

def print_slow(string):
    for letter in string:               # for each letter in the string
        sys.stdout.write(letter)        # prints out letter
        sys.stdout.flush()              # flushes the line ()
        time.sleep(0.3)

def print_slow2(string):
    for letter in string:               # for each letter in the string
        sys.stdout.write(letter)        # prints out letter
        #sys.stdout.write(numbers)     
        sys.stdout.flush()              # flushes the line ()
        time.sleep(0.1)

user_birth = input("Enter Your Birthday: dd mm yyyy: ")
#user_birth = "25 01 1992"
convert_date = datetime.strptime(user_birth, "%d %m %Y")

year = (datetime.today() - convert_date).days//365.25
#convert_back = datetime.strftime(year)
time.sleep(0.5) 
print("Your are ", year, "years old!")
time.sleep(0.9)
print_slow("BUT WAIT!\n")

days_remain = (datetime.today() - convert_date).days%365.25
print_slow2("There are: "), time.sleep(2), print(days_remain, "days remain")
print_slow2("What we would do whit them?\n")