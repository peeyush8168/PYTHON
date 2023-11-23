'''Relational Operators: Relational operators, also known as comparison operators, are used in 
programming to compare values and determine the relationship between them. '''
# Relational operators: <,>,==,!=,<=,>=
''' a=5
b=5
if (a==b):
    print("a is equal to b")
a=4
b=6
if (a<b):
    print("a is less than b")
a=6
b=4
if (a>b):
    print("a is greater than b")
a=1
b=3
if (a!=b):
    print("a is not equal to b")
a=5
b=6
if (a<=b):
    print("a is less than or equal to b")
a=6
b=4
if (a>=b):
    print("a is greater than or equal to b") '''


'''Logical Operators: These operators in python are used to perform logical operations on
Boolean values(True and False) or expressions that evaluate to Boolean values. These operations
allow us to combine and manipulate Boolean values to make decisions and control the flow of your
program. '''
''' x=10
y="peeyush10"

if (x.isalnum() and y.isalnum()):
    print("Both x and y are true")
elif(x.isalnum() or y.isalnum()):
    print("Either x or y is true")
elif(x.notisalnum()):
    print("x is not true") '''
    
''' Bitwise Operator: USed to perform bit-level operations on integers. '''
''' x=5
y=3
result=x&y 
print(result) '''

#AND operator- 0,0 = 0, 0,1 = 0, 1,1 = 1, 1,0 = 0 
#XOR operator- same 0 and for different 1


''' my_list = []
my_dict = {
    "Name": ["Peeyush","Ayushman","Gagandeep","Aryan"],
    "Roll no.": [32,5,18,1],
    "Age": [18,20,19,23]
}
my_list.append(my_dict)
another_dict={
    "Name":["ABC"],
    "Roll no.": [24],
    "Age": [10]
    }
my_list.append(another_dict)
print(my_list) '''



student_data = {
    101: {"Name": "Peeyush", "Age": 18, "Grade": "A"},
    102: {"Name": "Gagandeep", "Age": 19, "Grade": "A"},
    103: {"Name": "Ayushman", "Age": 21, "Grade": "A"},
    104: {"Name": "Aryan", "Age": 22, "Grade": "A"},
}
def add_student_record():
    name=input("Enter the name of the student: ")
    age=input("Enter the age: ")
    grade=input("Enter the grade: ")
    student_record={'Name':name,'Age':age,'Grade':grade}
    student_data.append(add_student_record)
    print(student_data)
def search_student_by_name(name):
    for student_id, student_info in student_data.items():
        if student_info["name"].lower() == name.lower():
            return student_id, student_info
    return None
while True:
    print("\nStudent Search Menu:")
    print("1. Search by Name")
    print("2. Add student")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        name = input("Enter the name of the student: ")
        result = search_student_by_name(name)
        if result:
            student_id, student_info = result
            print(f"Student ID: {student_id}")
            print(f"Name: {student_info['name']}")
            print(f"Age: {student_info['age']}")
            print(f"Grade: {student_info['grade']}")
        else:
            print("Student not found.")
    if choice =="2":
        student_data.append(add_student_record)
        print(student_data)
    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1 or 2")
