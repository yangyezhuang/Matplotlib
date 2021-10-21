import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "SimHei"
plt.rcParams["axes.unicode_minus"] = False

testA = np.random.randn(5000)
testB = np.random.randn(5000)
testList = [testA, testB]
labels = ["随机数生成器AlphaRM", "随机数生成器BetaRM"]
colors = ["#1b9e77", "#d95f02"]


bplot = plt.boxplot(testList, whis=1.6, widths=0.35,
                    sym="o", labels=labels, patch_artist=True)
for patch, color in zip(bplot["boxes"], colors):
    patch.set_facecolor(color)
plt.ylabel("随机数值")
plt.title("生成器抗干扰能力的稳定性比较")
plt.grid(axis="y", ls=":", lw=1, color="gray", alpha=0.4)
plt.show()
