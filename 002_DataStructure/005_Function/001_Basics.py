# ============================================
#                  Function
# ============================================

# Function to print the sum of two fixed numbers
def print_sum():
    a = 2
    b = 4
    c = a + b
    print("Sum is:", c)

print_sum()

# Function to return the sum of two numbers passed as parameters
def add_numbers(x, y):
    return x + y

result = add_numbers(2, 3)
print("Addition result:", result)

# 1. Function with Default Arguments
def greet(name="Isha"):
    print("Hello,", name)

greet()
greet("Amit")

# 2. Function Returning Multiple Values

def add_numbers(x, y):  # here x and y are parameters
    return x + y , x-y

add,sub = add_numbers(2, 3) # here 2 and 3 are arguments
print("Add:", add)
print("Sub:", sub)

# 3. Function with Variable-Length Arguments

def print_all(*args):
    for item in args:
        print(item , end=" ")

print_all("AI", "ML", "Python", "Data Science")