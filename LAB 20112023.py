'''def input(name):
    print(f"hi{name}")
a=input("enter")
print(a) '''

'''Function:- A function is a reusable and self-contained block of code that performs a specific
task or a set of related tasks. '''

'''
# Passing List
my_list = [1, 2, 3, 4, 5]
def my_function(input_list):
    for item in input_list:
        print(item)
my_function(my_list)


# Passing Dictionaries
my_dict = {1: 'a', 2: 'b', 3: 'c'}
print(my_dict[1])
print(my_dict[2]) 
print(my_dict[3])
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")


# Passing Tuples
my_tuple = ('a', 'b', 'c', 'd', 'e')
first_element = my_tuple[0]  
second_element = my_tuple[1] 
third_element = my_tuple[2]  
fourth_element = my_tuple[3] 
fifth_element = my_tuple[4]  
for element in my_tuple:
    print(element)
    '''
    
# Check right angled triangle
def is_right_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()
    
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("It's a right-angled triangle.")
    else:
        print("It's not a right-angled triangle.")

def area_triangle(a,b,c):
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print("Area of triangle: ",area)
    
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
is_right_triangle(a, b, c)
area_triangle(a,b,c)
