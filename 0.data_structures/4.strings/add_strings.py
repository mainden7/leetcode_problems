class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        numbers = list()
        for num in num1, num2:
            number1 = 0
            for digit in num:
                number1 *= 10
                digit = ord(digit) - ord("0")
                number1 += digit
            numbers.append(number1)
        result = sum(numbers)
        return str(result)



if __name__ == '__main__':
    print(Solution().addStrings(
        "456",
        "77"
    ))