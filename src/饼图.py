import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'simhei'
plt.rcParams['axes.unicode_minus'] = False

font = {
    'size': 20
}

name = ["面粉", "砂糖", "牛奶", "草莓酱", "果汁"]
data = [12, 34, 26, 19, 22]


def pie_graph():
    plt.title('饼图', fontdict=font)
    explode = [0.05] * len(data)
    plt.pie(data, explode, autopct='%.2f%%', shadow=True)
    plt.legend(name, bbox_to_anchor=(-0.5, 0, 0.5, 1))
    plt.show()


if __name__ == '__main__':
    pie_graph()
