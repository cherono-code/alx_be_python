def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            result = num1 + num2
            return result
            
        case "subtract":
            result = num1 - num2
            return result
            
        case "multiply":
            result = num1 * num2
            return result 
            
        case "divide":
            if num1 == 0 or num2 == 0:
                return print("Cannot divide by zero.")
            else:
                result = num1 / num2
                return result
            
        case _:
            return print("Invalid operation. Please choose from add, subtract, multiply, or divide.")
# Example usage: