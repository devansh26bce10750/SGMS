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
