from collections import Counter
import sys


def read(inp):
    s = inp.readline()

    return s


def huffman(s):
    symbols = Counter(s)

    return len(symbols), symbols


def encode(string, codes):
    return ''.join(str(bin(codes[c])[2:]) for c in string)


if __name__ == '__main__':
    inp = open('1', 'r')
    # inp = sys.stdin

    n = read(inp)

    cnt, codes = huffman(n)
    res = encode(n, codes)

    print(cnt)
    print(' '.join([f'{k}: {v}' for k, v in codes.items()]))
    print(res)
