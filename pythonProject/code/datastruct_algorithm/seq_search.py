# -*-coding:utf-8-*-


def seq_search(list1, target):
    """顺序查找"""
    for index, item in enumerate(list1):
        if item == target:
            return index
    return -1


def bin_search(list1, target):
    """折半查找"""
    start, end = 0, len(list1) - 1
    i = 0
    while start <= end:
        mid = (start + end) // 2
        i = i + 1
        print(f'第{i}趟')
        print(f'{mid}')
        if target < list1[mid]:
            end = mid - 1
        elif target > list1[mid]:
            start = mid + 1
        else:
            return mid
    return -1


def main():
    list1 = [12, 3, 35, 20, 56, 90, 8, 70, 100, 68]
    print(seq_search(list1, 100))
    print("----折半查找------")
    # 折半查找一般是在排序完以后进行，要不然会出现查询不到的情况
    print(bin_search(list1, 100))
    print(9 // 2)


if __name__ == '__main__':
    main()
