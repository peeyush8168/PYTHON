list=[10,11.4,'Python',23,64]
length=len(list)
while(1):
    print("****List-Iteration****")
    print('1. By using loop(variable)')
    print('2. By using loop(range)')
    print('3. By using while loop')
    print('4. By using list comprehension')
    print('5. By using Enumeration')
    print('6. Exit')
    v=int(input("Enter your choice: "))
    
    if(v==1):
        for i in list:
            print(i)
    elif(v==2):
        for i in range(0,5):
            print(list[i])
    elif(v==3):
        i=0
        while(i<length):
            print(list[i])
            i+=1
    elif(v==4):
        [print(i) for i in list]
    elif(v==5):
        for i,val,in enumerate(list):
            print(i,",",val)
    else:
        exit