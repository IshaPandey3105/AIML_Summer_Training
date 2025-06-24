# ==================================================
#                     STRINGS
# ==================================================

# Strings are sequences of characters like lists and tuples.
# Strings are immutable – they cannot be changed after creation
# Strings are ordered – they support indexing and slicing
# Strings can be defined using '', "", or '''triple quotes'''

# ---------------- Creating Strings ----------------

str1 = "Hello, World!"
str2 = 'Hello, World!'
str3 = '''Hello,
I am Isha,
I am from India'''

print(str1)    # Output: Hello, World!
print(str2)
print(str3)

# To print a literal backslash, we use \\
a = 'This is a string and \\ next line character'
print(a)    # Output: This is a string and \ next line character

# \n is used to insert a newline (i.e., move to the next line)
b = 'This is a string and \nnext line character'
print(b)    # Output:
            # This is a string and 
            # next line character

# ---------------- Iterating over a String ----------------

# Using for loop
for i in "Hello !!":
    print(i, end=" ")

# Using while loop
s2 = 'Hello World!'
i = 0
while i < len(s2):
    print(s2[i], end=" ")
    i += 1


# ---------------- String Slicing ----------------

# Syntax: string[start:stop:step]
print("\n")
print(s2[1:4])       # Output: ell
print(s2[:-1])       # Output: Hello World


# ---------------- Membership Testing ----------------

s3 = "India is my country"
print('India' in s3)      # Output: True

# Count number of 'i' in string
count = 0
for s in s3.lower():
    if s == 'i':
        count += 1
print("Count of i:", count)    # Output: 2


# ---------------- Common String Functions ----------------

str1 = "nieLiT"

print(len(str1))           # 6
print(str1.upper())        # NIELIT
print(str1.lower())        # nielit
print(str1.capitalize())   # Nielit
print(str1.title())        # NielIt
print(str1.islower())      # False
print(str1.isalpha())      # True
print(str1.isdigit())      # False

print("is23".isalnum())    # True
print("23".isdigit())      # True


# ---------------- split() Function ----------------

# Splits a string into list using delimiter
str2 = "nielit is a go#od institute"
print(str2.split("#"))     # Output: ['nielit is a go', 'od institute']


# ---------------- strip() Variants ----------------

print(" hello there !  ".lstrip())   # Removes leading space
print(" hello there !  ".rstrip())   # Removes trailing space
print(" hello there !  ".strip())    # Removes both leading and trailing spaces

#  Concatenation
s1 = "Hello"
s2 = "World"
result = s1 + " " + s2
print(result)  # Output: Hello World

#  Repetition
repeat = "Hi! " * 3
print(repeat)  # Output: Hi! Hi! Hi! 

