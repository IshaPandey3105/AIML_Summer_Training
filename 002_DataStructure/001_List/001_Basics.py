# ============================================
#           LIST (Data Structure)
# ============================================

# List is a collection of items which are ordered and changeable.
# Lists are denoted by squar brackets [] and items are separated by comma.
# To store various types of data
# ordered collection of items (Heterogeneous elems)

# student_details=["Isha",90,"Python","Delhi"]
# print(student_details)
# fruits=["Apple","Kiwi","Banana","cherry"]
# for i in fruits:
#     print("I Like ", i)

# ============================================
#      Accessing the elements (Indexing and Slicing)
# ============================================

# 1. Indexing : When we want to retrive single element from list

# marks=[20,30,40,50,60,70]
# print(len(marks))   # For counting the number of elements in list
# print(marks[2])  
# print(marks[-2])
# print("Marks are ::")
# for i in range(0,len(marks)):   # But we can use direct list name as above
#     print(marks[i])


a=[1,"ram",["shyam","krishna",[1,2,[1,2,3,[4,5,6]]]]]
print(a)
print(a[2][2][2][3][1])
print(a[len(a)-1])   # we can do this without counting and access the last element 
print(a[-len(a)])

# 2. Slicing : when we want to retrive a part of list

# #list[start:stop:step]
marks=[20,30,40,50,60,70]
print(marks[2:7:1])
print(marks[2:7])
print(marks[:7:2])
print(marks[:3:])
print(marks[::5])
print(marks[2])          # single Elem
print(marks[-2:-3:-1])  # Negative Indexing
print(marks[-6:-3:1])  
print(marks[::-1])  # Reverse
print(marks[::])    # Full List
l1 = list(range(0, 10))
print(l1)
print(l1[4:])

## printing of range fn
a=range(1,10)
print(type(a))
print(list(a)) 

l2 = list(range(0, 10))
print(l2)  

for i in range(1,100):
    if(i%3==0) and (i%5==0):
        print(i)

# ============================================
#        LIST METHODS
# ============================================

## Adding elements: append(), insert(), extend()

l1=[10,20,30,40,50]
print("Original List ::",l1)
l1.append(60)
print("Now List ::",l1)
l1.insert(2,100)
print("Now List ::",l1)
l1.extend([1,2,3,4])
print("Now List ::",l1)
l1.sort()
print("sorted List ::",l1)
l1.reverse()
print("reversed List ::",l1)
print("Original List ::",l1) # List is mutable

## Removing elements: remove(), pop(), clear()

l1=[10,20,30,40,50]
print("Original List ::",l1)
l1.remove(30)
print("Now List ::",l1)
l1.pop(2)
print("Now List ::",l1)
l1.clear()
print("Now List ::",l1)

## Other methods: count(), index(), sort(), reverse()

l1=['s','i','o','h','i']
print("Original List ::",l1)
print("Count of i in list ::",l1.count('i'))
print("Index of i in list ::",l1.index('i'))
l1.sort()
print("sorted List ::",l1)
l1.reverse()
print("reversed List ::",l1)

# my_list=[]
# for i in range(5):
#     num=int(input("enter Elem::"))
#     my_list.append(num)
# print(my_list)

# ============================================
#           LIST OPERATIONS
# ============================================

a=[1,2,3,4,5]
b=[10,20,30,40,50]

c=a+b
print(c)

d=a*2
print(d)

a.reverse()
print(a)

b.sort()  # ascending 
print(b)

b.sort(reverse=True)   # descending
print(b)

print(max(a))
print(min(a))
print(sum(a))
print(len(a))

# ============================================
#      Membership Test in List
# ============================================

LIST=[1,2,3,4,"isha"]
print("isha" in LIST)

# ============================================
#      ASCII Values
# ============================================

print(ord('A'))
print(ord('a'))
