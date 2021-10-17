import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'simhei'

name = ['时尚酒店', '大宝饭店', '798精品店', '得福宾馆']
v1 = [12, 34, 26, 19]
v2 = [17, 28, 33, 24]


def line_graph():
    plt.title('折线图', fontsize=18)
    plt.plot(name, v1, 'o--', label='一月')
    plt.plot(name, v2, 'd-', label='二月')
    plt.ylabel('销售额')
    plt.legend()
    plt.grid(axis='y', alpha=0.5)
    plt.show()


if __name__ == '__main__':
    line_graph()
