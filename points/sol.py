import math


def read_array(inp):
    n = int(inp.readline())
    points = [tuple(map(int, inp.readline().split())) for _ in range(n)]

    return points


def partition(points):
    m = len(points) // 2
    return points[:m], points[m:], points[m][0]


def min_border(points, v, distance):
    if math.isinf(distance):
        return math.inf
    border_points = sorted([p for p in points if abs(p[0] - v) <= distance], key=lambda p: p[1])

    res = []
    for i in range(len(border_points)):
        current_point = border_points[i]
        next_max_6_points = [border_points[i + shift] for shift in range(1, min(len(border_points) - i, 6))]
        dists = [distance] + [calc_dist(current_point, pt) for pt in next_max_6_points]

        res.append(min(dists))

    return min(res)


def min_distance(points):
    if len(points) <= 1:
        return math.inf
    if len(points) == 2:
        return calc_dist(points[0], points[1])

    lp, rp, v = partition(points)

    min_left = min_distance(lp)
    min_right = min_distance(rp)
    min_b = min_border(points, v, min(min_left, min_right))

    return min(min_b, min_left, min_right)


def calc_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


if __name__ == '__main__':
    inp = open('2', 'r')

    points = read_array(inp)
    p_sorted = sorted(points, key=lambda p: p[0])
    print(p_sorted)

    print(min_distance(p_sorted))



