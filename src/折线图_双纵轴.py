import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'simhei'
font = {
    'size': 16
}

x = ['a', 'b', 'c', 'd', 'e', 'f']
y1 = [30481, 12583, 51, 9, 4442, 2]
y2 = [0.165, 0.016, 0.039, 0, 0.065, 0]


def twinx_line_graph():
    plt.title('双Y轴折线图', fontdict=font)
    plt.plot(x, y1, 'd-', label='销售人次')
    plt.xlabel('种类')
    plt.ylabel('销量')
    plt.legend(loc='upper center')

    ax2 = plt.twinx()
    ax2.plot(x, y2, 'ro--', label='本月销售量')
    ax2.set_ylabel('利率')
    ax2.legend()
    plt.show()


if __name__ == '__main__':
    twinx_line_graph()
