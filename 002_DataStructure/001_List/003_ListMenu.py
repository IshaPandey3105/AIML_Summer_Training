# Q Creating a menu driven program for all operations in list

L=[0,0,1,2,3,4,5,6,7,8,9,10]
print("list is : ",L)
print("1 For Insertion , 2 For Deletion , 3 For Length , 4 For Search , 5 For Sort ") 
print("6 For Reverse , 7 For count ,8 For index value , 9 For updation ,10 For Exit")
option=int(input("Enter your choice::"))
while (option!=10):
    if(option==1):
        num=int(input("Enter the number to be inserted::"))
        L.append(num)
        print("Updated list:",L)
    elif(option==2):
        num=int(input("Enter the number to be deleted::"))
        L.pop(num)
        print("Updated list:",L)
    elif(option==3):
        print("Length of list is::",len(L))
    elif(option==4):
        num=int(input("Enter the number to be searched::"))
        if num in L:
            print(num,"is present in list")
        else:
            print(num,"is not present in list")
    elif(option==5):
        L.sort()
        print("Sorted List is ::",L)
    elif(option==6):
        L.reverse()
        print("reversed List is ::",L)
    elif(option==7):
        num=int(input("Enter the number to be counted::"))
        print("Count of",num,"is::",L.count(num))
    elif(option==8):
        num=int(input("Enter the number to get index::"))
        print("Index of",num,"is::",L.index(num))
    elif(option==9):
        num=int(input("Enter the number to be updated::"))
        pos=int(input("Enter the position to be updated::"))
        L[pos]=num
        print("Updated list:",L)
    else:
        print("Invalid choice")
    option=int(input("Enter again::"))
print("End Of Program")