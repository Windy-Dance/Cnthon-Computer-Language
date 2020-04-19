# coding : utf-8
# Author : Parallel
# Create On
import os

__all_change__ = ["唠嗑", "找茬", "轮回", "抄家", "降维", "升维",
                  "踢出", "找来", "打开", "执行", "虚无", "并且",
                  "一旦", "不然", "否则", "干掉", "遛", "就是",
                  "或者", "尝试", "错执", "从", "跳过", "匿名",
                  "正确", "错误", "跳出", "自个", "比作",
                  "当", "定义", "生成", "不是", "在", "新类",
                  ]
__all_bring__ = ["print", "input", "range", "len", "int", "str",
                 "return", "import", "open", "exec", "None", "and",
                 "if", "elif", "else", "del", "for", "is",
                 "or", "try", "except", "from", "continue", "lambda",
                 "True", "False", "break", "self", "as",
                 "while", "def", "yield", "not", "in",
                 "class",
                 ]
p = ""


def __exec__(program=""):
    for i in range(len(__all_change__)):
        program = program.replace(__all_change__[i], __all_bring__[i])
    exec(program)


def openfile(name):
    global p
    with open(name.replace('"', ''), "r+", encoding="utf-8") as f:
        p = f.read()
        f.close()


def bring():
    you = str(input("请输入你要编译的cn脚本文件路径,exit退出:"))
    if you == 'exit':
        print("退出...")
        exit("退出...")
    else:
        try:
            openfile(you)
            __exec__(p)
        except:
            print("出错")
            bring()


if __name__ == '__main__':
    while True:
        bring()
