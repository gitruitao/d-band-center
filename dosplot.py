import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# 文件路径
file_path = sys.argv[1]

# 读取文件并处理数据
data = np.loadtxt(file_path)

# 提取第一列作为x轴
x = data[:, 0]

# 计算y1和y2
y1 = data[:, 8] + data[:, 10] + data[:, 12] + data[:, 14] + data[:, 16]
y2 = data[:, 9] + data[:, 11] + data[:, 13] + data[:, 15] + data[:, 17]

# 设置字体为Times New Roman, 字体大小为14
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 15
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{times}'

# 绘制图表
plt.figure(figsize=(10, 6))
plt.plot(x, y1, color='blue', linestyle='-', label='Spin-up')
plt.fill_between(x, y1, color='blue', alpha=0.5)
# plt.fill_between(x, y1, color='blue')

plt.plot(x, y2, color='red', linestyle='-', label='Spin-down')
plt.fill_between(x, y2, color='red', alpha=0.5)
# plt.fill_between(x, y2, color='red')

# 添加表示费米能级的垂直虚线
plt.axvline(x=0, color='black', linestyle='--', linewidth=1)

# 设置横坐标范围
plt.xlim(-20, 10)
plt.ylim(-6, 6)

# 设置带有下标的xlabel
plt.xlabel(r'$\mathrm{E}-\mathrm{E}_f$ (eV)')  # 使用LaTeX格式的字符串
                 
# plt.xlabel('First column data (x)')
plt.ylabel(r'DOS (electron/eV)')
# plt.title('Electronic Density of States')

# 设置图例，并去掉图例边框
plt.legend(frameon=False)

# 取消图表的边框
ax = plt.gca()

# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.spines['left'].set_visible(False)
# ax.spines['bottom'].set_visible(False)

plt.grid(False)

# 动态获取文件名并保存图表为jpg文件
file_name = os.path.splitext(os.path.basename(file_path))[0]
output_path = f'{file_name}.jpg'
plt.savefig(output_path, format='jpg')

# plt.show()
