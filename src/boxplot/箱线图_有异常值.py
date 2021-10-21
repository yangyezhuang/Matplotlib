import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "SimHei"
plt.rcParams["axes.unicode_minus"] = False

x = np.random.randn(1000)

plt.boxplot(x, vert=False)
plt.xlabel("随机数值")
plt.yticks([1], ["随机数生成器AlphaRM"], rotation=90)
plt.title("有异常值的水平箱线图")
plt.grid(axis="x", ls=":", lw=1, color="gray", alpha=0.4)
plt.show()
