R = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
extr = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900
}


class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) == 1:
            return R[s]

        digits = []
        rs = list(s)
        i = 0
        while i < len(s):
            letter = rs[i]
            if i + 1 < len(rs):
                nx = rs[i + 1]
                com = letter + nx
                if com in extr:
                    digits.append(extr[com])
                    i += 2
                    continue
            digits.append(R[letter])
            i += 1

        print(digits)
        return sum(digits)




if __name__ == '__main__':
    print(Solution().romanToInt(
        "LVIII"
    ))