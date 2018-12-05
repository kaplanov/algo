import sys
from random import randint


def read_array(inp):
    n, m = list(map(int, inp.readline().split()))
    lines = [tuple(map(int, inp.readline().split())) for i in range(n)]
    # print(lines)
    # beg = list(map(int, inp.readline().split()))
    # end = list(map(int, inp.readline().split()))
    points = list(map(int, inp.readline().split()))
    return lines, points


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def quick_lines(point_list, line_list, beg, end, beg_lines, end_lines, res_dict):
    if beg >= end:
        point = point_list[end]
        cnt, line_piv_1, line_piv_2 = partition_lines(0, len(line_list) - 1, point, line_list)
        res_dict[point] = cnt
        return

    new_pivot = partition(beg, end, point_list)

    # cnt, line_piv_1, line_piv_2 = partition_lines(beg_lines, end_lines, point_list[new_pivot], line_list)
    cnt, line_piv_1, line_piv_2 = partition_lines(0, len(line_list)-1, point_list[new_pivot], line_list)
    res_dict[point_list[new_pivot]] = cnt

    quick_lines(point_list, line_list, beg, new_pivot - 1, beg_lines, line_piv_2 - 1, res_dict)
    quick_lines(point_list, line_list, new_pivot + 1, end, line_piv_1, end_lines, res_dict)


def partition_lines(beg, end, point, line_list):
    if beg > end:
        return 0, 0, 0
    if beg == end == 0:
        return 1 if line_list[0][0] <= point <= line_list[0][1] else 0, 0, 0
    i = j = k = beg
    while i <= end and j <= end and k <= end:
        line = line_list[k]
        if line[1] < point:
            swap(line_list, i, k)
            i += 1
            if j < i:
                j = i
            if k < i:
                k = i
        if k > end:
            continue
        line2 = line_list[k]
        if line2[0] <= point <= line2[1]:
            swap(line_list, j, k)
            j += 1
            if k < j:
                k = j
        if k > end:
            continue
        line3 = line_list[k]
        if line3[0] > point:
            k += 1

    return j - i, i, j


def partition(beg, end, point_list):
    pivot = beg
    # randomly choose pivot
    swap(point_list, pivot, randint(beg, end))

    i = j = beg + 1
    while j <= end and i <= end:
        if point_list[j] <= point_list[pivot]:
            swap(point_list, i, j)
            i += 1
            if j <= i:
                j = i
        else:
            j += 1
    new_pivot = i - 1
    swap(point_list, pivot, new_pivot)
    return new_pivot


if __name__ == '__main__':
    inp = open('1', 'r')
    # inp = sys.stdin

    lines, points = read_array(inp)
    p_cp = list(points)

    # print(lines)
    # print(points)
    res = {}
    quick_lines(points, lines, 0, len(points) - 1, 0, len(lines) - 1, res)

    # print('results')
    # print(points)
    # print(res)
    # print(p_cp)
    print(' '.join(map(str, [res[p] for p in p_cp])))

