import time

userimp = int(input("Take a number: "))

mash_time = time.time()
humtime = time.ctime(mash_time)
time.sleep(0.5)
print("Begin Time: ", humtime)

start_time = time.time()

if userimp > 0:
    for i in range(userimp, 0, -1):
        time.sleep(0.5)
        print(i)

stop_time = time.time()

mash_time2 = time.time()
humtime2 = time.ctime(mash_time2)
time.sleep(0.5)
print("End Time: ", humtime2)

count_time = (stop_time - start_time)
time.sleep(0.5)
print("Countdown Time: ", count_time)        