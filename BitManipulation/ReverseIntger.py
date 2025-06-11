class Solution:
    def reverse(self, x: int) -> int:
        reversed = ''
        str_x = str(x)
        str_x.rstrip('0')
        if x < 0:
            reversed += '-'
        for c in str_x[::-1]:
            if c.isdigit():
                reversed += c
            else:
                break
        if int(reversed) > 2**31 - 1 or int(reversed) < -(2**31):
            return 0
        return int(reversed)