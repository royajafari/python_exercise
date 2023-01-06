def search_student(stu):
    search_id = int(input('which student do you pursue?, please enter student_id: '))
    for student in stu:
        if int(student['student_id'])  == search_id:
            print('Result :')
            print('Student_id: ',student['student_id'])
            print('Name: '      ,student['name'])
            print('Family: '    ,student['family'])
            print('Mager: '     ,student['mager'])
