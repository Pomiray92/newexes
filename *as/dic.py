
# def full_name(**kwargs):
#     print(kwargs)
#     first_name = kwargs["first_name"]
#     last_name = kwargs["last_name"]
#     return f"{first_name} {last_name}"


# print(full_name(first_name="Joe", last_name="Doe"))




# first_name = ""                 # Global variable
# def full_name():                
#     first_name = "Peer"         # Local variable(with local scope)
#     last_name = "someone"
#     # print(first_name, last_name)
    
#     def add_sir(name):
#         return f"Sir {name} {last_name}"
    
#     new_full_name = add_sir(first_name)
#     # return f"{first_name} {last_name}"
#     return new_full_name


# full_name()
# print(full_name())
    

# def full_name(first_name = input("What is your first name?: ")):
#     """
    
#     """
#     # first_name 
#     print(first_name)



last_name = {
    "First_Name": "Joe",
    "Last_name": "Doe"                
    }

# "Pass by reference" variables can change

def full_name(last_name):
    # variations 
    last_name["Last_name"] = "Hoffman"
    return last_name


print(last_name)

print(full_name(last_name))

print(last_name)