# Our First Python Assignment – PLP Academy

#Procedures:
# Ask the Calc user to enter two numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# We then Convert the input to numbers wiyth decimals(float)
num1 = float(num1)
num2 = float(num2)

# We then ask the user to choose an operation
operation = input("Choose operation (+, -, *, /): ")

# Operations and calculations
if operation == "+":
    print(num1 + num2)

elif operation == "-":
    print(num1 - num2)

elif operation == "*":
    print(num1 * num2)

elif operation == "/":
    print(num1 / num2)
    
else:
    print("Invalid operation")
