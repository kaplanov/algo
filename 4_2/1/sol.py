import sys
import heapq
from collections import Counter, namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc+"0")
        self.right.walk(code, acc+"1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def read(inp):
    s = inp.readline()
    return s


def huffman(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    # h = [(freq, Leaf(ch)) for ch, freq in Counter(s).items()]
    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        freq1, _c1, left = heapq.heappop(h)
        freq2, _c2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if h:
        [(_freq, _, root)] = h
        root.walk(code, "")
    return code


def encode(string, code):
    return ''.join(code[c] for c in string)


if __name__ == '__main__':
    inp = open('1', 'r')
    # inp = sys.stdin

    n = read(inp)

    codes = huffman(n)
    res = encode(n, codes)

    print(len(codes), len(res))
    for c in sorted(codes):
        print(f'{c}: {codes[c]}')
    print(res)
