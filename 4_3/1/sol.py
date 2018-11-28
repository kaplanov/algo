import sys
import math


class PQueue:
    def __init__(self):
        self.q = []

    def insert(self, n):
        idx = len(self.q)
        self.q.append(n)
        self._sift_up(idx)

    def extract_max(self):
        max_value = self.q[0]
        last_idx = len(self.q)-1
        self._swap(last_idx, 0)
        self.q.pop(last_idx)
        self._sift_down(0)
        return max_value

    def _sift_up(self, idx):
        el = self.q[idx]
        parent_idx = int(math.ceil((idx - 1) / 2))
        parent = self.q[parent_idx]
        if parent < el:
            self._swap(idx, parent_idx)
            self._sift_up(parent_idx)

    def _sift_down(self, idx):
        if len(self.q) == 0:
            return
        el = self.q[idx]
        child_idx_1 = min((idx * 2) + 1, len(self.q) - 1)
        child_idx_2 = min((idx * 2) + 2, len(self.q) - 1)
        if el < self.q[child_idx_1] and el < self.q[child_idx_2]:
            min_idx = child_idx_1 if self.q[child_idx_1] > self.q[child_idx_2] else child_idx_2
            self._swap(idx, min_idx)
            self._sift_down(min_idx)
        elif el < self.q[child_idx_1]:
            self._swap(idx, child_idx_1)
            self._sift_down(child_idx_1)
        elif el < self.q[child_idx_2]:
            self._swap(idx, child_idx_2)
            self._sift_down(child_idx_2)

    def _swap(self, idx1, idx2):
        temp = self.q[idx1]
        self.q[idx1] = self.q[idx2]
        self.q[idx2] = temp

    def __repr__(self):
        return str(self.q)


def read(inp):
    n = int(inp.readline())
    com = (tuple(line.split()) for line in inp)

    return com


if __name__ == '__main__':
    inp = open('3', 'r')
    # inp = sys.stdin

    heap = PQueue()
    commands = read(inp)
    for comm in commands:
        if comm[0] == 'Insert':
            heap.insert(int(comm[1]))
        elif comm[0] == 'ExtractMax':
            print(heap.extract_max())
        else:
            print('command was skipped')
