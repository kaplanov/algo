import sys


def read_array(inp):
    n = int(inp.readline())
    line = list(map(int, inp.readline().split()))
    return line


def merge(a1, a2):
    li, ri = 0, 0
    res = []
    swap_count = 0
    # if len(a1) == 0 or len(a2) == 0:
    #     return a1 + a2
    while li < len(a1) and ri < len(a2):
        if a1[li] <= a2[ri]:
            res.append(a1[li])
            li += 1
        else:
            res.append(a2[ri])
            ri += 1
            swap_count += len(a1) - li

    res += a1[li:]
    res += a2[ri:]

    return res, swap_count


def merge_sort_count(arr, l, r):
    if l >= r:
        return arr[l:r+1], 0
    m = (l + r) // 2
    left, l_count = merge_sort_count(arr, l, m)
    right, r_count = merge_sort_count(arr, m+1, r)
    res, cnt = merge(left, right)
    return res, cnt+l_count + r_count


if __name__ == '__main__':
    inp = open('1', 'r')
    # inp = sys.stdin

    arr = read_array(inp)
    s_arr, cnt = merge_sort_count(arr, 0, len(arr)-1)

    print(cnt)
    print(s_arr)


