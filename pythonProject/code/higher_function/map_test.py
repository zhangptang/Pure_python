# -*-coding:utf-8-*-
from functools import wraps
from time import time


def record_time(func):
    """记录函数时间"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f'{func.__name__}: {time() - start}秒')
        return result

    return wrapper


def sum1(x, y, comp=lambda x, y: x + y):
    return comp(x, y)


def main():
    """
    filter(func, iter) 过滤
    map(func, iter) 会根据提供的函数对指定序列做映射
    :return:
    """
    list1 = [x ** 2 for x in range(1, 10) if x % 2 == 0]
    print(list1)
    list1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(1, 10))))
    print(list1)
    print(record_time(sum1(2, 4)))


if __name__ == '__main__':
    main()
