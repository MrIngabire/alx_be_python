# match_case_calculator.py

# Prompt user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt user to choose the operation
operation = input("Choose the operation (+, -, *, /): ")

# Perform calculation based on user's choice using match case
match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
    case _:
        print(f"Invalid operation '{operation}'. Please choose from '+', '-', '*', '/'.")

# Print the result if operation was valid
if operation in {'+', '-', '*', '/'}:
    print(f"The result is {result}.")
