# ============================================
#             QUESTIONS (List Practice)
# ============================================

## Q1: Counting number of students fail and pass
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

# ============================================

## Q2: Searching a particular name
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

# ============================================

## Q3: Count the no. of vowels and consonants in a string
# s="Hello World"
# vowels=0
# consonants=0
# for i in s:
#     if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
#         vowels+=1
#     else:
#         consonants+=1
# print("Total vowels:" ,vowels)
# print("Total consonants:" ,consonants)

# ============================================

## Q4: Count the even and odd numbers
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

# ============================================

## Q5: Calculating average of marks
# marks=[]
# sum=0
# n=int(input("Enter total no. of students::"))
# for i in range(n):
#     m=int(input("Enter the marks::"))
#     marks.append(m)
# for i in marks:
#     sum+=i
# print("Average marks",sum/n)

# ============================================

## Q6: Creating a new list from rupees list to dollar
# R=[100,200,300,400,500]
# D=[]
# for i in R:
#     # D.append(i*(1/85))
#     D.append(i*0.012)
# print(D)

# ============================================

## Q7: Removing low salaries into another list
# L1=[100,10000,20000,700,30000,500,40000,50000,800,9,8]
# L2=[]
# for i in L1:
#     if(i<=1000):
#         L2.append(i)
#         L1.remove(i)
# print(L1)
# print(L2)

#  Correct Method using copy of list
# L1 = [100, 10000, 20000, 700, 30000, 500, 40000, 50000, 800, 9, 8]
# L2 = []
# for i in L1[:]:  # iterate over a copy
#     if i <= 1000:
#         L2.append(i)
#         L1.remove(i)
# print(L1)
# print(L2)

# ============================================

## Q8: Find highest and lowest number in a list (without built-in functions)
L1=[1000,1,2,3,4,500,6,7,8,9,100]
min=L1[0]
max=L1[0]
for i in L1:
    if(i<min):
        min=i
    if(i>max):
        max=i
print(min)
print(max)
