import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'simhei'
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(1, 10, 10)
y = np.sin(x)

plt.title('阶梯图',fontsize=16)
plt.step(x, y, where="pre", lw=2)
plt.xlim(0, 11)
plt.xticks(np.arange(1, 11, 1))
plt.ylim(-1.2, 1.2)
plt.show()
