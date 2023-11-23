# CLASSES and OBJECTS:-
# Classes and objects are a powerful way to model and organise code in python. 
# It promote code reusable.
# CLASS:-
''' A class is a blueprint or a template for creating objects.
It defines a set of attributes(variables) and methods(functions) that objects created from
the class will have.
Classes provide a way to encapulate data and behaviour into a single unit, which promote 
modularity and code reusability. '''
# OBJECT:-
''' An object is an instance of a class. It is a concrete realization of the blueprint defined 
by the class.
Objects are created from a class, and each subject has its own unique set of attribute values, 
even through the attributes and methods are defined in the class. '''


''' class Adder:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def add(self):
        return self.n1 + self.n2
    def subtract(self):
        return self.n1 - self.n2
    def divide(self):
        return self.n1 / self.n2
    def multiply(self):
        return self.n1 * self.n2
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
print("****Enter from the following options****")
print("1. Addition")
print("2. Subtract")
print("3. Divide")
print("4. Multiply")
choice=input("Enter your choice: ")
if (choice=="1"):
    Addition=Adder(a,b)
    result=Addition.add()
    print(f"Sum of {Addition.n1} and {Addition.n2} is {result}") 
if (choice=="2"):
    Addition=Adder(a,b)
    result=Addition.subtract()
    print(f"Subtraction of {Addition.n1} and {Addition.n2} is {result}") 
if (choice=="3"):
    Addition=Adder(a,b)
    result=Addition.divide()
    print(f"Division of {Addition.n1} and {Addition.n2} is {result}")
if (choice=="4"):
    Addition=Adder(a,b)
    result=Addition.multiply()
    print(f"Multiplication of {Addition.n1} and {Addition.n2} is {result}")  '''


'''for i in range (0,6):
    print(" *"*i) '''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print() '''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" " * (n-i) + "* "*i) '''

'''n=int(input("Enter the number of rows: "))
for i in range(n,0,-1):
    print(" " * (n-i) + "* "*i)'''
    
'''n=int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print(" " * (n-i) + "* " * i)  
print(" " * (n-1))
for i in range(n - 1, 0, -1):
    print(" " * (n-i) + "* " *i)'''
    
