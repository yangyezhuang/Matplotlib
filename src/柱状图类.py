import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'simhei'
plt.rcParams['axes.unicode_minus'] = False

name = ["家庭", "小说", "心理", "科技"]
v1 = [12, 34, 26, 19]
v2 = [21, 29, 33, 25]

plt.figure(figsize=(12, 6))
plt.subplots_adjust(wspace=0.6, hspace=0.5)
plt.suptitle('柱状图类', fontsize=20)


class Graph:
    def __init__(self):
        pass

    def bar(self):
        plt.subplot(231)
        plt.title('柱状图')
        plt.bar(name, v1, width=0.5, label='v1')
        for i, j in zip(range(len(name)), v1):
            plt.text(i, j, j, ha='center', va='bottom')
        plt.grid(axis='y', alpha=0.5)
        plt.legend()

    # 并列柱状图
    def bar_bl(self):
        plt.subplot(232)
        plt.title('并列柱状图')
        plt.bar(name, v1, width=0.3, label='v1')
        plt.bar(np.arange(len(name)) + 0.3, v2, width=0.3, label='v2')
        for x, y in zip(range(len(name)), v1):
            plt.text(x, y, y, ha='center', va='bottom')
        plt.legend(bbox_to_anchor=[0.9, 0, 0.5, 1])
        plt.grid(axis='y', alpha=0.5)

    # 叠加柱状图
    def bar_dj(self):
        plt.subplot(233)
        plt.title('叠加柱状图')
        plt.bar(range(len(v1)), v1, label='v1')
        for x, y in zip(range(len(name)), v1):
            plt.text(x, y, y, va='bottom')
        plt.bar(range(len(v2)), v2, bottom=v1, label='v2')
        for x, y in zip(range(len(name)), v2):
            plt.text(x, y, y, va='top')
        plt.legend(bbox_to_anchor=[0.9, 0, 0.5, 1])
        plt.plot(name, v1, 'r', marker='d')
        plt.grid(axis='y', alpha=0.5)

    # 条形图
    def barh(self):
        plt.subplot(234)
        plt.title('水平柱状图')
        plt.barh(name, v1, height=0.6, label='v1')
        for x, y in enumerate(v1):
            plt.text(y, x, y)
        plt.grid(axis='x', alpha=0.5)
        plt.legend()

    # 并列条形图
    def barh_bl(self):
        plt.subplot(235)
        plt.title('水平并列柱状图')
        plt.barh(np.arange(len(v1)), v1, height=0.4, label='v1')
        for x, y in enumerate(v1):
            plt.text(y, x, y)
        plt.barh(np.arange(len(v2)) + 0.4, v2, height=0.4, label='v2')
        for x, y in enumerate(v2):
            plt.text(y, x + 0.4, y)
        plt.legend(bbox_to_anchor=[0.9, 0, 0.5, 1])
        plt.yticks(np.arange(len(name)), name)
        plt.grid(axis='x', alpha=0.5)

    # 叠加条形图
    def barh_dj(self):
        plt.subplot(236)
        plt.title('水平堆积柱状图')
        plt.barh(range(len(v1)), v1, height=0.6, label='v1')
        plt.barh(range(len(v2)), v2, height=0.6, left=v1, label='v2')
        plt.legend(loc='upper right', bbox_to_anchor=[0.9, 0, 0.5, 1])
        plt.yticks(np.arange(len(name)), name)
        plt.grid(axis='x', alpha=0.5)


def main():
    g = Graph()
    g.bar()
    g.bar_bl()
    g.bar_dj()
    g.barh()
    g.barh_bl()
    g.barh_dj()
    plt.show()


if __name__ == '__main__':
    main()
