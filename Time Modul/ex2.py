import time
import sys

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
        
print()

userimp = int(input(print_slow("Take a number: ")))


mash_time = time.time()
humtime = time.ctime(mash_time)

time.sleep(0.5)

print_slow("Begin Time: ")
print_slow(humtime)

print()

start_time = time.time()

if userimp > 0:
    for i in range(userimp, 0, -1):
        time.sleep(0.5)
        print("###",i,"###")

stop_time = time.time()

mash_time2 = time.time()
humtime2 = time.ctime(mash_time2)
time.sleep(0.5)

print_slow("End Time: ")
print_slow(humtime2)
print()

count_time = (stop_time - start_time)

time.sleep(0.5)
print_slow("Countdown Time: ")
print_slow(str(count_time))

print()
print()         