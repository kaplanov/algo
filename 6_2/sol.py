import sys


def read_array(inp):
    n = int(inp.readline())
    arr = list(map(int, inp.readline().split()))
    return arr


def lds(arr):
    d = [1 for i in range(len(arr))]
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] % arr[j] == 0 and d[j] + 1 > d[i]:
                d[i] = d[j] + 1

    return max(d)


if __name__ == '__main__':
    inp = open('1', 'r')
    # inp = sys.stdin

    arr = read_array(inp)
    print(lds(arr))
