import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

'''
# Functional method
plt.plot(x, y, 'blue')
plt.xlabel('X label')
plt.ylabel('Y label')
plt.title('Title')

plt.subplot(1, 2, 1)

plt.show()
'''

# Object-Oriented Method
'''
fig = plt.figure()

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

axes.plot(x, y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Title')
'''

'''
fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

axes1.plot(x, y)
axes2.plot(y, x)
'''

# fig, axes = plt.subplots(nrows=1, ncols=2)
# for current_ax in axes:
#     current_ax.plot(x, y)

# axes[0].plot(x, y)
# axes[0].set_title('First Plot')

'''
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 2))  # dpi=100

axes[0].plot(x, y)
axes[1].plot(y, x)

fig.savefig('my_picture.png', dpi=200)  # dpi=200
'''

'''
fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

# ax.set_title('Title')
# ax.set_xlabel('TRALALA')
# ax.set_ylabel('HOPASA')

ax.plot(x, x**2, label='X Squared')
ax.plot(x, x**3, label='X Cubed')

ax.legend(loc=0)  # 0 = best location
'''

fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

# color='#FF8C00' | linewidth == lw | linestyle == ls
ax.plot(x, y, color='orange', linewidth=4, alpha=0.5, linestyle='--',
        marker='*', markersize=20, markerfacecolor='blue', markeredgewidth=3, markeredgecolor='green')

# ax.set_xlim([0, 1])


plt.tight_layout()
plt.show()
