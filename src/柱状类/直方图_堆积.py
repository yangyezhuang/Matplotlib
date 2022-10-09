import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'simhei'
plt.rcParams['axes.unicode_minus'] = False

scoresT1 = np.random.randint(0, 100, 100)
scoresT2 = np.random.randint(0, 100, 100)
x = [scoresT1, scoresT2]

labels = ["班级A", "班级B"]
bins = range(0, 100, 10)
plt.hist(x, bins=bins, histtype="bar",
         rwidth=1.0, stacked=True, label=labels)
plt.xlabel("测试成绩(分)")
plt.ylabel("学生人数")
plt.title("不同班级的测试成绩的直方图")
plt.legend(loc="upper left")
plt.show()
