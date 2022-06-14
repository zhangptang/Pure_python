# -*-coding:utf-8-*-


def select_sort(list1, comp=lambda x, y: x < y):
    """
    选择排序
    从前开始，将第一个值设置为最小值，让后将这个值与后面的值进行比较，如果后面的列表中出现比设定的最小值还要小，就将
    找到的那个值重新设置为最小值，然后讲之前的值与新的最小值进行交换，然后依次进行比对交换
    :param list1:
    :param comp:
    :return:
    """
    list1 = list1[:]
    for i in range(len(list1) - 1):
        index_min = i
        for j in range(i + 1, len(list1)):
            if comp(list1[j], list1[index_min]):
                index_min = j
        list1[index_min], list1[i] = list1[i], list1[index_min]
    return list1


def main():
    list1 = [12, 3, 35, 20, 56, 90, 8, 70, 100, 68]
    list2 = select_sort(list1)
    print(list2)


if __name__ == '__main__':
    main()
