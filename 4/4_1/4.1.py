import sys


def read(inp):
    res = []
    n = int(inp.readline())
    for i in range(n):
        x, y = map(int, inp.readline().split())
        res.append((x, y))

    return res


def solve(lines):
    res = []
    covered = {}
    for l in lines:
        if l in covered:
            continue
        else:
            new_point = l[1]
            res.append(new_point)
            for l in lines:
                if l[0] <= new_point and new_point <= l[1]:
                    covered[l] = True

    return res


if __name__ == '__main__':
    inp = open('4_1/3', 'r')
    # inp = sys.stdin

    lines = read(inp)
    s_lines = sorted(lines, key=lambda l: l[1])
    res = solve(s_lines)

    print(len(res))
    print(' '.join(map(str, res)))
