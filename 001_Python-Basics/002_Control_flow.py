# ============================================
#    Control Flow Statements ::: if, elif, else  
# ============================================

# control Flow statements are used to control the flow of a program's execution based on certain conditions.
# if, elif, else are the most commonly used control flow statements in Python.
# if statement is used to execute a block of code if a condition is true.
# elif statement is used to check another condition if the first condition is false.
# else statement is used to execute a block of code if all conditions are false.

# ============================================

# --------------- Q1: Find Odd and Even ---------------
# a=int(input("Enter a no."))
# if (a%2==0):
#     print(f"{a} is even")
# else:
#     print(a,"is odd")    

# --------------- Q2: Grace Marks ---------------
# m=int(input("Enter a marks"))
# if (m<35):
#     print("fail")
#     m=m+5
#     print("Total marks after adding grace marks:" ,m)
# else:
#     print("pass")    

# --------------- Q3: Menu-Driven Calculator ---------------
# print("Enter 1 for add")
# print("Enter 2 for sub ")
# print("Enter 3 for mul ")
# print("Enter 4 for div ")
# x=int(input("Enter your choice"))
# a,b=input("enter no.::").split()
# a=int(a)
# b=int(b)
# if(x==1):
#     print(a+b)
# elif(x==2):
#     print(a-b)
# elif(x==3):
#     print(a*b)
# elif(x==4):
#     print(a/b)
# else:
#     print("invalid option ")

# --------------- Q4: Traffic Light ---------------
# color=input("Enter color :").lower()   
# if(color=="red"):
#     print("stop!")
# elif(color=="green"):
#     print("go!") 
# elif(color=="yellow"):
#     print("ready!")  
# else:
#     print("Invalid")   

# --------------- Q5: Electricity Bill ---------------
# units=int(input("Enter units :"))
# if(units<=100):
#     prize=units*5
# elif(units>=200):  
#     prize=100*5+ 100*7+(units-100)*10
# else:
#     prize= 100*5+(units-100)*7  
# print("bill:: ",prize)

# --------------- Q6: Grade Classification ---------------
# p=int(input("enter percentage :"))
# if(p>=90):
#     print("A+")
# elif(p>=75):
#     print("A")
# elif(p>=60):
#     print("B")
# elif(p>=40):
#     print("C")
# else:
#     print("Fail")

# --------------- Q7: Leap Year Check ---------------
year=int(input("Enter year :"))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("leap year")    
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("not leap year")

    
