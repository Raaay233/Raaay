"""
v1.3
添加打包单独文件的功能

v1.2
import方面进行优化，优化打包exe后大小
try部分的错误类型判断更为精确

v1.1
添加了判断路径中的无用字符
"""


from zipfile import ZipFile
from os import path, walk
from datetime import date
from time import sleep


def count_ignore_character(name):
    # 计算路径中的无用字符数量
    count = 0
    for i in name:
        if i == ' ' or i == '.':
            count += 1
    return count


def is_exists(name):
    # 检查路径是否可用
    directory = r'.\{}'.format(name)
    exists = path.exists(directory.strip())
    return exists, directory


def save_path():
    # 保存第一次输入的路径，并在下一次开启程序时调用
    try:
        with open('path.txt', 'r') as f:
            directory = f.read()
        return directory

    except FileNotFoundError:
        name = input('Please input the file/folder‘s name which you want to zip:\n')

        n = count_ignore_character(name)

        path_exists, directory = is_exists(name)

        while name == '' or not path_exists or n == len(name):
            name = input('The path IS NOT available! Please input the right file/folder‘s name!\n')
            n = count_ignore_character(name)

            path_exists, directory = is_exists(name)

        with open('path.txt', 'w') as f:
            f.write(directory)
        return directory


def get_all_file_paths(directory):
    file_paths = []
    if path.isfile(directory):
        file_paths.append(directory)
    else:
        # 把所有的文件夹以及子文件夹、以及文件全部搞出来
        for root, directories, files in walk(directory):
            for filename in files:
                # 得到完全路径
                filepath = path.join(root, filename)
                file_paths.append(filepath)

    return file_paths


def main(directory):
    today = date.today().strftime('%Y%m%d')

    file_paths = get_all_file_paths(directory)

    print('Following files will be zipped:')
    for file_name in file_paths:
        print(file_name)

    with ZipFile('{}_{}.zip'.format(directory, today), 'w') as zipp:
        for file in file_paths:
            zipp.write(file)

    print('All files zipped successfully!')
    sleep(1)


if __name__ == '__main__':
    directory = save_path()
    main(directory)
