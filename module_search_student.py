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
