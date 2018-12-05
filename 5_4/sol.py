import sys


def read_array(inp):
    n = int(inp.readline())
    arr = list(map(int, inp.readline().split()))
    return arr


if __name__ == '__main__':
    inp = open('1', 'r')
    # inp = sys.stdin

    arr = read_array(inp)
    print(arr)

    num_dict = {}
    for i in arr:
        if i in num_dict:
            num_dict[i] += 1
        else:
            num_dict[i] = 1
    print(num_dict)
    res = ''
    for i in sorted(num_dict.keys()):
        res += f'{i} ' * num_dict[i]
    print(res)

    #
    # print(lines)
    # print(points)
    # res = {}
    # quick_lines(points, lines, 0, len(points) - 1, 0, len(lines) - 1, res)
    #
    # # print('results')
    # # print(points)
    # # print(res)
    # # print(p_cp)
    # print(' '.join(map(str, [res[p] for p in p_cp])))

