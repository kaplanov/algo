import sys


def read(inp):
    n = int(inp.readline())

    return n


def solve(n):
    numbers = set()
    rem_n = n

    for i in range(1, n+1):
        if (rem_n-i) not in numbers and (rem_n-i) != i:
            if i not in numbers:
                numbers.add(i)
                rem_n -= i
                if rem_n == 0:
                    break
        else:
            numbers.add(rem_n)
            break

    return len(numbers), numbers


if __name__ == '__main__':
    inp = open('1', 'r')
    # inp = sys.stdin

    n = read(inp)

    cnt, numbers = solve(n)

    print(cnt)
    print(' '.join(map(str, numbers)))
