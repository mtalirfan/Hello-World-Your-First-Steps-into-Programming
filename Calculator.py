def calc(operator, num1, num2):
    if (operator == "+"):
        return num1 + num2

    elif (operator == "-"):
        return num1 - num2

    elif (operator == "*"):
        return num1 * num2

    elif (operator == "/"):
        return num1 / num2

    elif (operator == "%"):
        return num1 % num2

    elif (operator == "**"):
        return num1 ** num2

    else:
        return "Invalid operator"

print("Welcome to the calculator program!")

print("Here are the available operators:")
print("+ for addition")
print("- for subtraction")
print("* for multiplication")
print("/ for division")
print("% for modulo")
print("** for exponentiation")
print("q to quit")

while (True):
    op = input("Enter the operator: ")
    if (op == "q"):
      break
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    print("The result is: " + str(calc(op, int(num1), int(num2))))