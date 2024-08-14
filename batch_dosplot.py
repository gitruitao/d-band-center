import os
import sys
import subprocess

def process_directory(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):  # 只处理文件
            print(f"Processing file: {filepath}")
            # sys.executable表示类似/usr/local/bin/python的绝对路径
            subprocess.run([sys.executable, 'dosplot.py', filepath])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python batch_dosplot.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"{directory} is not a valid directory.")
        sys.exit(1)

    process_directory(directory)

