num1 = float(input("Write a number: "))
operator = str(input("Choose an operator: "))
num2 = float(input("Write a second number: ")) 

def calc(num1, num2, operator):
    if operator == "+":
        result = num1 + num2
    if operator == "-":
        result = num1 - num2
    if operator == "*":
        result = num1 * num2
    if operator == "/":
        result = num1 / num2
    return result


print(calc(num1, num2, operator))