import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'simhei'
plt.rcParams['axes.unicode_minus'] = False

x = np.arange(1, 6, 1)
y = [0, 4, 3, 5, 6]
y1 = [1, 3, 4, 2, 7]
y2 = [3, 4, 1, 6, 5]

labels = ["BluePlanet", "BrownPlanet", "GreenPlanet"]

plt.title('堆积折线图')
plt.stackplot(x, y, y1, y2, labels=labels)
plt.legend(loc="upper left")
plt.show()
