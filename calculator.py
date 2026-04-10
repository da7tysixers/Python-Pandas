prompt = "Enter an operation (+, -, *, /) and two numbers: "
user_input = input(prompt)
operation, num1, num2 = user_input.split(",")
num1 = float(num1)
num2 = float(num2)

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "Invalid operation"

print("Result:", result)
