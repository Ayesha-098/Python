num = input("Enter a number (any): ")
digit = input("Enter a digit to find its place value: ")  
 
places = ["Units", "Tens", "Hundreds", "Thousands", "Ten Thousands", "Hundred Thousands", "Millions"]
index = len(num) - num.index(digit) - 1 
print(f"Place value of {digit}: {places[index]}")
