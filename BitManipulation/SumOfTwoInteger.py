class Solution:
    def getSum(self, a: int, b: int) -> int:
        BITS = 32
        MASK = 0xFFFFFFFF

        a = a & MASK
        b = b & MASK
        
        a_bin = format(a, f'0{BITS}b')
        b_bin = format(b, f'0{BITS}b')
        
        carry = 0
        res = ['0'] * BITS
        
        for i in range(BITS - 1, -1, -1):
            ope_1 = int(a_bin[i])
            ope_2 = int(b_bin[i])
            
            s = ope_1 ^ ope_2 ^ carry
            carry = (ope_1 & ope_2) | (ope_1 & carry) | (ope_2 & carry)
            
            res[i] = str(s)
        
        res = "".join(res)
        if res[0] == '1':
            res = int(res, 2) - (1 << BITS)
        else:
            res = int(res, 2)
        return res
