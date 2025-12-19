class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Multiply two numbers.

        Args:
            cls: The class object (implicit parameter for class methods).
            a: The first number to multiply.
            b: The second number to multiply.

        Returns:
            The product of a and b.
        """
        #prints a class attribute named calculation_type before performing the multiplication.
        print(f"Calculation type: {cls.calculation_type}")  
        return a * b

# Setting a class attribute
    class calculation_type:
        calculation_type = "Arithmetic Operations"
        
class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()