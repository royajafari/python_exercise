def remove_list(stu):
    res       = 0
    rem_index = int(input('please enter student_id for remove from list: '))
    for student in stu:
        if int(student['student_id'])  == rem_index :
            res = 1
            print('res = ',res)
    if res == 1:
        stu.pop(rem_index-1)
        print('Student_id = ',rem_index,' was deleted')