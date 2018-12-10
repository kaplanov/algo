from points.sol import vertical_split, min_distance, min_border

if __name__ == '__main__':
    assert vertical_split([]) == 0
    assert vertical_split([3]) == 3
    assert vertical_split([0, 1]) == 0.5

    assert min_border([[]])


    assert min_distance([]) == float('inf')
    assert min_distance([(0, 0)]) == float('inf')
    assert min_distance([(0, 0), (1, 1)]) == 1
