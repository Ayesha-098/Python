# For user to enter number and operator
num1 = float(input("Enter first number: ")) 
num2 = float(input("Enter second number: "))
operator = input("Enter operator ( +, *, / -): ")

# Using try and except for exception handling
try: 
    if operator == "+":
        result = num1 + num2 # for addition
    elif operator == "*":
        result = num1 * num2 # for multiplication
    elif operator == "/":
        result = num1 / num2 # for division
    elif operator == "-":
        result = num1 - num2 # for subtraction

    print(f"Result: {result}") # printing the result

# Zero division error handling 
except(ZeroDivisionError): 
   print("Error, dividing by zero is not allowed")
