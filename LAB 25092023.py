# Conversion

'''
# 1. Type conversion
a=int(input("Enter the int value: "))
b=str(a)
print(b)
'''

'''
# 2. Explicit conversion 
d=10
e=2.0
f=d+e
print(f)
'''

'''
# 3. Binary octal hexadecimal conversion
a=int(input("Enter the number which you want to convert: "))
c=bin(a)
print(c)
d=oct(a)
print(d)
e=hex(a)
print(e)
'''

'''
# if else
a=int(input("Enter the number: "))
if(a<10):
    print("The number is less than 10")
elif(a==10):
    print("The number is equal to 10")
else:
    print("The number is greater than 10")
'''
    

# Number is odd or even
a=int(input("Enter the number: "))
if(a%2==0):
    print("The number is even")
elif(a==2):
    print("The number is even")
elif(a==1):
    print("The number is neither even nor odd")
else:
    print("The number is odd")