import time
import sys # import sys
import os


string = "Letter"

def print_slow(string):
    for letter in string:               # for each letter in the string
        sys.stdout.write(letter)        # prints out letter
        sys.stdout.flush()              # flushes the line ()
        time.sleep(0.1)




print()

userimp = int(input(print_slow("Take a number: "))) # taking int as input


mash_time = time.time()                # taking unix time (machine time)
humtime = time.ctime(mash_time)        # converting to human readable time

time.sleep(0.5)

print_slow("Begin Time: ")      # printing with the func
print_slow(humtime)             # printing with the func

print()                         # space

start_time = time.time()        # taking unix time again as start time

if userimp > 0: # 
    for i in range(userimp, 0, -1): # defining the countdown
        time.sleep(0.5)
        print("###",i,"###")

stop_time = time.time() # taking unix time again as start time

mash_time2 = time.time()                     # taking unix time (machine time)
humtime2 = time.ctime(mash_time2)            # converting to human readable time
time.sleep(0.5)

print_slow("End Time: ")        # printing with the func
print_slow(humtime2)            # printing with the func
print()

count_time = (stop_time - start_time) # defining elapsed time

time.sleep(0.5)
print_slow("Countdown Time: ")  # printing with the func
print_slow(str(count_time))     # printing with the func elapsed time

print()
print()         