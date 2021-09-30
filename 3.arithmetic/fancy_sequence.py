MOD = 10 ** 9 + 7


class Fancy:
    def __init__(self):
        self.seq = []
        self.add = 0
        self.pow = 1

    def append(self, val: int) -> None:
        self.seq.append((val - self.add) * pow(self.pow, -1, MOD))

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % MOD

    def multAll(self, m: int) -> None:
        self.add = (self.add * m) % MOD
        self.pow = (self.pow * m) % MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        else:
            return int(((self.seq[idx] * self.pow + self.add) % MOD))


if __name__ == "__main__":
    operation = [
        "Fancy",
        "append",
        "append",
        "getIndex",
        "append",
        "getIndex",
        "addAll",
        "append",
        "getIndex",
        "getIndex",
        "append",
        "append",
        "getIndex",
        "append",
        "getIndex",
        "append",
        "getIndex",
        "append",
        "getIndex",
        "multAll",
        "addAll",
        "getIndex",
        "append",
        "addAll",
        "getIndex",
        "multAll",
        "getIndex",
        "multAll",
        "addAll",
        "addAll",
        "append",
        "multAll",
        "append",
        "append",
        "append",
        "multAll",
        "getIndex",
        "multAll",
        "multAll",
        "multAll",
        "getIndex",
        "addAll",
        "append",
        "multAll",
        "addAll",
        "addAll",
        "multAll",
        "addAll",
        "addAll",
        "append",
        "append",
        "getIndex",
    ]
    args = [
        [],
        [12],
        [8],
        [1],
        [12],
        [0],
        [12],
        [8],
        [2],
        [2],
        [4],
        [13],
        [4],
        [12],
        [6],
        [11],
        [1],
        [10],
        [2],
        [3],
        [1],
        [6],
        [14],
        [5],
        [6],
        [12],
        [3],
        [12],
        [15],
        [6],
        [7],
        [8],
        [13],
        [15],
        [15],
        [10],
        [9],
        [12],
        [12],
        [9],
        [9],
        [9],
        [9],
        [4],
        [8],
        [11],
        [15],
        [9],
        [1],
        [4],
        [10],
        [9],
    ]
    outputs = [
        None,
        None,
        None,
        8,
        None,
        12,
        None,
        None,
        24,
        24,
        None,
        None,
        4,
        None,
        12,
        None,
        20,
        None,
        24,
        None,
        None,
        37,
        None,
        None,
        42,
        None,
        360,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        220560,
        None,
        None,
        None,
        285845760,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        150746316,
    ]
    f = Fancy()
    for op, arg, out in zip(operation[1:], args[1:], outputs[1:]):
        attr = getattr(f, op)
        res = attr(arg[0])
        assert out == res
