# ==================================================
#                   DICTIONARY
# ==================================================
# A dictionary is a collection of key-value pairs.
# It is an unordered collection of items 
# Each key is unique and maps to a value.
# Keys are immutable, values can be mutable.
# Dictionaries are mutable, meaning they can be changed after creation.
# No slicing, no indexing in dictionary

# ---------------- Creating a dictionary ----------------

d1 = {}  # Empty dictionary
print(d1)  # Prints {}

students = {"neha": 20, "divya": 40, "ram": 90, "rajesh": 80}
print(students)
print(type(students))

d2 = {1: "hi", 1: "hi", 1: "hi", 2: "hi", 1: "hello"}  # Duplicate keys are not allowed
print(d2)  # Prints {1: 'hello', 2: 'hi'}

# ---------------- Accessing dictionary elements ----------------

print(students["divya"])  # Prints 40
print(d2[1])              # Prints hello

# ---------------- Updating and adding key-value pairs ----------------

students["neha"] = 100  # Updating the value of a key
print(students)

students["dav"] = 60    # Adding new key-value pair
print(students)

# ---------------- Deleting a key-value pair ----------------
print("@@ Deleting @@")
del students["ram"]
print(students)

# ---------------- Traversing a dictionary ----------------

for i in students:
    print(i)  # Prints keys

for i in students:
    print(students[i])  # Prints values

for i in students:
    print(f"{i} : {students[i]}")  # Prints key-value pairs

# OR

for i, j in students.items():
    print(i, "--", j)

# ---------------- Dictionary methods ----------------

# 1. clear()      : Removes all elements from dictionary
# 2. keys()       : Returns view object of all keys 
# 3. values()     : Returns view object of all values 
# 4. items()      : Returns view object of (key, value) tuples
# 5. get()        : Returns value of key, else default None
# 6. pop()        : Removes key and returns its value

print(students.keys())
print(students.values())
print(students.items())

print(students.get("neha"))  # Prints 100
print(students.get("isha"))  # Prints None 

print(students.pop("dav"))  # Prints 60 and removes key from dictionary
print(students)

print(students.clear())  # Prints None
print(students)          # Prints {} (empty dictionary)


# ---------------- Sorting ----------------

# 1. Sorting keys of dictionary
age={"isha": 20,"lisa":30,"abel":60}

print(sorted(age))
print(sorted(age , reverse=True))
print(age)

for i in sorted(age):
    print(i,"=>",age[i])

revised_age={}
for i in sorted(age):
    revised_age[i]=age[i]
print(revised_age)


# 1. Sorting values od Dictionary 

for i in sorted(age.values()):
    print(i ,"age")

# or

# for Ascending order
for i in sorted(age,key=age.get):
    print(i ,"is" ,age[i])

# for Descending order
for i in sorted(age,key=age.get,reverse=True):
    print(i ,"is" ,age[i])

