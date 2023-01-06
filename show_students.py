from operator import itemgetter

from sorted_list import sorted_list


def show_students(stu):
    print("STUDENT_ID",'\t\t\t', 'NAME','\t\t\t\t','FAMILY','\t\t\t', 'MAGER','\t\t\t')
    stu.sort(key=sorted_list)
    for student in stu:
        print(student['student_id'],'\t\t\t\t\t',
              student['name'],'\t\t\t',
              student['family'],'\t\t\t',
              student['mager'])

