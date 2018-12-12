import sys


def read_array(inp):
    w, n = map(int, inp.readline().split())
    arr = list(map(int, inp.readline().split()))
    return w, arr


def knapsack(w, gold):
    d = [[0 for j in range(w+1)] for i in gold]
    for i in range(0, len(gold)):
        for wj in range(1, w+1):
            d[i][wj] = d[i-1][wj]
            gw = gold[i]
            if gw <= wj:
                d[i][wj] = max(d[i][wj], d[i-1][wj-gw] + gw)
    return max(max(row) for row in d)


if __name__ == '__main__':
    inp = open('2', 'r')
    # inp = sys.stdin

    w, arr = read_array(inp)
    print(knapsack(w, arr))
