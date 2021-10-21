import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'simhei'
plt.rcParams['axes.unicode_minus'] = False


def scatter():
    plt.title('散点图')
    X = np.random.randn(100)
    Y = np.random.randn(100)
    plt.scatter(X, Y, color='green', marker='D')
    plt.show()


if __name__ == '__main__':
    scatter()
