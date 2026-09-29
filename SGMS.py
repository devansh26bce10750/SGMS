students=[]

# tool to calculate grade
def calculate_grade(average):
    def get_grade(avg):
     if avg >= 90:
        return "A+"
     elif avg >= 80:
        return "A"
     elif avg >= 70:
        return "B"
     elif avg >= 60:
        return "C"
     elif avg >= 50:
        return "D"
     return "F"
    
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

# display all students
def display_students():
    print("All students")

    if not students:
        print("No students added yet.")
        return

    for student in students:
        print("Roll Number:", student["roll"])
        print("Name:", student["name"])
        print("Total Marks:", student["total"])
        print("Average:", student["average"])
        print("Grade:", student["grade"])

# search student
def search_student():
    print("Search student")

    roll = int(input("Enter roll number:"))

    for student in students:
        if student["roll"] == roll:
            print("Student Found")
            print("Name:", student["name"])
            print("Total Marks:", student["total"])
            print("Average:", student["average"])
            print("Grade:", student["grade"])
            return

    print("Student not found")


# find topper
def highest_scorer():
    print("--- Highest Scorer ---")

    if not students:
        print("No students found")
        return

    highest = students[0]

    for student in students:
        if student["average"] > highest["average"]:
            highest =student

    print("Name:", highest["name"])
    print("Roll Number:", highest["roll"])
    print("Average:", highest["average"])
    print("Grade:", highest["grade"])

# Main menu
while True:

    print("=============================")
    print(" STUDENT GRADE MANAGEMENT")
    print("==============================")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Find Highest Scorer")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        display_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        highest_scorer()

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid")