#python program for creating a string

#Creating a string with single quotes
String1='Hello,this is a single-quoted string'
print("String with the help of single quotes:")
print(String1)

#creating a string with double quotes
String2="Python is my favorite programminng language"
print("\nString with the use of double quotes:")
print(String2)
print(type(String2))

#print the data type of string 2
# Creating a string with triple quotes
String3='''this is a triple quoted string 
that spans across multiple lines.
It can include 'single' and "double" quotes without escaping.'''
print("\nString with the use of triple quotes:")
print(String3)
print(type(String3)) #Print the data type of String3

# Creating string with triple quotes allows multiple lines
String4 ='''Strings
        can
        be
        multiline'''
print("\nCreating a multiline String:")
print(String4)

# Concatenating two strings
String5 = String1 +" and " + String2
print("\nConcatenated String:")
print(String5)