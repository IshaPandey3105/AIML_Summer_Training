# LIST (data structure)
# To store various types of data
# ordered collection of items (Heterogeneous elems)

# student_details=["Isha",90,"Python","Delhi"]
# print(student_details)
# fruits=["Apple","Kiwi","Banana","cherry"]
# for i in fruits:
#     print("I Like ", i)

# Accessing the elements
# Indexing : When we want to retrive single element from list

# marks=[20,30,40,50,60,70]
# print(len(marks))   # For counting the number of elements in list
# print(marks[2])  
# print(marks[-2])
# print("Marks are ::")
# for i in range(0,len(marks)):   # But we can use direct list name as above
#     print(marks[i])

# # Slicing : when we want to retrive a part of list
# #list[start:stop:step]
# print(marks[2:7:1])
# print(marks[2:7])
# print(marks[:7:2])
# print(marks[:3:])
# print(marks[::5])
# print(marks[2])          # single Elem
# print(marks[-2:-3:-1])  # Negative Indexing
# print(marks[-6:-3:-1])  
# print(marks[::-1])  # Reverse
# print(marks[::])    # Full List


# l1 = list(range(0, 10))
# print(l1)
# print(l1[4:])



## LIST METHODS :- append (),insert(),remove(),pop(),sort(),reverse(),index(),count()

# we have 3 methods for adding elements in list
# 1. append() : adds element at the end of list
# 2. insert() : adds element at specified position in list
# 3. extend() : adds multiple elements at the end of list
# 4. add() : adds multiple elements at specified position in list

#eg::
# l1=[10,20,30,40,50]
# print("Original List ::",l1)
# l1.append(60)
# print("Now List ::",l1)
# l1.insert(2,100)
# print("Now List ::",l1)
# l1.extend([1,2,3,4])
# print("Now List ::",l1)
# l1.sort()
# print("sorted List ::",l1)
# l1.reverse()
# print("reversed List ::",l1)

# we have 3 methods for removing elements from list
# 1. remove() : removes first occurrence of element in list
# 2. pop() : removes element at specified position in list
# 3. clear() : removes all elements from list

#eg::
# l1=[10,20,30,40,50]
# print("Original List ::",l1)
# l1.remove(30)
# print("Now List ::",l1)
# l1.pop(2)
# print("Now List ::",l1)
# l1.clear()
# print("Now List ::",l1)

# some other methods
# 1. count() : returns count of element in list
# 2. index() : returns index of element in list
# 3. sort() : sorts list in ascending order
# 4. reverse() : reverses list

#eg::
# l1=['s','i','o','h','i']
# print("Original List ::",l1)
# print("Count of i in list ::",l1.count('i'))
# print("Index of i in list ::",l1.index('i'))
# l1.sort()
# print("sorted List ::",l1)
# l1.reverse()
# print("reversed List ::",l1)

# my_list=[]
# for i in range(5):
#     num=int(input("enter Elem::"))
#     my_list.append(num)
# print(my_list)


## **Quetions**


## Q1 Counting no. of students fail and pass
# marks=[20,45,50,12,40]
# p=0
# f=0
# for i in marks:
#     if(i<=35):
#         f+=1
#     else:
#         p+=1
# print("No. of students fail ::",f)
# print("No. of students pass ::",p)


## Q2 searching a particular name
# sname=["neha","priya","pooja","dolly","Garima"]
# name=input("Enter the name to be searched::").lower()
# for i in sname:
#     if(name==i):
#         flag=1
#         break
#     else:
#         flag=0
# if(flag==1):
#     print("Name found")
# else:
#     print("Name not found")


## Q3 count the no. of vowels and consonants in a string
# s="Hello World"
# vowels=0
# consonants=0
# for i in s:
#     if(i=='a' or i=='e' or i=='i' or i=='o ' or i=='u'):
#         vowels+=1
#     else:
#         consonants+=1
# print("Total vowels:" ,vowels)
# print("Total consonants:" ,consonants)


## Q4 count the even and odd no.
# L=range(0,20)
# even=0
# odd=0
# for i in L:
#     if(i%2==0):
#         even+=1
#     else:
#         odd+=1
# print("Total even no.:" ,even)
# print("Total odd no.:" , odd)


## Q5 Calculating average of marks
# marks=[]
# sum=0
# n=int(input("Enter total no. of students::"))
# for i in range(n):
#     m=int(input("Enter the marks::"))
#     marks.append(m)
# for i in marks:
#     sum+=i
# print("Average marks",sum/n)

## Q6 creating a new list  from rupees list to dollar
# R=[100,200,300,400,500]
# D=[]
# for i in R:
#     # D.append(i*(1/85))
#     D.append(i*0.012)
# print(D)

## Q7 Removing less salary from a list and adding in another
# L1=[100,10000,20000,700,30000,500,40000,50000,800,9,8]
# L2=[]
# for i in L1:
#     if(i<=1000):
#         L2.append(i)
#         L1.remove(i)
# print(L1)
# print(L2)

L1 = [100, 10000, 20000, 700, 30000, 500, 40000, 50000, 800, 9, 8]
L2 = []
for i in L1[:]:  # iterate over a copy
    if i <= 1000:
        L2.append(i)
        L1.remove(i)
print(L1)
print(L2)




## Q Creating a menu driven program for all operations in list
# L=[0,0,1,2,3,4,5,6,7,8,9,10]
# print("list is : ",L)
# print("1 For Insertion , 2 For Deletion , 3 For Length , 4 For Search , 5 For Sort ") 
# print("6 For Reverse , 7 For count ,8 For index value , 9 For updation ,10 For Exit")
# option=int(input("Enter your choice::"))
# while (option!=10):
#     if(option==1):
#         num=int(input("Enter the number to be inserted::"))
#         L.append(num)
#         print("Updated list:",L)
#     elif(option==2):
#         num=int(input("Enter the number to be deleted::"))
#         L.pop(num)
#         print("Updated list:",L)
#     elif(option==3):
#         print("Length of list is::",len(L))
#     elif(option==4):
#         num=int(input("Enter the number to be searched::"))
#         if num in L:
#             print(num,"is present in list")
#         else:
#             print(num,"is not present in list")
#     elif(option==5):
#         L.sort()
#         print("Sorted List is ::",L)
#     elif(option==6):
#         L.reverse()
#         print("reversed List is ::",L)
#     elif(option==7):
#         num=int(input("Enter the number to be counted::"))
#         print("Count of",num,"is::",L.count(num))
#     elif(option==8):
#         num=int(input("Enter the number to get index::"))
#         print("Index of",num,"is::",L.index(num))
#     elif(option==9):
#         num=int(input("Enter the number to be updated::"))
#         pos=int(input("Enter the position to be updated::"))
#         L[pos]=num
#         print("Updated list:",L)
#     else:
#         print("Invalid choice")
#     option=int(input("Enter again::"))
# print("End Of Program")
