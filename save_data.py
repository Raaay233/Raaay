from zipfile import ZipFile
import os
import datetime
import time


def save_path():
    try:
        with open('path.txt', 'r') as f:
            directory = f.read()
        return directory

    except Exception:
        name = input('Please input the name which you want to zip:\n')
        directory = r'.\{}'.format(name)

        isExists = os.path.exists(directory.strip())
        while name is None or not isExists:
            print('The path IS NOT available! Please input the right name!')
            name = input()
            directory = r'.\{}'.format(name)
            isExists = os.path.exists(directory.strip())

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
