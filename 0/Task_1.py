# зробити звичайний калькулятор який може + - * /

a = float(input("First number: "))
b = float(input("Second number: "))
operation = input("Operation: ")

result = None

if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    result = a / b
else:
    print("Unsupported operation")

if result is not None:
    print("Result: ", result)
