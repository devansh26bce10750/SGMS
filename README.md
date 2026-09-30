# Student Grade Management System

# Project Overview

The **Student Grade Management System (SGMS)** is a Python-based console application designed to manage student academic records. The system allows users to add student details, display all students, search for a particular student, and identify the highest scorer.

The project is organized into multiple Python modules, with each module responsible for a specific functionality. The main program connects these modules and provides a simple menu-driven interface.

# Objectives

The main objectives of this project are:

* To create a simple student record management system.
* To store student information using Python data structures.
* To calculate total marks and average marks.
* To automatically assign grades based on the student's average.
* To search for students using their roll number.
* To display all registered students.
* To identify the student with the highest average score.
* To demonstrate the use of Python modules and functions.

---

# Features

The Student Grade Management System provides the following features:

1. **Add Student**

   * Enter roll number and student name.
   * Enter marks for Python, Mathematics, and Programming.
   * Calculate total marks.
   * Calculate average marks.
   * Automatically calculate the grade.

2. **Display All Students**

   * Displays all students currently stored in the system.
   * Shows roll number, name, total marks, average, and grade.

3. **Search Student**

   * Searches for a student using their roll number.
   * Displays the student's academic details if found.
   * Displays a "Student not found" message if no matching roll number exists.

4. **Find Highest Scorer**

   * Checks all students.
   * Finds the student having the highest average.
   * Displays the student's name, roll number, average, and grade.

5. **Exit**

   * Terminates the program.

# Project Structure

```text
Student-Grade-Management-System/
│
├── SGMS(1).py
├── module_add_student.py
├── module_display_students.py
├── module_grade.py
├── module_highest_scorer.py
├── module_search_student.py
└── README.md
```

# Module Description

### 1. `SGMS(1).py`

This is the **main program file**. It imports all the required modules, creates the student list, connects the modules with the shared student data, and displays the main menu.

The main menu contains:

```text
1. Add Student
2. Display All Students
3. Search Student
4. Find Highest Scorer
5. Exit
```

The program continues running until the user selects the Exit option.

---

### 2. `module_add_student.py`

This module is responsible for adding a new student.

The user provides:

* Roll number
* Student name
* Python marks
* Mathematics marks
* Programming marks

The program then calculates:

```text
Total = Python + Mathematics + Programming
Average = Total / 3
```

The calculated grade is obtained using the grade calculation function. The student information is then stored in the `students` list.

---

### 3. `module_display_students.py`

This module displays all students stored in the system.

For every student, it displays:

```text
Roll Number
Name
Total Marks
Average
Grade
```

If no students have been added, the program displays:

```text
No students added yet.
```

---

### 4. `module_grade.py`

This module contains the function responsible for calculating grades.

The grading criteria used in the project are:

| Average Marks | Grade |
| ------------: | :---: |
|   90 or above |   A+  |
|         80–89 |   A   |
|         70–79 |   B   |
|         60–69 |   C   |
|         50–59 |   D   |
|      Below 50 |   F   |

The grade is calculated from the student's average marks.

---

### 5. `module_search_student.py`

This module allows the user to search for a student using their roll number.

If the roll number matches a student, the program displays:

```text
Student Found
Name
Total Marks
Average
Grade
```

If there is no matching student, the program displays:

```text
Student not found
```

---

### 6. `module_highest_scorer.py`

This module identifies the student with the highest average marks.

The program compares the average of each student and selects the student with the highest average.

It displays:

```text
Name
Roll Number
Average
Grade
```

---

## 🔄 Program Flow

The overall working of the system can be represented as:

```text
Start
  │
  ▼
Display Main Menu
  │
  ├── 1. Add Student
  │       │
  │       ├── Enter student details
  │       ├── Calculate total
  │       ├── Calculate average
  │       └── Calculate grade
  │
  ├── 2. Display All Students
  │       │
  │       └── Display stored student records
  │
  ├── 3. Search Student
  │       │
  │       └── Search using roll number
  │
  ├── 4. Find Highest Scorer
  │       │
  │       └── Find highest average
  │
  ├── 5. Exit
  │       │
  │       └── End Program
  │
  └── Invalid Choice
          │
          └── Display "Invalid"
```

---

## 🧮 Grade Calculation

The system calculates the average using the three subject marks:

```text
Average = (Python Marks + Mathematics Marks + Programming Marks) / 3
```

The grade is then assigned according to the average:

```text
Average >= 90  → A+
Average >= 80  → A
Average >= 70  → B
Average >= 60  → C
Average >= 50  → D
Otherwise      → F
```

---

## 💻 Requirements

To run this project, you need:

* Python 3.x
* A Python-compatible IDE or code editor
* Terminal/Command Prompt

No external Python libraries are required because the project uses standard Python functionality and user-defined modules.

---

## ▶️ How to Run

### Step 1: Clone or download the project

Place all the Python files in the same directory.

### Step 2: Open the project directory

Open the folder in a Python IDE such as VS Code, PyCharm, or any other Python-supported editor.

### Step 3: Run the main file

Run:

```bash
python "SGMS(1).py"
```

### Step 4: Select an option

The application will display:

```text
=============================
 STUDENT GRADE MANAGEMENT
==============================
1. Add Student
2. Display All Students
3. Search Student
4. Find Highest Scorer
5. Exit
```

Enter the number corresponding to the operation you want to perform.

# things Used

* **Programming Language:** Python
* **Application Type:** Console-based application
* **Data Structure:** Python List and Dictionary
* **Programming Concepts:**

  * Functions
  * Modules
  * Conditional statements
  * Loops
  * Lists
  * Dictionaries
  * User input
  * Function importing

# Learning Outcomes

Through this project, the following Python concepts are demonstrated:

* Creating and using Python functions.
* Creating multiple Python modules.
* Importing functions from different modules.
* Working with lists and dictionaries.
* Using conditional statements for grade calculation.
* Using loops to process student records.
* Taking input from users.
* Implementing a menu-driven console application.
* Sharing data between different modules.

# Author

**Name:** Devansh Tripathi
**Course:** B.Tech CSE
**University:** Vellore Institute of Technology, Bhopal

# Conclusion
The **Student Grade Management System** is a simple Python-based project that demonstrates how different programming concepts can be combined to create a functional student management application.

The modular structure makes the program easier to understand by separating individual functionalities such as adding students, displaying records, searching students, calculating grades, and finding the highest scorer.

# Project Modules used

| File                         | Purpose               |
| ---------------------------- | --------------------- |
| `SGMS(1).py`                 | Main program and menu |
| `module_add_student.py`      | Adds student records  |
| `module_display_students.py` | Displays all students |
| `module_grade.py`            | Calculates grades     |
| `module_search_student.py`   | Searches students     |
| `module_highest_scorer.py`   | Finds highest scorer  |
| `README.md`                  | Project documentation |
