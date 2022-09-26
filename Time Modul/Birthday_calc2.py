from datetime import date, datetime
import os, sys
import time
os.system("clear")
    

def print_slow(string):
    for letter in string:      # for each letter in the string
        sys.stdout.write(letter)        # prints out letter
        sys.stdout.flush()              # flushes the line ()
        time.sleep(0.2)



#user_birth = input("Enter Your Birthday: dd mm yyyy: ")
user_birth = "25 01 1992"
convert_date = datetime.strptime(user_birth, "%d %m %Y")

year = (datetime.today() - convert_date).days//365.25
#convert_back = datetime.strftime(year)
time.sleep(0.5) 
print("Your are ", year, "years old!")
time.sleep(0.9)
print_slow("BUT WAIT!\n")

days_remain = (datetime.today() - convert_date).days%365.25
print(f"There are: {days_remain} days remain\n")

time.sleep(0.5)
question = input("Do you want to convert them to month?: (yes/no): ")

if question == "yes":
   remain_to_month = (days_remain//30.5)
   remain_to_month2 = (days_remain/30.5)
   time.sleep(0.5)
   print(remain_to_month)
   time.sleep(0.5)
   print("Not correct!? I now! There are some rests: ", remain_to_month2)

else:
    print("See You!")
print()
time.sleep(0.5)
sec_question = input("Do yo want to continue?: yes/no: ")
print()
time.sleep(0.5)
if question == "yes":
    
   month2 = days_remain % (365.25/12)
   month = days_remain // (365.25/12)
   time.sleep(0.5)
   since_birth = f"Your are: {year} year {month} month and some day! I dont wont to continue! Bay!"
   print(since_birth)
   time.sleep(0.5)
   last_question = input("Do you want to now how many days?: yes/no: ")
   print()
   time.sleep(0.5)
   if last_question == "yes":
       print(("No Brother i dont now coding anymore today! See you!"))

       time.sleep(0.5)       
else:
    time.sleep(0.5)
    print("See you!")
    print()