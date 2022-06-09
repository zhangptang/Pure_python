# -*-coding:utf-8-*-
import collections
import heapq
import itertools


def sort_heaped():
    """堆排序"""
    list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
    list2 = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    print(heapq.nlargest(3, list1))
    print(heapq.nsmallest(3, list1))
    print(heapq.nlargest(3, list2, key=lambda x: x['price']))
    print(heapq.nsmallest(3, list2, key=lambda x: x['price']))
    print(heapq.nsmallest(1, list2, key=lambda x: x['shares']))


def itertools_test():
    """迭代工具"""
    # 产生ABCD的全排列
    perm = itertools.permutations('ABCD')
    for _ in perm.__iter__():
        print(perm.__next__())
    # 产生ABCDE的五选三组合
    select1 = itertools.combinations('ABCDE', 3)
    for _ in select1.__iter__():
        print(select1.__next__())


def collections_test():
    ball = collections.namedtuple('ball', ['color', 'func'])
    b = ball('red', 'go')
    print(b)
    print(type(b))
    print(b[1])
    # counter
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
        'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
        'look', 'into', 'my', 'eyes', "you're", 'under'
    ]
    counter = collections.Counter(words)
    print(counter.most_common(3))


def main():
    # sort_heaped()
    # itertools_test()
    collections_test()


if __name__ == '__main__':
    main()
