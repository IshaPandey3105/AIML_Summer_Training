# ============================================
#                QUESTIONS
# ============================================

## Q1 Create a tuple with data of three books(name,prize,pages) and print data vertically
BOOK1=("B1",100.0,500)
BOOK2=("B2",300.0,1000)
BOOK3=("B3",1000.50,2000)
BOOK=(BOOK1,BOOK2,BOOK3)
for i in BOOK:
    print(i)
    for j in i:
        print(j)



