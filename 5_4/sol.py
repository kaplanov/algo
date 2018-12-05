import sys

def read_array(inp):
    n, m = list(map(int, inp.readline().split()))
    lines = [tuple(map(int, inp.readline().split())) for i in range(n)]
    # print(lines)
    # beg = list(map(int, inp.readline().split()))
    # end = list(map(int, inp.readline().split()))
    points = list(map(int, inp.readline().split()))
    return lines, points


if __name__ == '__main__':
    inp = open('1', 'r')
    # inp = sys.stdin

    lines, points = read_array(inp)
    p_cp = list(points)

    print(lines)
    print(points)
    res = {}
    quick_lines(points, lines, 0, len(points) - 1, 0, len(lines) - 1, res)

    # print('results')
    # print(points)
    # print(res)
    # print(p_cp)
    print(' '.join(map(str, [res[p] for p in p_cp])))

