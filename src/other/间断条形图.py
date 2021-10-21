import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'simhei'
plt.rcParams['axes.unicode_minus'] = False

x = [(30, 100), (180, 50), (260, 70)]
y = [(60, 90), (190, 20), (230, 30), (280, 60)]

plt.title("不同区域的歌剧院的演出时间比较")
plt.broken_barh(x, (20, 8), facecolors="#1f78b4")
plt.broken_barh(y, (10, 8), facecolors=(
    "#7fc97f", "#beaed4", "#fdc086", "#ffff99"))
plt.xlim(0, 360)
plt.ylim(5, 35)
plt.xlabel("演出时间")
plt.xticks(np.arange(0, 361, 60))
plt.yticks([15, 25], ["歌剧院A", "歌剧院B"])
plt.grid(ls="-", lw=1, color="gray")
plt.show()
