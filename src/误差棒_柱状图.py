import matplotlib.pyplot as plt


plt.rcParams["font.sans-serif"] = "SimHei"
plt.rcParams["axes.unicode_minus"] = False


x = ["园区1", "园区2", "园区3", "园区4", "园区5"]
y = [100, 68, 79, 91, 82]
std_err = [7, 5, 6, 8, 5]  # 误差值
err_style = dict(elinewidth=2, ecolor="black", capsize=3)

'''
带误差棒的柱状图的关键要点在于函数bar（）中关键字参数yerr的使用，
误差棒的属性由关键字error_kw控制
'''
plt.bar(x, y, color="c", width=0.6, yerr=std_err, error_kw=err_style)
plt.xlabel("芒果种植区")
plt.ylabel("收割量")
plt.title("不同芒果种植区的单次收割量")
plt.grid(axis="y",  color="gray", alpha=0.3)
plt.show()
