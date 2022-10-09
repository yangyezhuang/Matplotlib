import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'simhei'
plt.rcParams['axes.unicode_minus'] = False

name = ["家庭", "小说", "心理", "科技"]
v1 = [12, 34, 26, 19]
v2 = [21, 29, 33, 25]


# 叠加柱状图
def func():
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
    plt.show()


if __name__ == '__main__':
    func()
