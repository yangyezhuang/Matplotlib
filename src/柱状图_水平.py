import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'simhei'
plt.rcParams['axes.unicode_minus'] = False
font = {
    'family': 'SimHei',
    'weight': 'bold',
    'size': 16
}

labs = ["苹果", "梨子", "车厘子"]
v1 = [1000, 800, 2300]
v2 = [1200, 700, 2000]


def func():
    plt.title('水平条形图', fontdict=font)
    plt.barh(np.arange(len(labs)), v1, height=0.4, label='v1')
    for x, y in enumerate(v1):
        plt.text(y, x, y)
    plt.barh(np.arange(len(labs)) + 0.4, v2, height=0.4, label='v2')
    for x, y in enumerate(v2):
        plt.text(y, x + 0.4, y)
    plt.yticks(np.arange(len(labs)) + 0.4 / 2, labs)
    plt.legend(loc='lower right')
    plt.grid(axis='x',alpha=0.5)
    plt.show()


func()
