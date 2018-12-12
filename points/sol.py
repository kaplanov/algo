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
            return x[median], median
        else:
            return (x[median] + x[median - 1]) / 2, median


def partition(points):
    if len(points) == 0:
        return [], [], math.inf
    elif len(points) == 1:
        return [], points, points[0][0]
    else:
        m = len(points) // 2
        return points[:m], points[m:], points[m][0]


def min_border(points, v, distance):
    if math.isinf(distance):
        return math.inf
    border_p = sorted([p for p in points if abs(p[0] - v) <= distance], key=lambda p: p[1])

    res = [distance]
    for i in range(len(border_p)):
        current_point = border_p[i]
        next_6_points = [border_p[i + shift] for shift in range(1, min(len(border_p) - i, 6))]
        dists = [dist(current_point, pt) for pt in next_6_points]
        dists.append(distance)
        res.append(min(dists))

    return min(res)


def min_distance(points):
    if len(points) <= 1:
        return math.inf
    if len(points) == 2:
        return dist(points[0], points[1])

    lp, rp, v = partition(points)

    min_left = min_distance(lp)
    min_right = min_distance(rp)
    min_b = min_border(points, v, min(min_left, min_right))

    return min(min_b, min_left, min_right)


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


if __name__ == '__main__':
    inp = open('3', 'r')
    # inp = sys.stdin

    points = read_array(inp)
    p_sorted = sorted(points, key=lambda p: p[0])
    print(p_sorted)

    print(min_distance(p_sorted))



