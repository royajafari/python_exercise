def edit_student(stu):
    student_id = int(input('For edit information of a student, enter the Student_id : '))
    for student in stu:
        if int(student['student_id']) == student_id:
            print('Name= '  , student['name'])
            print('Family= ', student['family'])
            print('Mager= ' , student['mager'])
            res = input('If you want edit enter "Y", else enter "N" ')
            if res == 'Y':
                name   = input('new name = ')
                family = input('new family = ')
                mager  = input('new mager = ')
    return {
        'student_id' : student_id,
        'name'       : name,
        'family'     : family,
        'mager'      : mager
    }

