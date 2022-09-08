import sys

num1 = sys.argv[1]
num2 = sys.argv[3]
choice = sys.argv[2]

if choice == "-":
    print(int(num1)-int(num2))
elif choice == "+":
    print(int(num1)+int(num2))