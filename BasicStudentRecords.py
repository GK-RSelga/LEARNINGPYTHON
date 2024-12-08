# Initialize an empty list to store student names
student_list = []
# Import colorama for colored text output
import colorama
colorama.init()
# Print using colorama for the header of student names
print(colorama.Fore.GREEN + "\n=== Enter Student Names === " + colorama.Style.RESET_ALL)
# Using For loops to input the names of the students
for x in range(1, 4):
    # Prompt the user to enter the names of the students
    student_name = input(f"Enter the name of the student {x}: ")
    # Convert the student's name to title case
    student_name = student_name.title()
    # Append the students name to the list
    student_list. append(student_name)
# Print header for student list
print(colorama.Fore.GREEN + "\nList of Students: " + colorama.Style.RESET_ALL)
# Using For Loops for the list of the students with their index that will start=1
for index, student_name in enumerate(student_list, start=1):
    # Print the student names with their index
    print(f"{index}. {student_name}")
# Print using colorama for the header of the grades of each students
print(colorama. Fore.GREEN + "\n=== Enter Grades for Each Students === " + colorama.Style.RESET_ALL)
# Define a function to input student grades
def enter_grades(student_name):
    # Print header of enter grades for student
    print(f"Enter Grades for {student_name}:")
    # Using While True Loop (try, except) until the input grades is valid
    while True:
        try:
            # Prompt user to enter the grades for each subjects
            math_grade = float(input("Math grade: "))
            science_grade = float(input("Science grade: "))
            history_grade = float(input("History grade: "))
            print("")
            # To calculate the average grade of the 3 subjects
            average = (math_grade + science_grade + history_grade) / 3
            # Use an If, else statement for the average passing score result
            if average >= PASSING_SCORE:
                result = "Pass"
            else:
                result = "Fail"
            # To return the grades, average and result as tuples
            return (math_grade, science_grade, history_grade, round(average,2), result)
        # For invalid input of non numerical values
        except ValueError:
            print("Invalid input.")
            print("Please enter numerical grades only. Try again.")
# Import tabulate for the table
from tabulate import tabulate
# Initialize an empty list [] to store the student names and grades on the student's table
students_table = []
# Using For Loops to the student list with their index which start=1
for index, student_name in enumerate(student_list, start=1):
    # Call each grades, average and result using the enter_grades function
    math_grade, science_grade, history_grade, average, result = enter_grades(student_name)
    # Append students name, grades (rounded by 2), average grade and result to the table
    students_table.append([index, student_name, round(math_grade,2), round(science_grade,2), round(history_grade,2), average, result)])
# Create headers or first row for the table
headers = [colorama. Fore.GREEN + "No." + colorama.Style.RESET_ALL, colorama. Fore.GREEN + "Student Name" + colorama.Style.RESET_ALL, colorama. Fore.GREEN + "Math" + colorama.Style.RESET_ALL,
           colorama. Fore.GREEN + "Science" + colorama.Style.RESET_ALL, colorama. Fore.GREEN + "History" + colorama.Style.RESET_ALL, colorama. Fore.GREEN + "Average" + colorama.Style.RESET_ALL,
           colorama. Fore.GREEN + "Result" + colorama.Style.RESET_ALL]
# Print tables using tabulate
print(tabulate(students_table, headers=headers, tablefmt="fancy_grid"))
# Initialize an empty set() to store unique subjects
unique_subjects = set()
# Print using colorama for the header of unique subjects
print(colorama.Fore.GREEN + "\n=== Enter Unique Subjects === " + colorama.Style.RESET_ALL)
# Using For Loops to input the unique subjects
for x in range(1, 4):
    # Ask the user to input unique subjects
    subject = input(f"Enter Subject {x}: ")
    # Using add to add the subjects to the sets
    unique_subjects.add(subject)
# Print using colorama for the header unique subjects offered
print(colorama.Fore.GREEN + "\nUnique Subjects Offered:" + colorama.Style.RESET_ALL)
# To loop to the set of unique subjects
for subject in unique_subjects:
    # Print each unique subjects offered
    print(f"- {subject}")

