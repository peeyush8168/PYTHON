'''Inheritence:It is a fundamental concept in object-oriented programming(OOP) that allows a 
class to inherit properties and behaviours from another class. 

5 types:
1. Single Inheritence
2. Multiple Inheritence
3. Multilevel Inheritence
4. Hierachical Inheritence
5. Hybrid Inheritence '''
'''
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")
   
# Creating an instance of the derived class
dog=Dog()

# Accessing methods from the base class
dog.speak()  # Output: Animal speaks

# Accessing methods from the derived class
dog.bark()   # Output: Dog barks
'''


'''Exp 9: write a program to implement an employee management system using classes, 
inheritence'''


'''Polymorphism: Is is an concept in OOP's that allows objects of different types to be
treated as objects of a common type. '''

'''Problem: Magic square'''
''' def is_magic_square(matrix):
    n = len(matrix)
    
    # Calculate the sum of the first row
    target_sum = sum(matrix[0])
    
    # Check the sum of rows
    if any(sum(row) != target_sum for row in matrix):
        return False

    # Check the sum of columns
    if any(sum(matrix[i][j] for i in range(n)) != target_sum for j in range(n)):
        return False

    # Check the sum of the main diagonal
    if sum(matrix[i][i] for i in range(n)) != target_sum:
        return False

    # Check the sum of the other diagonal
    if sum(matrix[i][n - 1 - i] for i in range(n)) != target_sum:
        return False

    return True

def get_matrix_from_user():
    try:
        n = int(input("Enter the size of the square matrix: "))
        matrix = []
        print("Enter the elements of the matrix row by row:")
        for i in range(n):
            row = list(map(int, input().split()))
            if len(row) != n:
                print("Invalid input. Please enter a square matrix.")
                return None
            matrix.append(row)
        return matrix
    except ValueError:
        print("Invalid input. Please enter integers.")
        return None

def main():
    matrix = get_matrix_from_user()
    if matrix is not None:
        if is_magic_square(matrix):
            print("The matrix is a magic square.")
        else:
            print("The matrix is not a magic square.")

if __name__ == "__main__":
    main() '''


# Calculator using switch case
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "not divide by zero"

def calculator(operation, x, y):
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    # Using get() method to handle invalid operation input
    selected_operation = operations.get(operation)

    if selected_operation:
        result = selected_operation(x, y)
        return result
    else:
        return "Invalid operation."

# Example usage:
operation = input("Enter operation (add, subtract, multiply, divide): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = calculator(operation, num1, num2)
print(f"Result: {result}")
