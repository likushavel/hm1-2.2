import time
import random

a = random.randint(1, 10)
b = random.randint(1, 10)
operation = input("Enter mathematical operation (+, -, *, /):")

if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
else:
    result = a / b

print("Result:", result)
time.sleep(2)
user_input = float(input("Enter your predicted result:"))

if user_input == result:
    print("You guessed it!")
else:
    print("Sorry, you did not guess correctly.")