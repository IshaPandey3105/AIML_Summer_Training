# ============================================
#               Loops : for , while 
# ============================================

# Loops are used to execute a block of code repeatedly for a specified number of times.
# There are two types of loops in Python: for and while loops.
# For loops are used to iterate over a sequence (such as a list, tuple, dictionary, set, or string)
# while loops are used to execute a block of code as long as a certain condition is met.

# ============================================

for i in range(-1,-10,-2):
    pass         # No error will come 
    # print("hi" , i,end=" ")
    
# for i in range(1,10):
#     print( "hi", end=" ")  # print nothing(just come out of loop)

# a=1
# while(a<=10):
#     print("hello",a)
#     a+=1


# ============================================
#               ****** QUESTIONS ******
# ============================================

## --------------- Q1: Even Numbers ---------------
# print("All Even no. till 10 are ::")
# count=0
# for i in range(0,11,2):
#     print(i , end=" ")
#     count+=1
# print("\nTotal no. of even no. are :: " , count)

## --------------- Q2: Sum of n Natural Numbers ---------------
# n=int(input("Enter value of n: "))
# sum=0
# for i in range(n+1): # We can also write range(1,n+1)
#     sum=sum+i
# print("Sum is:",sum)

## --------------- Q3: Factorial of a Number ---------------
# n=int(input("Enter value of n: "))
# fac=1
# for i in range(2,n+1): # We can also use range(n,0,-1)
#     fac=fac*i
# print("Factorial is:",fac)  

## --------------- Q4: Menu-Driven Program ---------------
# option="y"
# while(option!="n"):
#     print("Enter 1 for add")
#     print("Enter 2 for sub ")
#     print("Enter 3 for mul ")
#     print("Enter 4 for div ")
#     x=int(input("Enter your choice"))
#     a,b=input("enter no.::").split()
#     a=int(a)
#     b=int(b)
#     if(x==1):
#         print("ADD:",a+b)
#     elif(x==2):
#         print("SUB:",a-b)
#     elif(x==3):
#         print("MUL:",a*b)
#     elif(x==4):
#         print("DIV:",a/b)
#     else:
#         print("Invalid Option ")
#     print("Do you want to continue (y/n)?: ")
#     option=input()
# print("Program Ended Sucessfully ")    


# ============================================
#       Transfer Control Statements
# ============================================

# pass :: when we don't want to do work 
# break :: which will break the current loop
# continue:: skip the current iteration 

# -------- eg: break --------
# for i in range(1,10):
#     if (i==5):
#         break
#     print(i,end=" ")
# print("End")

# -------- eg: continue --------
# for i in range(1,10):
#     if (i==5):
#         continue
#     print(i)
# print("End")    

## We can use else with for loop
# -------- eg: check prime --------
# num=int(input("Enter number::"))
# for i in range(2,(num//2)+1):
#     if (num % i==0):
#         print("Not Prime")
#         break
# else:
#     print("Prime")


# ============================================
#         ***Q1: Check Prime Number***
# ============================================

num=int(input("Enter number::"))
for i in range(2,(num//2)+1):
    if (num % i==0):
        flag=0
        break
    else:
        flag=1

if(flag==0):        
    print("Not Prime")
else:
    print("Prime")

#OR

def prime(n):
    if n < 2:
        return False
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter number: "))
if prime(n):
    print("Prime")
else:
    print("Not prime")
