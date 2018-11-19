import sys


def read(inp):
    res = []
    n, v = map(int, inp.readline().split())
    for i in range(n):
        x, y = map(int, inp.readline().split())
        res.append((x, y))

    return v, res


def solve(v, items):
    res = 0
    rem_v = v

    for item in items:
        if rem_v > item[1]:
            res += item[0]
            rem_v -= item[1]
        else:
            res += item[0] * (rem_v/item[1])
            break

    return res


if __name__ == '__main__':
    inp = open('1', 'r')
    # inp = sys.stdin

    v, items = read(inp)
    s_items = sorted(items, key=lambda i: i[0]/i[1], reverse=True)
    res = solve(v, s_items)

    print(res)
