import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "SimHei"
plt.rcParams["axes.unicode_minus"] = False

x = ["家庭", "小说", "心理", "科技", "儿童"]
y = [1200, 2400, 1800, 2200, 1600]
std_err = [150, 100, 180, 130, 80]
colors = ["#e51a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00"]
err_style = dict(ecolor='black', elinewidth=2, capsize=4)

plt.title("不同图书种类的采购情况")
plt.barh(x, y, height=0.6, xerr=std_err, error_kw=err_style, color=colors)
plt.grid(axis="x", color="gray", alpha=0.3)
plt.xlim(0, 2600)
plt.show()
