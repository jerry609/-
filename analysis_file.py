import os
import datetime
import sys


def display_file_or_directory_tree(path, prefix='', file=sys.stdout):
    if os.path.isfile(path):
        file_name = os.path.basename(path)
        file_size = os.path.getsize(path)
        mod_time = os.path.getmtime(path)
        mod_time_str = datetime.datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S')
        print(f"{file_name}", file=file)
        print(f"└── 文件大小: {file_size} 字节", file=file)
        print(f"└── 最后修改时间: {mod_time_str}", file=file)
    else:
        display_directory_tree(path, prefix, file)


def display_directory_tree(directory, prefix='', file=sys.stdout):
    try:
        contents = os.listdir(directory)
    except PermissionError:
        print(f"{prefix}└── 访问被拒绝", file=file)
        return

    files = [f for f in contents if os.path.isfile(os.path.join(directory, f))]
    dirs = [d for d in contents if os.path.isdir(os.path.join(directory, d))]

    for i, f in enumerate(files):
        if i == len(files) - 1 and not dirs:
            print(f"{prefix}└── {f}", file=file)
        else:
            print(f"{prefix}├── {f}", file=file)

    for i, d in enumerate(dirs):
        if i == len(dirs) - 1:
            print(f"{prefix}└── {d}", file=file)
            display_directory_tree(os.path.join(directory, d), prefix + "    ", file)
        else:
            print(f"{prefix}├── {d}", file=file)
            display_directory_tree(os.path.join(directory, d), prefix + "│   ", file)


if __name__ == "__main__":
    target_path = input("请输入要显示的文件或目录路径: ").strip('"')  # 去除可能的引号
    if os.path.exists(target_path):
        base_name = os.path.basename(target_path)
        output_file_name = f"{os.path.splitext(base_name)[0]}_tree.txt"

        with open(output_file_name, 'w', encoding='utf-8') as output_file:
            print(f"\n{base_name}", file=output_file)
            display_file_or_directory_tree(target_path, file=output_file)

        print(f"结果已保存到 {output_file_name}")
    else:
        print("指定的路径不存在。")