def bin_search(el, array, left, right):
    if left >= right:
        return -1
    m = (left + right) // 2
    if el == array[m]:
        return m


    if el < array[m]:
        return bin_search(el, array, left, m-1)
    else:
        return bin_search(el, array, m+1, right)


if __name__ == '__main__':
    assert -1 == bin_search(1, [], 0, 0)
    assert 1 == bin_search(1, [0, 1, 2], 0, 2)
    assert -1 == bin_search(4, [0, 1, 2], 0, 2)