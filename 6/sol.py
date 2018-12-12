import sys


def read_array(inp):
    n = int(inp.readline())
    arr = list(map(int, inp.readline().split()))
    return arr


if __name__ == '__main__':
    inp = open('1', 'r')
    # inp = sys.stdin

    arr = read_array(inp)
    print(arr)