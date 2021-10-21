import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family']='simhei'

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.title('绘制平行于x/y轴的水平参考线')
plt.plot(x, y, ls="-.", lw=2, c="c", label="plot figure")
# 函数axhline()/axvline() 绘制平行于x/y轴的水平参考线
plt.axhline(y=0.0, c='r', ls='--', lw=2)
plt.axvline(x=4, c='r', ls='--', lw=2)

plt.legend()
plt.show()
