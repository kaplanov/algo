import sys


def read(inp):
    code = {}
    n, l = map(int, inp.readline().split())
    for i in range(n):
        ch, enc = inp.readline().rstrip('\n').split(': ')
        code[enc] = ch
    s = inp.readline().rstrip('\n')
    return code, s


def decode(s, code):
    sym = 0
    buff = ''
    res = ''
    for ch in s:
        buff += ch
        if buff in code:
            res += code[buff]
            buff = ''

    return res


if __name__ == '__main__':
    inp = open('2', 'r')
    # inp = sys.stdin

    code, s = read(inp)
    res = decode(s, code)

    print(code)
    print(s)
    print(res)
