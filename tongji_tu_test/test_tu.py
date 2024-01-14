import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

# 提示用户输入Excel文件路径
# excel_path = input("请输入待分析的Excel文件路径：")
excel_path = "D:\\Documents\\WeChat Files\\wxid_kbfebowxoeon22\\FileStorage\\File\\2024-01\\test.xlsx"

# 读取Excel数据
data = pd.read_excel(excel_path)
# 提取每个月份的降水量数据
monthly_data = data.iloc[1:, 1:]
# 设置英文显示
plt.rcParams['font.family'] = 'sans-serif'
# 绘制箱型线图
plt.figure(figsize=(12, 6))
# 去除背景网格线
plt.grid(True)
# 绘制箱型线图
sns.boxplot(data=monthly_data, palette='Blues', width=0.5, fliersize=5)

# 绘制每个月份的散点图
colors = sns.color_palette('BuGn', n_colors=12)
for i, col in enumerate(monthly_data.columns):
    x = [i] * len(monthly_data[col])
    y = monthly_data[col]
    plt.scatter(x, y, color=colors[i], alpha=0.5, s=20)

# 设置标题和标签
plt.title('Monthly Precipitation Distribution', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Precipitation (mm)', fontsize=12)
# 设置x轴刻度标签为月份的缩写
plt.xticks(range(0, 12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], fontsize=10)
# 显示图例
legend_labels = ['Scatter']
plt.legend(legend_labels)
# 显示图像
plt.show()


