# Python is a high-level, interpreted programming language 
# That is widely used for various purposes such as web development, scientific computing , data analysis, artificial intelligence, and more.
# Python is known for its simplicity, readability, and ease of use, making it a popular choice 
# In Python code is compliled into bytecode (.py) which is then executed by the Python interpreter.
# Python is a dynamically typed language, which means that you don't need to declare the data type of a variable before using it.
# Python has a vast collection of libraries and frameworks that make it suitable for a wide range of applications

# ============================================
#             TYPE CASTING SECTION
# ============================================
# Type casting is the process of converting a value from one data type to another.
# Python supports both explicit and implicit type casting.

print("--Type Casting--")
# Implicit --> Automatic conversion of data type
a = 5
b = 5.5
c = a + b
print(c) 
print(type(c))
print(10.5 + 10)

# Explicit --> int() float() str() bool() complex()
d = int(b)
print(d)

# ============================================
#                OPERATORS SECTION
# ============================================

# Operators - Arithmetic, Comparison, Logical, Assignment, Bitwise
print("--Operators--")
print(("5" + "0"), (9 / 2), (9 % 2), (9 // 2), (2 ** 3), (-10))  # 50 4.5 1 4 8 -10
print("5" == 5)  # False
print(not (4 >= 5) or ("abc" == "bc"))  # True
print((5 & 3), (5 | 3), (~5), (5 ^ 3), (5 << 2), (5 >> 2))  # 1 6 -6 2 20 -2

# ============================================
#               QUESTIONS SECTION
# ============================================

# --------------- Q1: Find Tax on a Bill ---------------
# name = input("Enter Name : ")
# qty = int(input("Enter Quantity : "))
# prize = int(input("Enter price of 1 product : "))
# tax = 0.05
# subtotal = qty * prize
# t_tax = subtotal * tax
# amt = subtotal + t_tax
# print(f"Tax on {name} bill is {t_tax}")  
# print(f"Bill Payable: {amt}")

# --------------- Q2: Binary Operators Program ---------------
# a = int(input("Enter a : "))
# b = int(input("Enter b : "))

# print("**Arithmetic**")
# print(f"Addition : {a + b}, Subtraction : {a - b}, Multiplication : {a * b}, Division : {a / b}, Modulus : {a % b}, Floor Division : {a // b}")

# print("**Comparison**")
# print(f"Equal : {a == b}, Not Equal : {a != b}, Greater than : {a > b}, Less than equal to : {a <= b}")

# print("**Logical**")
# print(f"AND : {(a > b) and (b == a)}, OR : {(a > b) or (b == a)}, NOT : {not a}")

# print("**Bitwise**")
# print(f"AND : {a & b}, OR : {a | b}, XOR : {a ^ b}, NOT : {~a}, Left Shift : {a << b}, Right Shift : {a >> b}")

# --------------- Q3: Simple Interest ---------------
# p = int(input("Enter principal : "))
# r = float(input("Enter rate : "))
# t = int(input("Enter time : "))
# si = (p * r * t) / 100
# print(f"Simple Interest is : {si}")

# --------------- Q4: Compound Interest ---------------
# p = int(input("Enter principal : "))
# r = float(input("Enter rate : "))
# t = int(input("Enter time : "))
# ci = p * (1 + r / 100) ** t - p
# print(f"Compound Interest is : {ci}")

# --------------- Q5: Area Calculations ---------------
# r = float(input("Enter radius : "))
# print(f"Area of circle is : {3.14 * r ** 2}")

# l = float(input("Enter length : "))
# b = float(input("Enter breadth : "))
# print(f"Area of rectangle is : {l * b}")

# s = float(input("Enter side : "))
# print(f"Area of square is : {s * s}")

# T_b = float(input("Enter base : "))
# h = float(input("Enter height : "))
# print(f"Area of triangle is : {(T_b * h) / 2}")

# --------------- Q6: Quadratic Equation Roots ---------------
# import math 
# b = float(input("Enter b : "))
# a = float(input("Enter a : "))
# c = float(input("Enter c : "))
# discriminant = b**2 - 4*a*c

# if discriminant > 0:
#     sqrt_d = math.sqrt(discriminant)
#     r1 = (-b + sqrt_d) / (2 * a)
#     r2 = (-b - sqrt_d) / (2 * a)
#     print(r1, r2)
# else:
#     print("Roots don't exist")

# ============================================
#             Pattern Printing Programs
# ============================================

print("************")
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()             # to move to the next line after inner loop

for i in range(3,0,-1):
    # print(i,end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range(1, 4):
    for j in range(1, i + 1):
        print(j, end=" ")
    print() 

# a=1
# while(a<=5):
#     b=1
#     while(b<=a):
#         print(b,end=" ")
#         b+=1
#     print()
#     a+=1

print("************")
a=3
while(a>=1):
    b=1
    while(b<=a):
        print(b,end=" ")
        b+=1
    print()
    a-=1