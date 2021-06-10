import matplotlib.pyplot as plt

# initializing the data
x = [10, 10]
y = [45, 20]

x1 = [10, 15]
y1 = [45, 30]

x2 = [15, 20]
y2 = [30, 45]

x3 = [20, 20]
y3 = [45, 20]

x4 = [25, 25]
y4 = [45, 20]

x5 = [25, 35]
y5 = [20, 20]

x6 = [35, 35]
y6 = [45, 20]

x7 = [40, 40]
y7 = [45, 20]

x8 = [40, 50]
y8 = [20, 25]

x9 = [40, 50]
y9 = [45, 40]

x10 = [50, 50]
y10 = [40, 25]

x11 = [55, 75]
y11 = [45, 45]

x12 = [65, 65]
y12 = [45, 25]

x13 = [60, 65]
y13 = [20, 25]

x14 = [60, 55]
y14 = [20, 25]

x15 = [55, 55]
y15 = [25, 30]

# plotting the data
plt.plot(x, y)
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.plot(x6, y6)
plt.plot(x7, y7)
plt.plot(x8, y8)
plt.plot(x9, y9)
plt.plot(x10, y10)
plt.plot(x11, y11)
plt.plot(x12, y12)
plt.plot(x13, y13)
plt.plot(x14, y14)
plt.plot(x15, y15)

# Adding the title
plt.title("Simple Plot")

# Adding the labels
plt.ylabel("y-axis")
plt.xlabel("x-axis")

plt.show()
