# Concatenation
text1="  Hello, World! "
text_upper=text1.upper()  # Convert to uppercase
print(text_upper)
text_stripped=text1.lstrip()  # For removing the leading and the trailing spaces lstrip() and rstrip()
print(text_stripped)
replaced_text=text1.replace("World","Python")  # Replace World with Python
print(replaced_text)
word_list=text1.split(",")  # Split
print(word_list)
starts_with_hello=text1.startswith(" Hello")  # True else False
print(starts_with_hello)
ends_with_exclamation=text1.endswith("! ")  # True else False
print(ends_with_exclamation)
text2="Python,is,awesome"
sentence=text2.split(",")  # Split the sentence into words using space
print(sentence)
joined_text2="-".join(text2)
print(joined_text2)


# append() and extend() function in a list
numbers1=[21,34,54,12]
print("Before append: ",numbers1)
numbers1.append(32)
print("After append: ",numbers1)
numbers2=[1,3,5]
even_numbers=[4,6,8]
numbers2.extend(even_numbers)
print("List after append: ",numbers2)


# Replace 
languages=['Python','Swift','C++']
languages[2]='C'
print(languages)  # ['Python','Swift','C']

