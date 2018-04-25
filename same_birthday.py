import matplotlib.pyplot as plt
import numpy as np

print("Find the probability of existing at least one peer of same birth day in the group")
print("n: the number of people in a group")

x = np.linspace(2, 366, 364)
y = []
no_match = 1
for n in range(2, 366):
	no_match *= (366-n) / 365
	match = 1 - no_match
	y.append(match)
	print("n = %3d: %f" % (n, match))

plt.plot(x, y)
plt.show()