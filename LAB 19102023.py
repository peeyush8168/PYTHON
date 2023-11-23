'''Sorting dictionaries in Python refers to arranging th key-value pairs within a dictionary in a 
specific order, typically based on the keys or values, Python dictionaries themselves do not
guarantee any particular order, but you can sort and order elements '''

'''my_dict={'7':1,'1':2,'2':5}
sorted_dict=(sorted(my_dict.items()))
print(sorted_dict)'''


'''my_dict={'apple':3,'banana':1,'cherry':2}'''
'''sorted_dict=dict(sorted(my_dict.items(),key=lambda item: item[1]))   #1=ascending, 0=same as given
print(sorted_dict) '''

'''sorted_dict=dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print(sorted_dict) '''

'''copy collection- method returns a copy of the specified list. why- For collections that are 
mutable or contain mutable items, a copy is sometimes needed so one can change one copy without 
changing the other. '''

import copy
original_list=[1,[2,3],4]
a=copy(deepcopy.original_list())
print(a)