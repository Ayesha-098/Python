num_students = int(input("Enter the number of students: "))
grades = []

for i in range(num_students):
    grade = float(input(f"Enter Marks for student {i+1}: "))
    grades.append(grade)

average = sum(grades) / num_students
highest = max(grades)
lowest = min(grades)

print(f"Average Marks: {average:.2f}")
print(f"Highest Marks: {highest}")
print(f"Lowest Marks: {lowest}")

