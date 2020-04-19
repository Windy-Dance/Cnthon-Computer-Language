# coding : utf-8
#Author : Parallel
#Create On  
__all_change__ = ["唠嗑", "找茬", "轮回", "抄家", "降维", "升维",
                  "踢出", "找来", "打开", "执行", "虚无", "并且",
                  "一旦", "不然", "否则", "干掉", "遛", "就是",
                  "或者", "尝试", "错执", "从", "跳过", "匿名",
                  "正确", "错误", "跳出","自个",
                  "当", "定义", "生成", "不是", "在", "新类",
                  ]
__all_bring__ = ["print", "input", "range", "len", "int", "str",
                 "return", "import", "open", "exec", "None", "and",
                 "if", "elif", "else", "del", "for", "is",
                 "or", "try", "except", "from", "continue", "lambda",
                 "True", "False", "break","self",
                 "while", "def", "yield", "not", "in",
                 "class",
                 ]
print("""
Cnthon 0.1.2,easy,unfast,great fun,and good for Chinese.
The Cnthon Computer Language by Parallel and Python.
Thank for Guido,It can let me create the Boring Language.
It's easy to use,if you used Python.
Look "README.md" to find help
    """)
while True:
    you = str(input(">>"))
    if you == "exit":
        exit("Exit Cnthon")
    try:
        for i in range(len(__all_change__)):
            you = you.replace(__all_change__[i],__all_bring__[i])
        exec(you)
    except:
        raise SyntaxError("I don't know why,but Your code is wrong...")
