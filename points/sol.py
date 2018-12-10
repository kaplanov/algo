import sys
import math


def read_array(inp):
    n = int(inp.readline())
    points = [tuple(map(int, inp.readline().split())) for _ in range(n)]

    return points


def vertical_split(x):
    if len(x) == 0:
        return 0
    elif len(x) == 1:
        return x[0]
    else:
        median = len(x) // 2
        odd = len(x) % 2
        if odd:
            return x[median]
        else:
            return (x[median] + x[median - 1]) / 2


def partition(points, v):
    l, r = [], []
    for p in points:
        if p[0] < v:
            l.append(p)
        else:
            r.append(p)
    return l, r


def min_border(point, v, d):
    border_p = sorted([p for p in points if math.abs(p[0] - v) <= d], key=lambda p: p[1])

    return float('inf')


def min_distance(points):
    if len(points) <= 1:
        return float('inf')
    if len(points) == 2:
        return dist(points[0], points[1])
    xs = sorted(x[0] for x in points)
    v = vertical_split(xs)
    lp, rp = partition(points, v)

    min_left = min_distance(lp)
    min_right = min_distance(rp)
    min_b = min_border(points, v, min(min_left, min_right))

    return min(min_b, min_left, min_right)


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p2[0] - p2[1])**2)


if __name__ == '__main__':
    inp = open('1', 'r')
    # inp = sys.stdin

    points = read_array(inp)
    x = sorted(x[0] for x in points)
    print(points)

    print(min_distance(points))



