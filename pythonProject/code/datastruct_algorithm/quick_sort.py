# -*-coding:utf-8-*-


def _partition(list1, left, right, comp):
    base = list1[left]
    while left < right:
        # 从右往左移动，直到找到小于base的数据
        while left < right and list1[right] >= base:
            right -= 1
        list1[left] = list1[right]

        # 从左往右移动，直到找到大于base值
        while left < right and list1[left] <= base:
            left += 1
        list1[right] = list1[left]
    list1[left] = base
    return left


def quick_sort(list1, left, right, comp=lambda x, y: x <= y):
    """
    快速排序
    将列表分成俩个小列表，一边的值小于基准值，一边都大于基准值
    主要是如何找到基准值
    """
    # 永远都是左边的小于右边的，要不然会出现越界情况
    if left < right:
        base = _partition(list1, left, right, comp)
        quick_sort(list1, left, base - 1, comp)
        quick_sort(list1, base + 1, right, comp)


def main():
    list1 = [12, 3, 35, 20, 56, 90, 8, 70, 100, 68]
    quick_sort(list1, 0, len(list1) - 1)
    print(list1)


if __name__ == '__main__':
    main()
