# 一个函数中一旦有了yield语句,当成生成器使用
def f1():
    for i in  range(2):
        yield i

g =f1()
while True:
    try:
        print(g.__next__())
    except Exception as e:
        break