import os
import sys
import numpy as np
import matplotlib.pyplot as plt

def process_file(file_path):
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
    plt.plot(x, y2, color='red', linestyle='-', label='Spin-down')
    plt.fill_between(x, y2, color='red', alpha=0.5)
    plt.axvline(x=0, color='black', linestyle='--', linewidth=1)
    plt.xlim(-20, 10)
    plt.ylim(-6, 6)
    plt.xlabel(r'$\mathrm{E}-\mathrm{E}_f$ (eV)')
    plt.ylabel(r'DOS (electron/eV)')
    plt.legend(frameon=False)
    plt.grid(False)

    # 动态获取文件名并保存图表为jpg文件
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    output_path = f'{file_name}.jpg'
    plt.savefig(output_path, format='jpg')
    plt.close()

def process_directory(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):  # 只处理文件
            print(f"Processing file: {filepath}")
            process_file(filepath)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    if os.path.isfile(directory):
        process_file(directory)

    elif not os.path.isdir(directory):
        print(f"{directory} is not a valid directory.")
        sys.exit(1)
    else:
        process_directory(directory)
