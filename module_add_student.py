# add  student
def add_student():
    print("Add Student")

    roll = int(input("Enter roll number: "))
    name = input("Enter student name: ")

    mark1 = float(input("Enter Python marks: "))
    mark2 = float(input("Enter Mathematics marks: "))
    mark3 = float(input("Enter Programming marks: "))

    total =mark1 +mark2 +mark3
    average = total/3

    grade = calculate_grade(average)

    student = {"roll": roll,
                "name": name,
                "total": total,
              "average": average,
              "grade": grade}

    students.append(student)

    print("Student added successfully")
    print("Total marks:", total)
    print("Average:", average)
    print("Grade:", grade)
