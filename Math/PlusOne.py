class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = 0
        for i, num in enumerate(digits[::-1]):
            total += num * pow(10, i)
        total += 1

        output = list()
        while total != 0:
            digit = total % 10
            print(digit)
            output.append(digit)
            total //= 10
        print(output)
        output.reverse()

        return output