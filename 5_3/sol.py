import sys


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


def quick(arr, beg, end):
    pivot = beg
    i = j = beg+1
    while j <= end and i <= end:
        if arr[j] <= arr[pivot]:
            swap(arr, i, j)
            i += 1
            if j <= i:
                j = i + 1
        else:
            j += 1
    new_pivot = i-1
    swap(arr, pivot, new_pivot)

    quick(arr, beg, new_pivot-1)
    quick(arr, new_pivot+1, end)


if __name__ == '__main__':
    inp = open('2', 'r')
    # inp = sys.stdin

    lines, points = read_array(inp)

    print(lines)
    print(points)
    quick(points, 0, len(points) - 1)
    print(points)

