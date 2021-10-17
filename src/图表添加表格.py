import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "SimHei"
plt.rcParams["axes.unicode_minus"] = False


class Project:
    # 绘图部分
    def graph(self):
        labs = "A级难度", "B级难度", "C级难度", "D级难度"
        students = [0.35, 0.15, 0.20, 0.30]
        explode = [0.05] * 4
        plt.title("选择不同难度测试试卷的学生占比")
        plt.pie(students, explode, labs, autopct="%.1f%%", shadow=True)

    # 表格部分
    def table(self):
        colLabels = ["语文", "数学", "英语", "物理"]
        rowLabels = ["alice", 'tom']
        Values = [[112, 130, 98, 88],
                  [101, 122, 99, 95]]

        colColors = ["r", "g", "b", "y"]
        plt.table(cellText=Values,  # 表格数据
                  cellLoc="center",  # 数据左右对齐方式
                  colWidths=[0.3] * 4,
                  colLabels=colLabels,  # 行标签
                  colColours=colColors,
                  rowLabels=rowLabels,  # 列标签
                  rowLoc="center")  # 数据上下对齐方式


def main():
    p = Project()
    p.graph()
    p.table()
    plt.show()


if __name__ == '__main__':
    main()
