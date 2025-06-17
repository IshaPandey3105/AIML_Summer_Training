# Control Flow Statments ::: If , elif , else 

# #Q1 Find odd and even 
# a=int(input("Enter a no."))
# if (a%2==0):
#     print(f"{a} is even")
# else:
#     print(a,"is odd")    

##Q2 Grase marks    
# m=int(input("Enter a marks"))
# if (m<35):
#     print("fail")
#     m=m+5
#     print("Total marks after adding grace marks:" ,m)
# else:
#     print("pass")    

# #Q3 Menu driven program calculator
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

# # #Q4 trafic light 
# color=input("Enter color :").lower()   
# if(color=="red"):
#     print("stop!")
# elif(color=="green"):
#     print("go!") 
# elif(color=="yellow"):
#     print("ready!")  
# else:
#     print("Invalid")   

# # Q5 Electricity bill
# units=int(input("Enter units :"))
# if(units<=100):
#     prize=units*5
# elif(units>=200):  
#     prize=100*5+ 100*7+(units-100)*10
# else:
#     prize= 100*5+(units-100)*7  
# print("bill:: ",prize)

# #Q6 Grade classification
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

# #Q7 leap year
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
