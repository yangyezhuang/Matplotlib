import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'simhei'
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(12, 6))
plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.suptitle('极轴类合集', fontsize=20)


class Graph(object):
    def __init__(self):
        self.font = {
            'size': 12
        }

    def pie(self):
        plt.subplot(231)
        plt.title('饼图', fontdict=self.font)
        explode = [0.01] * len(subjects)
        plt.pie(v1, explode, pctdistance=0.7, autopct='%.2f%%')
        plt.legend(subjects, loc='upper left', bbox_to_anchor=[1, 0, 0.5, 1], fontsize=7)

    def ring(self):
        plt.subplot(232)
        plt.title('环形图', fontdict=self.font)
        explode = [0.01] * len(subjects)
        plt.pie(v2, explode, autopct='%.1f%%', pctdistance=0.8, wedgeprops=dict(width=0.5, edgecolor='w'))
        plt.legend(loc='upper left', bbox_to_anchor=[1, 0, 0.5, 1], fontsize=7)

    def two_ring(self):
        plt.subplot(233)
        a = [0.4, 0.15, 0.2, 0.1, 0.15]
        b = [0.3, 0.25, 0.16, 0.14, 0.15]
        label = ["面粉", "砂糖", "奶油", "果酱", "坚果"]
        color = ['pink', 'greenyellow', 'lightcoral', 'yellow', 'cyan']
        plt.title('内嵌环形图', fontdict=self.font)
        plt.pie(a, autopct='%.1f%%', radius=1, pctdistance=0.85, colors=color,
                wedgeprops=dict(edgecolor='w', width=0.3))
        plt.pie(b, autopct='%.1f%%', radius=0.7, pctdistance=0.65, colors=color,
                wedgeprops=dict(edgecolor='w', width=0.3))
        plt.legend(label, fontsize=7, title="颜料表",
                   bbox_to_anchor=[1, 0, 0.5, 1])

    def radar(self, subjects, v1):
        plt.subplot(234, projection='polar')
        plt.title('雷达图', fontdict=self.font)
        theta = np.linspace(0, 2 * np.pi, len(subjects), endpoint=False)
        theta = np.concatenate((theta, [theta[0]]))
        subjects = np.concatenate((subjects, [subjects[0]]))
        v1 = np.concatenate((v1, [v1[0]]))
        plt.polar(theta, v1)
        plt.fill(theta, v1, color='c', alpha=0.4, label='v1')
        plt.thetagrids(theta * 180 / np.pi, subjects)
        plt.legend(loc='upper left', bbox_to_anchor=[1, 0, 0.5, 1], fontsize=7)

    def two_radar(self, subjects, v1, v2):
        plt.subplot(235, projection='polar')
        plt.title('多线雷达图', fontdict=self.font)
        theta = np.linspace(0, 2 * np.pi, len(subjects), endpoint=False)
        theta = np.concatenate((theta, [theta[0]]))
        subjects = np.concatenate((subjects, [subjects[0]]))
        v1 = np.concatenate((v1, [v1[0]]))
        v2 = np.concatenate((v2, [v2[0]]))
        plt.polar(theta, v1)
        plt.fill(theta, v1, alpha=0.3, label='v1')
        plt.polar(theta, v2)
        plt.fill(theta, v2, alpha=0.3, label='v2')
        plt.thetagrids(theta * 180 / np.pi, subjects)
        plt.legend(loc='upper left', bbox_to_anchor=[1, 0, 0.5, 1], fontsize=7)

    def rose(self):
        plt.subplot(236, projection='polar')
        plt.title('玫瑰图', fontdict=self.font)
        theta = np.linspace(0, 2 * np.pi, len(subjects), endpoint=False)
        plt.polar()
        plt.bar(theta, v1, width=1.3, bottom=30,
                color=np.random.random((len(v1), 4)))
        for i in range(len(subjects)):
            plt.text(theta[i], v1[i] / 2, subjects[i] + str(v1[i]),
                     rotation=theta[i] * 180 / np.pi,  # 文字角度
                     rotation_mode='anchor',  # 标签起始位置不再是左上角
                     size=8)
        plt.axis(False)


def main():
    g = Graph()
    g.pie()
    g.ring()
    g.two_ring()
    g.radar(subjects, v1)
    g.two_radar(subjects, v1, v2)
    g.rose()
    plt.show()


if __name__ == '__main__':
    subjects = ['语文', '数学', '英语', '物理', '化学']
    v1 = [77, 92, 83, 74, 90]
    v2 = [63, 88, 99, 69, 66]
    main()
