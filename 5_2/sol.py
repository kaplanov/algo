import sys
from functools import reduce

def read_array(inp):
    n = int(inp.readline())
    line = list(map(int, inp.readline().split()))
    return line


def merge(a1, a2):
    li, ri = 0, 0
    res = []
    if len(a1) == 0 or len(a2) == 0:
        return a1 + a2
    while li < len(a1)-1 or ri < len(a2)-1:
        if a1[li] < a2[ri]:
            res.append(a1[li])
            li += 1
        else:
            res.append(a2[ri])
            ri += 1
    # if li < len(a1) - 1:
    res.append(a1[li:])
    res.append(a2[ri:])

    return res


def merge_sort_count(arr, l, r):
    count = 0
    if l >= r:
        return arr[l:r+1]
    m = (l + r) // 2
    return merge(merge_sort_count(arr, l, m), merge_sort_count(arr, m+1, r))


if __name__ == '__main__':
    inp = open('1', 'r')
    # inp = sys.stdin

    arr = read_array(inp)
    s_arr = merge_sort_count(arr, 0, len(arr)-1)
    # idx = [find_first_idx(el, s_arr) for el in arr]
    # res = [max(0, pos - idx) for idx, pos in enumerate(idx)]

    print(arr)
    print(s_arr)


