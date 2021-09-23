import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'simhei'

name = ['一月', '二月', '三月', '四月']
v1 = [23, 25, 34, 11]
v2 = [16, 8, 14, 17]


def bar():
    plt.title('堆积柱状图')
    plt.xlabel('月份')
    plt.ylabel('销售额')
    plt.bar(name, v1, width=0.5, label='v1')
    for x,y in enumerate(v1):
        plt.text(x,y,y)
    plt.bar(name, v2, width=0.5, bottom=v1, label='v2')
    for x,y in enumerate(v2):
        plt.text(x,y,y)
    plt.legend()
    plt.grid(axis='y',alpha=0.5)
    plt.show()


if __name__ == '__main__':
    bar()
