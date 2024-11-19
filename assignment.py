def calculator():
    # User to input two numbers and an operation
    num1 = int(input("Enter the first number: "))
    operation = input("Enter an operation (+, -, *, /): ")
    num2 = int(input("Enter the second number: "))
    

    # Perform the operation based on user input
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please enter one of +, -, *, /.")


calculator()