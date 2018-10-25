"v1.1"


from zipfile import ZipFile
import os
import datetime
import time


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
    exists = os.path.exists(directory.strip())
    return exists, directory


def save_path():
    # 保存第一次输入的路径，并在下一次开启程序时调用
    try:
        with open('path.txt', 'r') as f:
            directory = f.read()
        return directory

    except Exception:
        name = input('Please input the name which you want to zip:\n')

        n = count_ignore_character(name)

        path_exists, directory = is_exists(name)

        while name == '' or not path_exists or n == len(name):
            name = input('The path IS NOT available! Please input the right name!\n')
            n = count_ignore_character(name)

            path_exists, directory = is_exists(name)

        with open('path.txt', 'w') as f:
            f.write(directory)
        return directory


def get_all_file_paths(directory):
    file_paths = []

    # 把所有的文件夹以及子文件夹、以及文件全部搞出来
    for root, directories, files in os.walk(directory):
        for filename in files:
            # 得到完全路径
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    return file_paths


def main(directory):
    today = datetime.date.today().strftime('%y%m%d')

    file_paths = get_all_file_paths(directory)

    print('Following files will be zipped:')
    for file_name in file_paths:
        print(file_name)

    with ZipFile('{}_{}.zip'.format(directory, today), 'w') as zip:
        for file in file_paths:
            zip.write(file)

    print('All files zipped successfully!')
    time.sleep(2)
    return None


if __name__ == '__main__':
    directory = save_path()
    main(directory)
