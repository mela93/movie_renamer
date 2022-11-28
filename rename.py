import re
import os
import time

dir_path = "F:/temp/output/"


# 获取无用词
def get_stop_words():
    file_object = open("data/badwords.txt")
    stop_words = []
    for line in file_object.readlines():
        line = line[:-1]
        line = line.strip()
        stop_words.append(line)
    return stop_words


# 添加-分隔
def add_dash(args, num):
    if args[num].isdigit():
        if args[:num].isalpha():
            args = args[:num] + '-' + args[num:]
    return args


# 重命名文件
def rename_file(old, new):
    old_path = dir_path + old
    new_path = dir_path + new
    # 检查文件是否存在
    if not os.path.isfile(old_path):
        print("%s not exist!" % old_path)
    else:
        os.rename(old_path, new_path)
        # 输出结果方便检查
        print("%s ---> %s" % (old, new))


def load_data():
    index = 0
    t = str(time.time())
    print('加载数据中...')
    stop_words = get_stop_words()  # 加载停用词表
    # filenames = open("data/dev.txt")
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for i in filenames:
            # 如果是文件就跳过
            if not os.path.isfile(dir_path + i):
                continue
            # 计数器 记录当前处理的个数
            index = index + 1
            o = i
            # 分离文件后缀
            p = i.split(".")
            i = i.split(" ")[0]
            # 获取后缀名
            suffix = '.' + p[-1]
            # 移除后缀 方便后续处理
            i = i.replace(suffix, '')
            # 分离其他内容
            i = i.split(" ")[0]
            # 字母转大写 移除无用词
            for w in stop_words:
                i = i.upper().replace(w.upper(), '')
            # 把 00 替换 -
            number = re.findall("\d+", i)
            # 如果是00123的换成-123
            if len(number[0]) > 4:
                i = i.replace("00", '-')
            # 给没有-分隔的添加分隔
            i = add_dash(i, 2)
            i = add_dash(i, 3)
            i = add_dash(i, 4)
            # 拼接后缀
            with open("result/list" + t + ".txt", mode='a') as f:
                f.write(i)
            suffix = suffix.lower()
            i = i + suffix
            # 处理带C的情况
            i = i.replace("C" + suffix, '-C' + suffix)
            i = i.replace("_CH", '-C')
            # 重命名文件
            rename_file(o, i)
            with open("result/logs" + t + ".txt", mode='a') as f:
                f.write("%s ---> %s" % (o.strip(), i))
            # 暂停确认文件名是否有误
            if index % 5 == 0:
                c = input('确认继续?')
                if c == '':
                    print(111)
                else:
                    exit()


def main():
    load_data()


main()
