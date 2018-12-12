import bisect


def read_array(inp):
    n, m = list(map(int, inp.readline().split()))
    lines = [tuple(map(int, inp.readline().split())) for i in range(n)]
    points = list(map(int, inp.readline().split()))
    return lines, points


def calc_lines(points, lines):
    begs = [l[0] for l in lines]
    ends = [l[1] for l in lines]

    sb = sorted(begs)
    se = sorted(ends)

    res = [(bisect.bisect_left(sb, p+1), bisect.bisect_left(se, p)) for p in points]

    return [max(0, d[0] - d[1]) for d in res]


if __name__ == '__main__':
    inp = open('1', 'r')

    lines, points = read_array(inp)
    p_cp = list(points)

    print(' '.join(map(str, calc_lines(points, lines))) )
