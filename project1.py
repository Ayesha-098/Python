numbers = []

while True:
    num = float(input("Enter number (-1 to stop): " ))
    if num == -1:
        break
    numbers.append(num)

if numbers:
    average = sum(numbers) / len(numbers)
    print(f"Average of numbers entered: {average:.2f}")
else:
    print("No average because there is no number")