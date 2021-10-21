import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'simhei'


title = ['福建', '辽宁', '河北', '安徽', '广东', '山东', '陕西', '广西']
value = [144, 127, 188, 162, 139, 155, 177, 166]
value = np.sort(value)


def rose_graph():
    theta = np.linspace(0, 2 * np.pi, len(title), endpoint=False)

    plt.polar()
    plt.bar(theta, value,
            width=0.79,  # 控制宽度
            color=np.random.random((len(value), 3)),
            bottom=50)  # 中间空白区域大小

    for t, v in zip(theta, value):  # 柱状图数量
        plt.text(t, v + 70, v, fontsize=12)

    plt.title('南丁格尔玫瑰图', fontsize=15)
    plt.axis(False)  # 关闭极坐标轴
    plt.tight_layout()  # 自动调节子图大小
    plt.show()


if __name__ == '__main__':
    rose_graph()
