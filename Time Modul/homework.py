import time
import sys

mash_time = time.time()
hum_time = time.ctime(mash_time)

time.sleep(0.5)

print("Start Time: ", hum_time)

mash_time2 = time.time()
hum_time2 = time.ctime(mash_time2)

time.sleep(0.5)

print("End Time: ", hum_time2)
time.sleep(0.5)
count_time = (mash_time2 - mash_time)
print("Counting Time", count_time)