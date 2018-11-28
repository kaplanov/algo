import sys


def read_array(inp):
    line = list(map(int, inp.readline().split()))
    line.pop(0)
    return line


def bin_search(el, array, left, right):
    m = (left + right) // 2
    if el == array[m]:
        return m
    if left >= right:
        return -1

    if el < array[m]:
        return bin_search(el, array, left, m-1)
    else:
        return bin_search(el, array, m+1, right)


if __name__ == '__main__':
    inp = open('1', 'r')
    # inp = sys.stdin

    ar1 = read_array(inp)
    ar2 = read_array(inp)

    res = [bin_search(el, ar1, 0, len(ar1) - 1) for el in ar2]
    res_fin = [el+1 if el >= 0 else el for el in res]
    print(' '.join(map(str, res_fin)))
