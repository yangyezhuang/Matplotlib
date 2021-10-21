import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.5, 2 * np.pi, 20)
y = np.random.randn(20)

plt.stem(x, y, linefmt="-.", markerfmt="o", basefmt="-")

if __name__ == '__main__':
    plt.show()
