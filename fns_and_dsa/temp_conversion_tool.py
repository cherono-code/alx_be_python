FAHRENHEIT_TO_CELSIUS = 5 / 9
CELSIUS_TO_FAHRENHEIT = 9 / 5

temperature = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT + 32

if unit == "C":
    result = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {result}°F")
elif unit == "F":
    result = convert_to_celsius(temperature)
    print(f"{temperature}°F is {result}°C")
else:
    print("Invalid unit entered.")