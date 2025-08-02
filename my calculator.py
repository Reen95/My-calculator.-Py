simple calculator 
print("my calulator.py")

# Get user input
num1 = float(input("Enter first number: "))
operator = input("Choose operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Perform calculation
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero!"
else:
    result = "Invalid operator!"

# Show result
print("Result:", result) 
Enter first number: 10
Choose operation (+, -, *, /): +
Enter second number: 5
Result: 15.0
Finished

