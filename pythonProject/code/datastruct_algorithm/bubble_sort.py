# -*-coding:utf-8-*-


def bubble_basci(list1, comp=lambda x, y: x > y):
    """
    冒泡排序
    从前开始，相邻的两个元素进行比对，谁大谁往后移动，两者交换位置，多次
    交换后，排序完成
    """
    list1 = list1[:]
    for i in range(len(list1) - 1):
        swapped = False
        for j in range(len(list1) - 1 - i):
            if comp(list1[j], list1[j + 1]):
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
                swapped = True
        if not swapped:
            break;
    return list1


def Bubble_upgrade_sort(list1, comp=lambda x, y: x > y):
    """
    搅拌排序（冒泡排序升级版）
    在冒泡排序的基础上增加了每一次排序完以后，在反向进行一次逆向的比较，将最小的放到最前面
    从而在冒泡排序的基础上减少了最外层循环的次数
    :param list1:
    :param comp:
    :return:
    """
    list1 = list1[:]
    for i in range(len(list1) - 1):
        swapped = False
        for j in range(len(list1) - 1 - i):
            if comp(list1[j], list1[j + 1]):
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
                swapped = True
        # 逆向交换
        if swapped:
            swapped = False
            for j in range(len(list1) - 2 - i, i, -1):
                if comp(list1[j - 1], list1[j]):
                    list1[j - 1], list1[j] = list1[j], list1[j - 1]
                    swapped = True
        if not swapped:
            break
    return list1


def main():
    list1 = [12, 3, 35, 20, 56, 90, 8, 70, 100, 68]
    list2 = bubble_basci(list1)
    print(list2)
    # 可以打印每一趟的打印结果，看一下前后的比较次数
    print('---------------- 搅拌排序-----------')
    list2 = Bubble_upgrade_sort(list1)
    print(list2)


if __name__ == '__main__':
    main()
