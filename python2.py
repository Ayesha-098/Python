# for user to enter a number 
n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n + 1):  
    factorial *= i  # Multiply the current value of factorial by i

# Print the computed factorial
print(f"The factorial of {n} is {factorial}.")

