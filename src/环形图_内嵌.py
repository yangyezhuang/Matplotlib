import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

a = [0.4, 0.15, 0.2, 0.1, 0.15]
b = [0.3, 0.25, 0.16, 0.14, 0.15]
label = ["面粉", "砂糖", "奶油", "果酱", "坚果"]
color = ['pink', 'greenyellow', 'lightcoral', 'yellow', 'cyan']

plt.title("面包配料百分比")
# 外环
plt.pie(a, autopct="%.1f%%", radius=1,  pctdistance=0.85, colors=color,
        wedgeprops=dict(width=0.3, edgecolor='w'))

# 内环
plt.pie(b,  autopct="%.1f%%", radius=0.7, pctdistance=0.75, colors=color,
        wedgeprops=dict(width=0.3, edgecolor='w'))

'''
radius：饼图半径，默认值为1
pctdistance：饼块内标签与圆心的距离，默认值为0.6，autopct不为None该参数生效
shadow：饼图下是否有阴影，默认值为False
wedgeprops：饼块属性。字典。默认值为None
wedgeprops -> width：饼块宽度
wedgeprops -> edgecolor：饼块边缘线颜色
'''

plt.legend(label, fontsize=12, title="颜料表",
           loc="center left", bbox_to_anchor=(-0.3, 0, 0.5, 1))
plt.show()
