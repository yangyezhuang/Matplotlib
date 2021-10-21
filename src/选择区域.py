import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x, y, ls="-.", lw=2, c="c", label="plot figure")
# axvspan()函数绘制垂直于x轴的参考区域
plt.axhspan(ymin=0.0, ymax=0.5, color='c', alpha=0.3)
plt.axvspan(xmin=4.0, xmax=6.0, color='pink', alpha=0.3)

plt.legend()
plt.show()