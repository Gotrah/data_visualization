import matplotlib.pyplot as plt

# input_values = []
# squares = []
#
# for i in range(1, 10):
#     input_values.append(i)
#     squares.append(i * i)

input_values = range(1, 1001)
cubes = [x ** 3 for x in input_values]

plt.style.use('seaborn')
# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
# ax.plot(input_values, squares, linewidth=3)
ax.scatter(input_values, cubes, c=cubes, cmap=plt.cm.Reds, s=10)

# ax.axis([0, 1100, 0, 1_100_000])
# ax.ticklabel_format(style='plain')

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

plt.show()
# plt.savefig('squares_plot.png', bbox_inches='tight')
