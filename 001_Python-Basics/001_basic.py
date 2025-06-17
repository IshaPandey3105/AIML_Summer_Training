print("--Type Casting--")
#implicit --> Automatic conversion of data type
a=5
b=5.5
c=a+b
print(c) 
print(type(c))
print(10.5 + 10)
#Explicite --> int() float() str() bool() complex()
d=int(b)
print(d)


# Operators - Arithmetic, Comparison, Logical, Assignment, Bitwise
print("--Operators--")
print(("5"+"0"),(9/2),(9%2),(9//2),(2**3),(-10))     # 50 4.5 1 4 8 -10
print("5"==5) # False
print(not(4>=5) or ("abc"=="bc")) # True
print((5&3),(5|3),(~5),(5^3),(5 << 2),(5 >> 2))  # 1 6 -6 2 20 -2

## ******Questions******

## Q1- Find Tax on a bill
# name=input("Enter Name : ")
# qty=int(input("Enter Qunatity :"))
# prize=int(input("Enter prize of 1 product : "))
# tax=0.05
# subtotal= qty*prize
# t_tax=subtotal*tax
# amt= subtotal+t_tax
# print(f"Tax on {name} bill is {t_tax}")  
# print(f"Bill Paybel:{amt}")

# #Q2-Program to impliment all binary operators
# a=int(input("Enter a : "))
# b=int(input("Enter b : "))

# print("**Arithmetic**")
# print(f"Addition : {a+b}, Subtraction : {a-b} , Multiplication : {a*b} , Division : {a/b} , Modulus : {a%b} , Floor Division : {a//b}")

# print("**Comparison**")
# print(f"Equal : {a==b} , Not Equal : {a!=b} , Greater than : {a>b}, Less than equal to : {a<=b}")

# print("**Logical**")
# print(f"AND : {(a>b) and (b==a)} , OR : {(a>b) or (b==a)} , NOT : {not a}")

# print("**Bitwise**")
# print(f"AND : {a&b} , OR : {a|b} , XOR : {a^b} , NOT : {~a} , Left Shift : {a<<b} , Right Shift : {a>>b}")

# #Q3- Program to calculate simple interest
# p=int(input("Enter principal : "))
# r=float(input("Enter rate : "))
# t=int(input("Enter time : "))
# si=(p*r*t)/100
# print(f"Simple Interest is : {si}")

# #Q4- Program to calculate compound interest
# p=int(input("Enter principal : "))
# r=float(input("Enter rate : "))
# t=int(input("Enter time : "))
# ci=p*(1+r/100)**t-p
# print(f"Compound Interest is : {ci}")

# #Q5- Program to calculate area of circle, rectangle, square, triangle

# r=float(input("enter radius : "))
# print(f"Area of circle is : {3.14*r**2}")

# l=float(input("Enter length : "))
# b=float(input("Enter breadth : "))
# print(f"Area of rectangle is : {l*b}")

# s=float(input("Enter side : "))
# print(f"Area of square is : {s*s}")

# T_b=float(input("Enter base : "))
# h=float(input("Enter height : "))
# print(f"Area of triangle is : {(T_b*h)/2}")


#Q6 finding quadratic equation roots
import math 
b=float(input("Enter b : "))
a=float(input("Enter a : "))
c=float(input("Enter c : "))
discriminant = b**2 - 4*a*c

if(discriminant >0) :
    sqrt_d = math.sqrt(discriminant)
    r1 = (-b + sqrt_d) / (2*a)
    r2 = (-b - sqrt_d) / (2*a)
    print(r1,r2)
else :
    print("Roots doesn't exist")
