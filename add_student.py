def add_student():
    print("insert on the request: ")
    student_id = input("Student_id= ")
    name       = input("name= ")
    family     = input("family= ")
    mager      = input("mager= ")
    return{
        'student_id': student_id,
        'name'      : name,
        'family'    : family,
        'mager'     : mager
    }