import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'simhei'
font = {
    'size': 20
}

data = [0.3, 0.25, 0.16, 0.14, 0.15]
label = ["面粉", "砂糖", "奶油", "果酱", "坚果"]


def ring_graph():
    explode = [0] * len(label)
    plt.title('环形图', fontdict=font)
    plt.pie(data, explode, pctdistance=0.8, autopct='%.2f%%',
            wedgeprops=dict(width=0.4, edgecolor='w'))
    # radius：半径
    # pctdistance：控制数字与圆心间的距离
    plt.legend(label, bbox_to_anchor=(-0.5, 0, 0.5, 1))
    plt.show()


if __name__ == '__main__':
    ring_graph()
