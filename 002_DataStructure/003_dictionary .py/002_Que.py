# ============================================
#                QUESTIONS
# ============================================

## Q1 Book data in dictionary format and print it
books={"b1":["AI","BPB",2022],"b2":["Java","Pearson",2015],"b3":["Python","Springer",2024]}
print(books)
library_books={"b001":{"bname":"AI","publisher":["BPB","Mac"],"year":"2022"},
               "b002":{"bname":"Java","publisher":"Pearson","year":"2015"},
               "b003":{"bname":"Python","publisher":"Springer","year":"2024"}}
print(library_books)
print(library_books["b001"]["publisher"][0]) # Accessing the first publisher of book b001

# ============================================

## Q2 Create a dictionary of n students store their roll no. and name take inputs from user
students={}
n=int(input("Enter total no. of students : "))
for i in range(n):
    roll_no=int(input("Enter Roll Number : "))
    name=input("Enter name : ")
    students[roll_no]=name
print(students)

# ============================================

## Q3 Create a dictionary of 5 employees and store their emp code , name and designation by reading from user
emp={}
for i in range(2):
    ecode=int(input("Enter emp code : "))
    ename=input("Enter emp name : ")
    desig=input("Enter emp designation : ")
    l1=[ecode,ename,desig]
    emp[i]=l1
print(emp)

# ============================================

## Q4 Write a Programme to enter subject name and marks of 5 students and calculate their percentage

s = {}  
n=int(input("Enter Total no. of subjects : "))
for i in range(n):
    sub = input(f"Enter subject name {i+1}: ")
    marks_list = []
    for j in range(1, 6):
        marks = float(input(f"Enter marks of student {j} in {sub} (out of 100): "))
        marks_list.append(marks)
    s[sub] = marks_list  # Store subject and its list of marks
print(s)
print("Subject-wise Percentages")
for i, j in s.items():
    percentage = (sum(j) / 500)*100
    print(f"{i} : {percentage}%")