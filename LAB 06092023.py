# Built in functions


# 1st
# The abs() function returns the absolute value of a number.
print(abs(-10))

# The len() function returns the length of a string or sequence.
print(len("WelcomeTo, Miet!"))

# The min() function returns the minimum value of a sequence.
print(min([10, 20, 30]))

# The round() function returns a number to a specified number of decimal places.
print(round(3.14159, 2))

# The isalnum() function returns True if a string contains only alphanumeric characters, False otherwise.
print("CSE, 3rd Sem!".isalnum())
print("123abc".isalnum())

# The type() function returns the type of an object.
print(type(10))
print(type("AI and, ML!"))



# 2nd
# all()- Returns True if all elements in an iterable are true, otherwise returns False.
list1=[True, True, True]
list2=[True, False, True]
print(all(list1))
print(all(list2))

# any()- Returns True if any element in an iterable is true, otherwise returns false.
list3=[False, False, False]
list4=[True, False, False]
print(any(list3))
print(any(list4))

# ascii()- Returns a string containing a printable representation of an object.
# It is used to get a printable representation of an object, not its ASCII value.
print(ascii("Kot, \nBhalwal!"))

# The ord() function returns the Unicode code point of a character.
# It is more comprehensive character encoding than ASCII.
print(ord("a"))
print(ord(" "))
print(ord(","))
print(ord("*"))


# 3rd
# bin()- Converts an integer to a binary string.
print(bin(10))
print(bin(15))

# bool()- Converts a value to a Boolean(True or False).
print(bool(0))
print(bool(42))
print(bool([]))
print(bool([1, 2]))

# bytearray()- Returns a mutable bytearray object from an iterable of integers.
byte_array = bytearray([65, 66, 67])
print(byte_array)
byte_array[0] = 88 # ASCII value of 'X'
print(byte_array)

# bytes()- Returns a immutable bytes object from an iterable of integers.
byte_string = bytes([68, 69, 70])
print(byte_string)

# callable()- Returns True if the object appears callable (can be called as a function), otherwise false.
def my_function():
    return 42
print(callable(my_function))
print(callable(42))
