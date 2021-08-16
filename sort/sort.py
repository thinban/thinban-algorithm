def bubble_sort(list):
    length = len(list)
    for index in range(length):
        # 标志位（减少循环次数）
        flag = True
        # 【把大的数冒泡到数组尾部】
        for j in range(1, length - index):
            if list[j - 1] > list[j]:
                list[j - 1], list[j] = list[j], list[j - 1]
                flag = False
        if flag:
            # 没有发生交换，直接返回list
            return list
    return list


def selection_sort(list):
    n = len(list)
    for i in range(0, n):
        min = i
        # 【[i+1,n)中找到最小的值，与 list[i]替换】
        for j in range(i+1, n):
            if list[j] < list[min]:
                min = j
                list[min], list[i] = list[i], list[min]
    return list


def insert_sort(list):
    n = len(list)
    for i in range(1, n):
        if list[i] < list[i - 1]:
            # 找到第一个小于前面的数
            temp = list[i]
            index = i
            # [0,i-1]为已排序部分，从后往前“挤”走比list[i]大的数
            for j in range(i - 1, -1, -1):
                if list[j] > temp:
                    list[j + 1] = list[j]
                    index = j
                else:
                    break
            list[index] = temp
    return list


def shell_sort(list):
    n = len(list)
    # 初始步长
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            # 每个步长进行插入排序
            temp = list[i]
            j = i
            # 插入排序
            while j >= gap and list[j - gap] > temp:
                list[j] = list[j - gap]
                j -= gap
            list[j] = temp
        # 得到新的步长
        gap = gap // 2
    return list


def merge_sort(list):
    # 合并排序
    if len(list) <= 1:
        return list
    middle = len(list) // 2
    left = merge_sort(list[:middle])
    right = merge_sort(list[middle:])
    return merge_sort_merge(left, right)


def merge_sort_merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
        reslut += left[l:]
        result += right[r:]
    return result


def qsort(arr):
    # 快排：分治法
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x < pivot]
        greater = [x for x in arr[1:] if x >= pivot]
        return qsort(less) + [pivot] + qsort(greater)


def heap_sort(list):
    # 创建最大堆
    for start in range((len(list) - 2) // 2, -1, -1):
        heap_sort_sift_down(list, start, len(list) - 1)

    # 堆排序
    for end in range(len(list) - 1, 0, -1):
        list[0], list[end] = list[end], list[0]
        heap_sort_sift_down(list, 0, end - 1)
    return list


def heap_sort_sift_down(lst, start, end):
    # 最大堆调整
    root = start
    while True:
        child = 2 * root + 1
        if child > end:
            break
        if child + 1 <= end and lst[child] < lst[child + 1]:
            child += 1
        if lst[root] < lst[child]:
            lst[root], lst[child] = lst[child], lst[root]
            root = child
        else:
            break


def count_sort(list):
    # 计数排序
    min = 2147483647
    max = 0
    # 取得最大值和最小值
    for x in list:
        if x < min:
            min = x
        if x > max:
            max = x
    # 创建数组C
    count = [0] * (max - min + 1)
    for index in list:
        count[index - min] += 1
    index = 0
    # [1,1,2,1,0,0,0,0,1],range(0)不发生遍历
    print(count)
    # 填值
    for a in range(max - min+1):
        for c in range(count[a]):
            list[index] = a + min
            index += 1
    return list


if __name__ == '__main__':
    # https://www.cnblogs.com/huang-yc/p/9774287.html
    list = [1, 3, 4, 9, 2, 3]
    # print(bubble_sort(list))
    print(count_sort(list))
