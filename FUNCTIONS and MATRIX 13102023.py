'''def sum(a,b,c):
    d=a+b+c
    print("Sum of a, b and c is: ",d)
    
print("hi")
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
sum(a,b,c) '''

# Matrix
row=int(input("Enter the number of rows:"))  
column=int(input("Enter the number of columns:"))  
List1=[[int(input()) for column in range(column)] for row in range(row)]  
print(List1) 
sum=0
for row in List1:
    for column in row:
        print(column,end=" ")
        if column%2==0:
            sum=sum+column
    print()

print("Sum of all the elements in the matrix is: ",sum) 

'''row=int(input("Enter the number of rows:"))  
column=int(input("Enter the number of columns:"))  
List1=[[int(input()) for column in range(column)] for row in range(row)]  
print(List1) 
sum=0
for row in range(0,len(List1)):
    for column in List1[row]:
        print(column,end=" ")
        if(row==1):
                sum=sum+column
    print()

print("Sum of the elements in the matrix in row 2 is: ",sum) '''

'''row=int(input("Enter the number of rows:"))  
column=int(input("Enter the number of columns:"))  
List1=[[int(input()) for column in range(column)] for row in range(row)]  
print(List1) 
sum=0
count=0
for row in List1:
    for column in row:
        print(column,end=" ")
        if(count%2==0):
                sum=sum+column
        count+=1
    print()

print("Sum of the elements in the matrix with even index is: ",sum) '''

'''row=int(input("Enter the number of rows:"))  
column=int(input("Enter the number of columns:"))  
List1=[[int(input()) for column in range(column)] for row in range(row)]  
print(List1) 
sum=0
for row in range(0,len(List1)):
    sum=sum+List1[row][3]
    print()

print("Sum of the elements in the matrix with the last element of the column is: ",sum) '''

'''row=int(input("Enter the number of rows:"))  
column=int(input("Enter the number of columns:"))  
List1=[[int(input()) for column in range(column)] for row in range(row)]  
print(List1) 
principal = 0
secondary = 0
for row in range(0, len(List1)): 
      for column in range(0, len(List1)): 
          if (row == column):
              principal += List1[row][column]
          if ((row + column) == (len(List1) - 1)):
              secondary += List1[row][column]
      print()
print("Principal Diagonal:", principal)
print("Secondary Diagonal:", secondary)
print("Sum of the diagonal elements: ",principal+secondary) '''

''' row=int(input("Enter the number of rows: "))  
column=int(input("Enter the number of columns: "))  
List1=[[int(input()) for column in range(column)] for row in range(row)]  
print(List1)
print("The original list is : " + str(List1))
K=3
for i in range(K-1, len(List1), K):
    List1[row] = List1[row][::-1]
print("After reversing every Kth row: " + str(List1)) ''' #PURA KARNA HAI

