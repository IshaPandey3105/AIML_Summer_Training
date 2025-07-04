file=open("Text.txt","w")  # file is object of file class
file.write("Hello!!  ")     # write function is used to write data in file
name=input("Enter Your Name :")
C_name=input("Enter Your College Name :")
age=input("Enter Your age :")
file.write(name)
file.write(C_name)
file.write(age)
file.close()

# file=open("Text.txt","r")
# print(file.read())
# file.close()

# if we dont want to close manually we can use with keyword
with open("Text.txt","r") as file:
    print(file.read())
