# # 🔹Line Plot
# import matplotlib.pyplot as plt
# x=[1,2,3,4]
# y=[10,20,30,40]
# plt.plot(x, y)                 # Plot line chart
# plt.title("Simple Line Graph") # Add a title
# plt.xlabel("X Axis")           # Label X
# plt.ylabel("Y Axis")           # Label Y
# plt.grid(True)                 # Show grid
# plt.show()                     # Display the plot


# # line graph by taking 5 values from users and given x=0,1,2,3,4.
import matplotlib.pyplot as plt
x=[0,1,2,3,4]             # taking lots of time   (do in google colab)
y=[] 
for i in range(5):
    n=int(input("Enter NO.: "))
    y.append(n)
plt.plot(x,y)
plt.show