# Question
#List of tupples
list=[
      (1001,"Peeyush",18,"Male",("Maths","Science","C")),
      (1002,"Ayushman",20,"Male",("Maths","Science")),
      (1003,"Saksham",19,"Male",("Maths","C","Physics")),
      (1004,"Aryan",19,"Male",("C","Physics")),
      (1005,"Gagandeep",19,"Male",("Maths","Science")) ,]

# Function to calculate average age of all students
def average_age(list):
    total_age=sum(student[2]for student in list)
    return total_age/len(list)
print("Average age: ",average_age(list))

# Function to find the student with most subjects enrolled
def most_subjects_enrolled(list):
    return max(list,key=lambda x:len(x[4]))
print("Student with most subjects enrolled: ",most_subjects_enrolled(list))

# Function to find the student with mimimum subjects enrolled
def least_subjects_enrolled(list):
    return min(list,key=lambda x:len(x[4]))
print("Student with least subjects enrolled: ",least_subjects_enrolled(list))