# This function performs basic arithmetic operations based on user input.
def perform_operation(num1, num2, operation):
    match operation:
        #addition
        case "add":
            result = num1 + num2
            return result
         #subtraction   
        case "subtract":
            result = num1 - num2
            return result
         #multiplication   
        case "multiply":
            result = num1 * num2
            return result 
        #division    
        case "divide":
            if num1 == 0:
                return print("Cannot divide by zero.")
            elif num2 == 0:
                return print("Cannot divide by zero.")
            else:
                result = num1 / num2
                return result
        #invalid operation    
        case _:
            return print("Invalid operation. Please choose from add, subtract, multiply, or divide.")
