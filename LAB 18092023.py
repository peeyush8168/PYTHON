# Remove function from a list

# 1
num = [10, 30, 40]
num.insert(1, 20)
print(num)

languages = ['Python', 'Swift', 'C++']
languages[2] = 'C'
print(languages)

languages = ['a', 'b', 'c', 'd']
del languages[1]
print(languages)

languages = ['a', 'b', 'c', 'd']
del languages[-1]
print(languages)

languages = ['a', 'b', 'c', 'd']
del languages[0:2]
print(languages)

languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'PHP', 'R']
languages.remove('Python')
print(languages)

# 2
# Create a list named numbers containing integers from 1 to 10
list=[1,2,3,4,5,6,7,8,9,10]
print(list[:])  # Print the list
list.insert(10,11)  #Add number 11 to the end of the list
print(list)
list.insert(0,0)  # Insert 0 at the begining
print(list)
list.remove(5)  # Remove 5 from the list
print(list)  # Print the modified list

# 3
# Tuples
# Tuple with mixed data types
my_tuple=(1,"Hello",3.4)
print(my_tuple)
# Nested tuple
my_tuple=("mouse",[8,4,6],(1,2,3))
print(my_tuple)
# Tuple with one element
var1=("Hello")
var2=("Hello",)
print(type(var1))
print(type(var2))
