import matplotlib.pyplot as plt
import numpy as np


def hist():
    plt.title('直方图')
    x = np.random.normal(size=100)
    plt.hist(x, bins=30)
    plt.show()


if __name__ == '__main__':
    hist()
