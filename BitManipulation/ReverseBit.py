class Solution:
    def reverseBits(self, n: int) -> int:
        origin  = "{:032b}".format(n)
        reversed = 0
        for i in origin[::-1]:
            reversed = reversed << 1
            reversed += int(i)

        return reversed