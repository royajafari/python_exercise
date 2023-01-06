from add_student import add_student
from edit_student import edit_student
from main_menu import main_menu
from remove_list import remove_list
from search_student import search_student
from show_students import show_students

print("Hello, This is CRUD menu for students")
choice = main_menu()

students =[
    {
        "student_id" : "1",
        "name"       : "Roya  ",
        "family"     : "Jafari",
        "mager"      : "Computer"
    },
    {
        "student_id" :  "2",
        "name"       :  "Rahile",
        "family"     :  "Jafari",
        "mager"      :  "Plasma"
    }
]

while choice != 0:
    if   choice == 1:
#         Show all students
          show_students(students)
    elif choice == 2:
#        Add new student
         new_student = add_student()
         students.append(new_student)
         show_students(students)
    elif choice == 3:
#       Edit Student information
        edited_list = edit_student(students)
        rem_student_id = edited_list['student_id']
        for student in students:
            if int(student['student_id']) == rem_student_id:
                students.pop(rem_student_id-1)
        students.append(edited_list)
        show_students(students)
    elif choice == 4:
#      Remove a student from list
        remove_list(students)
    elif choice == 5:
#      Search a student in list
        search_student(students)
    choice = main_menu()