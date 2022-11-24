import re


def get_stop_words():
    file_object = open("data/badlinks.txt")
    stop_words = []
    for line in file_object.readlines():
        line = line[:-1]
        line = line.strip()
        stop_words.append(line)
    return stop_words


def get_links():
    file_object = open("data/waitlinks.txt")
    links = []
    for line in file_object.readlines():
        line = line[:-1]
        line = line.strip()
        links.append(line)
    return links


def get_items():
    file_object = open("data/metadata_items.txt")
    items = []
    for line in file_object.readlines():
        line = line[:-1]
        line = line.strip()
        p = line.split("-")
        if len(p) > 2:
            line = p[0] + "-" + p[1]
            items.append(line)
    return items


def add_dash(args, num):
    if args[num].isdigit():
        if args[:num].isalpha():
            args = args[:num] + '-' + args[num:]
    return args


def load_data():
    links = get_links()
    items = get_items()
    stop_words = get_stop_words()  # 加载停用词表
    print(stop_words)
    finals = {}
    lists = []
    for l in links:
        p = l.split("=")[2]
        # 分离其他内容
        p = p.split(" ")[0]
        # 字母转大写 移除无用词
        for w in stop_words:
            p = p.upper().replace(w.upper(), '')
        # 把 00 替换 -
        number = re.findall("\d+", p)
        # 如果是00123的换成-123

        if len(number[0]) > 4:
            p = p.replace("00", '-')
        # 给没有-分隔的添加分隔
        if len(re.findall("-", p)) > 1:
            p = p[1:]
        p = add_dash(p, 2)
        p = add_dash(p, 3)
        p = add_dash(p, 4)
        # print(p)
        if p not in items:
            finals[p] = l
    for i in sorted(finals):
        lists.append(finals[i])
    with open("result/download.txt", mode='a') as f:
        for item in lists:
            f.write(item + "\n")


def main():
    load_data()


main()
