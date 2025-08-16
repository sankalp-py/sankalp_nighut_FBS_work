def calculator():
    try:
        num1 = float(input("Enter first number: "))

        operator = input("Enter operator (+, -, *, /): ")

        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            try:
                result = num1 / num2
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")
                return
        else:
            raise ValueError("Invalid operator")

        print(f"Result: {num1} {operator} {num2} = {result}")

    except ValueError as ve:
        if str(ve) == "Invalid operator":
            print("Error: Please enter a valid operator (+, -, *, /).")
        else:
            print("Error: Invalid number entered. Please enter numeric values only.")

calculator()
