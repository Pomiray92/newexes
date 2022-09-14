import time

userimp = int(input("Take a number: "))


if userimp > 0:
    for i in range(userimp, 0, -1):
        time.sleep(0.5)
        print(i)

          