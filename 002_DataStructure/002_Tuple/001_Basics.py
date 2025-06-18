# Tuple
# It is a collection of multiple values in an ordered sequence 
# They are immutable

## (list , dictionary , set are only mutable)
## ( all other like tuple,string , int , float are immutable)
# After modification too list has same id as it is mutable but not in integers,strings etc 

l1=[1,2,3,4]
print(id(l1))
l1[0]=100
print(id(l1))

T1=(1,2,3,4,5)
(10,20,30,40)
t1=1,2,3,4,5
# print(T1[0])=4000   # error
print(type(T1))
print(type(t1))

x=23,
print(type(x))

x=(23,)
print(type(x))

x=()           # empty Tuple
print(type(x))

y=56,"neha",True,78.5
print(type(y))

p,q = 10,20
print(type(p))
print(q)

p,q=q,p  # swapping
print(p)
print(q)

book=(100,"java",["abc","Macro hills"],(["v1","v2"]),"A")
book[2][0] ="ABC"   # we can change a list
print(book)
print(book[-1][-1])
print(book[3][0])
book[3][1]="V1.$"
print(book[3][1])
print(book)

book_list=list(book)
print(book_list)  

book_list=tuple(book)
# MemberShip Test in Tuple and list
print("java2" in book)
print("java" in book)

tuple1=(1,2,3,4,5)
tuple2=(10,20,30,40,50)
print(tuple1 + tuple2)
print(tuple1 * 3) # but no change in tuple
print(tuple1)
tuple1=tuple1*3  # now chnage in tuple
print(tuple1)

del(tuple1)
# print(tuple1)   # error as already deleted 

