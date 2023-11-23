# Built in functions

# Calculator
import math
print("\n****WELCOME TO MY CALCULATOR****\n")

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

print("What do you want to choose from the following")
print(' 1. ADD\n','2. SUB\n','3. MUL\n','4. DIV\n','5. MOD\n','6. POWER\n','7. ROOT\n','8. Factrial')
user_input = str(input("Enter your option: "))

def factorial(a):
  fact = 1
  for i in range(2, a + 1):
    fact *= i
  return fact
if user_input == "1":
    print("You chose sum")
    print("The sum is: ",a+b)
elif user_input == "2":
    print("You chose sub")
    print("The sub is: ",a-b)
elif user_input == "3":
    print("You chose mul")
    print("The mul is: ",a*b)
elif user_input == "4":
    print("You chose div")
    print("The div is: ",a/b)
elif user_input == "5":
    print("You choose mod")
    print("The mod is: ",a%b)
elif user_input == "6":
    print("You choose power")
    print("The power is: ",a**b)
elif user_input == "7":
    print("You choose root")
    print("The root of number a is: ",math.sqrt(a))
    print("The root of number b is: ",math.sqrt(b))
elif user_input == "8":
    print("You choose factorial")
    print("The factorial of a is: ",factorial(a))
    print("The factorial of b is: ",factorial(b))
else:
    print("Invalid command")


'''
int a=10
int b=20
for (int i=1;1<=a;i++):
    {
    a++ 
    }
print(a)
'''

'''
name=str(input("Enter your name: "))
age=str(input("Enter your age: "))
print("My name is",name,"and my age is",age)
'''
