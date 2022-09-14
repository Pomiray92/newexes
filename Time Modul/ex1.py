import time

# EXERCISE:
# Create a program that
# - saves current time and prints it
# - saves another time moment and prints it
# - prints the time that has passed in between


start_time = time.time()


machtime = time.time()
humtime = time.ctime(machtime)
time.sleep(0.5)
print("Time begin: ", humtime)

time.sleep(1)
print("###5###")
time.sleep(1)
print("###4###")
time.sleep(1)
print("###3###")
time.sleep(1)
print("###2###")
time.sleep(1)
print("###1###")

machtime2 = time.time()
humtime2 = time.ctime(machtime2)
time.sleep(1)
print("End Time: ", humtime2)


stop_time = time.time()

elapsed_time = (stop_time - start_time)
time.sleep(0.5)
print("Time in between: ", stop_time - start_time)
