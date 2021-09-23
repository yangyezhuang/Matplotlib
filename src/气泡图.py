import matplotlib.pyplot as plt
import numpy as np

a = np.random.randn(100)
b = np.random.randn(100)

plt.scatter(a, b, s=np.power(10*a + 20*b, 2),
            c=np.random.rand(100),
            cmap=plt.cm.RdYlBu,
            marker="o")
plt.show()