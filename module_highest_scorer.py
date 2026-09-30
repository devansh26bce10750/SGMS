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
