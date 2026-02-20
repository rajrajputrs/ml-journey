import matplotlib.pyplot as plt

# 1. Line Plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, marker='o', color='green', linestyle='--')
plt.title("Line Plot Example")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

# 2. Scatter Plot
x = [5, 7, 8, 7, 2, 17, 2, 9]
y = [99, 86, 87, 88, 100, 86, 103, 87]

plt.scatter(x, y, color='red')
plt.title("Scatter Plot Example")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

# 3. Bar Chart
categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]

plt.bar(categories, values, color='purple')
plt.title("Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# 4. Histogram
data = [1,2,2,3,3,3,4,4,4,4,5,5,6,7,7,8]

plt.hist(data, bins=5, color='orange', edgecolor='black')
plt.title("Histogram Example")
plt.xlabel("Bins")
plt.ylabel("Frequency")
plt.show()
