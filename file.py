import zipfile
import re
import os
import sys


# 生成资源文件目录访问路径
def resource_path(relative_path):
    if getattr(sys, 'frozen', False):  # 是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def remove_dir(dir):
    dir = dir.replace('\\', '/')
    if os.path.isdir(dir):
        for p in os.listdir(dir):
            remove_dir(os.path.join(dir, p))
        if os.path.exists(dir):
            os.rmdir(dir)
    else:
        if os.path.exists(dir):
            os.remove(dir)


def unlock_pptx(file_path="test.pptx"):
    file_data = ""
    re_rule = re.compile(r'<p:modify.*?/>')

    with zipfile.ZipFile(file_path) as azip:
        azip.extractall('tmp/')

    with open('tmp/ppt/presentation.xml', "r", encoding="utf-8") as f:
        for line in f:
            # print(line)
            line = re.sub(re_rule, '', str(line))
            file_data += line
        # print(file_data)
    with open('tmp/ppt/presentation.xml', "w", encoding="utf-8") as f:
        f.write(file_data)

    with zipfile.ZipFile(file_path, 'w') as azip:
        for current_path, sub_folders, files_name in os.walk('tmp/'):
            # print(current_path, sub_folders, files_name)
            # files_name是一个列表，我们需要里面的每个文件名和当前路径组合
            for file in files_name:
                # 将当前路径与当前路径下的文件名组合，就是当前文件的绝对路径
                azip.write(os.path.join(current_path, file), os.path.join(current_path, file).replace("tmp/", ""))

    remove_dir("tmp")
