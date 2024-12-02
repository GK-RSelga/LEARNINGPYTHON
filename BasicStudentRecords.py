# Initialize an empty list to store student names
student_list = []
# Import colorama for colored text output
import colorama
colorama.init()
# Print using colorama for the header of student names
print(colorama.Fore.GREEN + "\n=== Enter Student Names === " + colorama.Style.RESET_ALL)
# Using For loops to input the names of the student
for x in range(1, 4):
    # Prompt
