import matplotlib.pyplot as plt

x_values = range(6)
y_values = [x**2 for x in x_values]

plt.style.use('tableau-colorblind10')
fig, ax = plt.subplots()

ax.plot(x_values, y_values,linewidth=3)
ax.set_title('square NUmbers',fontsize=24)
ax.set_xlabel('Value',fontsize=24)
ax.set_ylabel('square NUmbers',fontsize=24)

ax.tick_params('both',labelsize=14)
plt.show()
