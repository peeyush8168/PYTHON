my_dict={"Name":"John","Age":20,"City":"Jammu"}
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())


d={'Key1':1,'Key2':2,'Key3':3}
for k in d:
    print(k)
for v in d.values():
         print(v)
for k,v in d.items():
         print(k, v)



my_list=[1,3,6,8,10,13,15]
length=len(my_list)
x=int(input("Set target: "))
for i in length:
    if my_list[i]==x:
        print(i)