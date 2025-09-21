num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
        
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
        
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
        
    case "/":
        if num1 == 0 or num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
        
        