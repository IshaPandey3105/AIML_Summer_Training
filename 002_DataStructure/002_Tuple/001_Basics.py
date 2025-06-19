# =====================================================
#                        TUPLES
# =====================================================

# It is a collection of multiple values in an ordered sequence.
# Tuples are immutable (cannot be changed after creation).
# Mutable: list, dictionary and set
# Immutable: tuple, string, int, float etc

# Check mutability with id()
l1=[1,2,3,4]
print(id(l1))
l1[0]=100
print(id(l1))  # ID remains same => mutable

# Tuple Examples
T1=(1,2,3,4,5)
(10,20,30,40)  # This is also a tuple
t1=1,2,3,4,5
# print(T1[0])=4000   # error
print(type(T1))
print(type(t1))  # Tuple type without parentheses also valid

# Singleton Tuple
x=23,
print(type(x))  # tuple

x=(23,)
print(type(x))  # tuple

x=()           # Empty Tuple
print(type(x))

# Heterogeneous Tuple
y=56,"neha",True,78.5
print(type(y))

# Tuple unpacking
p,q = 10,20
print(type(p))
print(q)

# Swapping values
p,q = q,p
print(p)
print(q)

# Nested Structures in Tuple
book=(100,"java",["abc","Macro hills"],(["v1","v2"]),"A")
book[2][0] = "ABC"  # list inside tuple is mutable
print(book)
print(book[-1][-1])  # A
print(book[3][0])    # v1
book[3][1]="V1.$"
print(book[3][1])
print(book)

# Convert to list
book_list = list(book)
print(book_list)

# Convert back to tuple
book_list = tuple(book)

# Membership Test
print("java2" in book)  # False
print("java" in book)   # True

# Tuple Operations
tuple1 = (1,2,3,4,5)
tuple2 = (10,20,30,40,50)
print(tuple1 + tuple2)   # Concatenation
print(tuple1 * 3)        # Repetition (no change in original tuple)
print(tuple1)

tuple1 = tuple1 * 3  # Overwriting with repeated tuple( change in original tuple)
print(tuple1)

# Delete entire tuple
del(tuple1)
# print(tuple1)  #  Error: tuple1 is deleted
