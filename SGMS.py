from module_grade import calculate_grade
import module_add_student
import module_display_students
import module_search_student
import module_highest_scorer

students = []

module_add_student.calculate_grade = calculate_grade
module_add_student.students = students
module_display_students.students = students
module_search_student.students = students
module_highest_scorer.students = students

add_student = module_add_student.add_student
display_students = module_display_students.display_students
search_student = module_search_student.search_student
highest_scorer = module_highest_scorer.highest_scorer

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
