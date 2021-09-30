class Solution:
    def is_valid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        def pair(a, b):
            d = {"(": ")", ")": "(", "[": "]", "]": "[", "{": "}", "}": "{"}

            return d[a] == b

        queue = []
        opened = ["(", "[", "{"]
        closed = [")", "]", "}"]

        for b in s:
            if b in opened:
                queue.append(b)

            if b in closed:
                try:
                    ele = queue.pop()
                except IndexError:
                    return False

                if not pair(b, ele):
                    return False
        if queue:
            return False

        return True
