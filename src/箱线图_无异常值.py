import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"] = "SimHei"
plt.rcParams["axes.unicode_minus"] = False

x = np.random.randn(1000)

plt.boxplot(x, vert=False, showfliers=False)
# vert：是否将箱线图垂直摆放，默认垂直摆放
# showfliers：是否显示异常值，默认显示；
plt.xlabel("随机数值")
plt.yticks([1], ["随机数生成器AlphaRM"], rotation=90)
plt.title("无异常值水平箱线图")
plt.grid(axis="x", ls=":", lw=1, color="gray", alpha=0.4)
plt.show()
