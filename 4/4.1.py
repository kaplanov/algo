import string
import sys


def read(inp):
    res = []
    n = int(inp.readline())
    for i in range(n):
        x, y = map(int, inp.readline().split())
        res.append((x, y))

    return res


if __name__ == '__main__':
    inp = open('1', 'r')
    # input = sys.stdin

    lines = read(inp)

    print(lines)
