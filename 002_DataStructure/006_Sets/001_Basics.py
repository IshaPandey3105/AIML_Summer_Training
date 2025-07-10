# ============================================
#                  Sets
# ============================================

# What is a Set?
 
# A set is an unordered, unindexed collection of unique elements.
# Defined using {} curly braces or the set() function.
# Duplicate values are automatically removed.

my_set = {1, 2, 3, 4, 5}
print("SET:",my_set)  # O/P:: {1, 2, 3, 4, 5}
print(type(my_set)) # O/P:: <class 'set'>

# Duplicates are removed
my_set = {1, 2, 2, 3, 4,5,5,5,4}
print("Duplicated removes:",my_set)  # O/P ::{1, 2, 3, 4,5}

# ============================================

# Creating a Set:

# Using curly braces
fruits = {"apple", "banana", "cherry"}

# Using set() function
numbers = set([1, 2, 3, 4])

# Empty set
empty_set = set()

# ============================================

#  Set Methods : [ add(), remove(), discard(), pop(),copy(),clear()]


S1={1,2,3,4}
# add() ➔ Add a single element
S1.add(5)
print("ADD:",S1)  
# update() ➔ Add multiple elements
S1.update([6,7,8])
print("UPDATE:",S1)
# remove() ➔ Remove an element
S1.remove(1)
print("REMOVE:",S1)
# discard() ➔ Remove element (no error if not found)
S1.discard(9)
S1.discard(2)
print("DISCARD:",S1)
# pop() ➔  Remove and return a random element
print(S1.pop())
print("POP:",S1)
# copy() ➔ Create a copy
S2=S1.copy()
print("COPY:",S2)
# clear() ➔ Remove all elements
S1.clear()
print("CLEAR:",S1)  

# ============================================

# Set Operations : [ union(), intersection(), difference(), symmetric_difference() ]

# Two sample sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Set A:", A)
print("Set B:", B)

# Union ➔ All unique elements
print("Union:", A.union(B))          # or A | B

# Intersection ➔ Common elements
print("Intersection:", A.intersection(B))  # or A & B

# Difference ➔ Elements in A but not in B
print("Difference (A - B):", A.difference(B))  # or A - B

# Symmetric Difference ➔ In A or B but not both
print("Symmetric Difference:", A.symmetric_difference(B))  # or A ^ B

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)   # Union: {1, 2, 3, 4, 5, 6}
print(A & B)   # Intersection: {3, 4}
print(A - B)   # Difference: {1, 2}
print(A ^ B)   # Symmetric Difference: {1, 2, 5, 6}


# ============================================

#  Set Comparisons

# Subset ➔ Check if A is subset of B  ( if every element of A is also present in B.)
print("Is A subset of B?", A.issubset(B))

# Superset ➔ Check if A is superset of B (A contains all elements of B)
print("Is A superset of B?", A.issuperset(B))

# Disjoint ➔ Check if A and B have no elements in common
print("Are A and B disjoint?", A.isdisjoint(B))


# ============================================

# Set Comprehension
# A set comprehension is a compact way to create a set from an iterable.

squares = {x**2 for x in range(1, 6)}
print(squares) # Output: {1, 4, 9, 16, 25}