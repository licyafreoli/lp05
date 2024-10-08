def calculate_average(grades):
    return sum(grades) / len(grades)

num_students = int(input("Enter the number of students: "))

total_class_average = 0

for i in range(num_students):
    print(f"\nStudent {i+1}")
    student_name = input("Enter the student's name: ")
    grades = []
    for j in range(1, 4):
        grade = float(input(f"Enter grade {j} for {student_name}: "))
        grades.append(grade)

    student_average = calculate_average(grades)

    if student_average >= 7.0:
        status = "Approved"
    else:
        status = "Failed"

    print(f"\nName: {student_name}")
    print(f"Grades: {grades}")
    print(f"Average: {student_average:.2f}")
    print(f"Status: {status}")

    total_class_average += student_average

class_average = total_class_average / num_students
print(f"\nClass average: {class_average:.2f}")
