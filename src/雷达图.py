import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = 'simhei'

name = ['语文', '数学', '英语', '物理', '化学']
v1 = [77, 92, 83, 74, 90]
v2 = [63, 88, 99, 69, 66]


def radar(name, v1, v2):
    plt.subplot(projection='polar')
    plt.title('雷达图', fontsize=16)
    
    theta = np.linspace(0, 2 * np.pi, len(v1), endpoint=False)
    theta = np.concatenate((theta, [theta[0]]))
    name = np.concatenate((name, [name[0]]))
    v1 = np.concatenate((v1, [v1[0]]))
    v2 = np.concatenate((v2, [v2[0]]))

    plt.polar(theta, v1, 'ro-')
    plt.fill(theta, v1, 'pink', alpha=0.5, label='小明')
    plt.polar(theta, v2, 'bo-')
    plt.fill(theta, v2, 'c', alpha=0.3, label='小王')
    plt.thetagrids(theta * 180 / np.pi, name)
    plt.legend(bbox_to_anchor=(-0.6,0,0.5,1))
    plt.ylim(0, 110)
    plt.show()


if __name__ == '__main__':
    radar(name, v1, v2)
