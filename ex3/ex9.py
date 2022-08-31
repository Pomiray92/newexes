

secret = "This is my secret"
secret_name = "Max"
secret_year = "1982"
for user in range(3):
    user = input("Do you wont to now my secret? ")

    # How are you Somon

    if user == "*secret:*":
        print(secret[::-1])

    elif user == "*name:*":
        print(secret_name[::-1])

    elif user == "*year:*":
        print(secret_year[::-1])

    else:
        print("Password entered incorrectly! Maybe next time? Good Look!")