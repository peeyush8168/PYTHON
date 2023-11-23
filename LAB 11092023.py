# Examples of Passing Immutable Arguments
#1
a=10

def change_value(a):
    a=20
    print("Inside function, address: ",id(a))
    return a

print("Before function call, a= ",a,"address: ",id(a))
a=change_value(a)
print("After function call, a= ",a,"address: ",id(a))

#2
my_list=[1,2,3,4,5,6]

def change_value(my_list):
    my_list[3]=30
    print("Value inside the list:",my_list)
    print("Address is:",id(my_list)) #Print the memory address
    return
print("Before function call,my_list:",my_list)
print("Address:",id(my_list)) #Print the memory address
change_value(my_list)
print("After function call,my_list:",my_list)
print("Address:",id(my_list)) #Print the memory address

# Default Argument Values
def function1(a,b=90):
# This prints a passed info into this function
    print("Value of a: ",a)
    print("Value of b: ",b)
    return
# Call function1 function
function1(a="Monika",b=50)
function1(a="Lalit")