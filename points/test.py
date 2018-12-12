import math
from points.sol import min_distance, min_border, partition


ps = [(0, 7), (0, 1), (0, 2), (0, 5), (0, 10), (0, 6), (0, 8), (0, 9), (0, 3), (0, 4)]

ps0 = []
ps1 = [(0, 1)]
ps2 = [(1, 1), (1, 1)]
ps3 = [(1, 0), (2, 0), (3, 0)]


if __name__ == '__main__':
    l, r, v = partition(ps0)
    assert len(l) == 0 and len(r) == 0 and math.isinf(v)

    l, r, v = partition(ps1)
    assert len(l) == 0 and len(r) == 1 and v == 0

    l, r, v = partition(ps2)
    assert len(l) == 1 and len(r) == 1 and v == 1

    l, r, v = partition(ps3)
    assert len(l) == 1 and len(r) == 2 and v == 2

    assert min_border(ps, 0, 2) == 1
    assert min_border(ps, 0, float('inf')) == float('inf')

    assert min_distance([]) == float('inf')
    assert min_distance([(0, 0)]) == float('inf')
    assert min_distance([(0, 0), (1, 1)]) == math.sqrt(2)
