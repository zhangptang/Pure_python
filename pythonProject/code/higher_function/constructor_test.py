# -*-coding:utf-8-*-
"""
生成式
"""


def fib(num):
    """斐波拉契数列"""
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a


def acal_avg():
    """
    流式计算平均值
    生成器对象可以使用send()方法发送数据，发送的数据会成为生成器函数中通过yield表达式获得的值。
    这样，生成器就可以作为协程使用，协程简单的说就是可以相互协作的子程序
    :return:
    """
    total, counter = 0, 0
    avg_value = None
    while True:
        value = yield avg_value
        total, counter = total + value, counter + 1
        avg_value = total / counter


def main():
    fib1 = fib(10)
    for num in fib1:
        print(num, end=',')

    gener1 = acal_avg()
    next(gener1)
    print("")
    print(gener1.send(30))
    print(gener1.send(40))
    print(gener1.send(50))


if __name__ == '__main__':
    main()
