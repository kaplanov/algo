import sys
from random import randint


def read_array(inp):
    n, m = list(map(int, inp.readline().split()))
    beg = list(map(int, inp.readline().split()))
    end = list(map(int, inp.readline().split()))
    points = list(map(int, inp.readline().split()))
    return list(zip(beg, end)), points


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def quick_lines(point_list, line_list, beg, end, beg_lines, end_lines, res_dict):
    if beg >= end:
        res_dict[point_list[end]] = end
        return

    new_pivot = partition(beg, end, point_list)

    cnt, line_piv_1, line_piv_2 = partition_lines(beg_lines, end_lines, point_list[new_pivot], line_list)
    res_dict[point_list[new_pivot]] = new_pivot

    quick_lines(point_list, line_list, beg, new_pivot - 1, beg_lines, line_piv_1 - 1, res_dict)
    quick_lines(point_list, line_list, new_pivot + 1, end, line_piv_2 + 1, end_lines, res_dict)


def partition_lines(beg, end, point, line_list):
    line_cnt = 0
    pivot1 = 0
    pivot2 = 0
    i = j = k = 0
    while i <= end and j <= end and k <= end:
        line = line_list[k]
        if line[1] < point:
            swap(line_list, i, k)
            i += 1
            if j < i:
                j = i
            if k < i:
                k = i
        elif line[0] <= point <= line[1]:
            swap(line_list, j, k)
            j += 1
            if j < i:
                j = i
            if k < i:
                k = i



    return line_cnt, pivot1, pivot2


def partition(beg, end, point_list):
    pivot = beg
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
    inp = open('2', 'r')
    # inp = sys.stdin

    lines, points = read_array(inp)
    p_cp = list(points)

    print(lines)
    print(points)
    res = {}
    quick_lines(points, lines, 0, len(points) - 1, 0, len(points) - 1, res)

    print('results')
    print(points)
    print(res)
    print(p_cp)
    print(' '.join(map(str, [res[p] for p in p_cp])))

