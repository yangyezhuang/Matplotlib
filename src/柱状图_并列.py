import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'simhei'

name = ['苹果', '梨', '香蕉', '葡萄']
d1 = [23, 25, 34, 11]
d2 = [16, 11, 14, 17]


def plot():
    plt.title('并列柱状图')
    plt.xticks(np.arange(len(name)), name)
    plt.bar(np.arange(len(name)), d1, width=0.3, label='一月')
    for x, y in enumerate(d1):
        plt.text(x, y, y, ha='center', va='bottom')
    plt.bar(np.arange(len(name)) + 0.3, d2, width=0.3, label='二月')
    for x, y in enumerate(d2):
        plt.text(x + 0.3, y, y, ha='center', va='bottom')
    plt.xticks(np.arange(len(name)) + 0.3 / 2, name)
    plt.legend()
    plt.ylim(0, 50)
    plt.ylabel('销售额')
    plt.grid(axis='y', alpha=0.5)
    plt.show()


if __name__ == '__main__':
    plot()
